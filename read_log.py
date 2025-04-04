import uuid
import sys
import csv
import math
import binascii
from datetime import datetime
from datetime import timedelta
from commands import Time, Console, Print, ID, Int, OS, dirify
from smbprotocol.connection import Connection, Dialects
from smbprotocol.open import (Open, CreateDisposition, FilePipePrinterAccessMask, FileAttributes, ImpersonationLevel,
                              ShareAccess, CreateOptions, RequestedOplockLevel)
from smbprotocol.session import Session
from smbprotocol.tree import TreeConnect
from smbprotocol.exceptions import (SMBResponseException, SharingViolation, SMBConnectionClosed, SMBException,
                                    RequestNotAccepted)

if "test" in OS.args:
    from creds_test import server, share, user, password
    server_name = "test"
elif "prod" in OS.args:
    from creds_prod import server, share, user, password
    server_name = "prod"
else:
    print("Use \"test\" or \"prod\" argument to select server")

LOG_LEVELS = ["Trace", "Debug", "Info", "Warning", "Error", "Fatal", "Unknown"]
MIN_LOG_LEVEL_STRING = "Trace"
for arg in OS.args:
    prefix = "--min-log-level="
    if arg.startswith(prefix):
        MIN_LOG_LEVEL_STRING = arg[len(prefix):].title()
    if MIN_LOG_LEVEL_STRING not in LOG_LEVELS:
        raise ValueError(f"Log level \"{MIN_LOG_LEVEL_STRING}\" isn't supported. Supported are " + ", ".join(LOG_LEVELS))
MIN_LOG_LEVEL = LOG_LEVELS.index(MIN_LOG_LEVEL_STRING)


def clear_cache():
    global CACHE

    try:
        max_cache = max(CACHE.keys())
    except ValueError:
        return

    CACHE = {max_cache: CACHE[max_cache]}



def decode_utf8(byte_array):
    try:
        return byte_array[::-1].decode('utf-8', errors='replace')
    except UnicodeError:
        print(byte_array[::-1])
        raise


def smb_read_with_retry(file, position, length):
    while True:
        try:
            return file.read(position, length)
        except SMBResponseException:
            Time.sleep(1, verbose=True)


def get_byte_from_cache(byte_array, position, file, cached_position, length):
    global CACHE
    cached = byte_array[position:position + 1]
    if cached:
        return cached
    else:
        new_cache = smb_read_with_retry(file, cached_position, length)
        CACHE[cached_position] = new_cache
        return new_cache[position:position+1]


def read_cached(file, position, cache_length=16834):
    global CACHE
    if cache_length == 1:
        return file.read(position, 1)
    
    cached_position = position - position % cache_length
    if cached_position not in CACHE:
        CACHE[cached_position] = smb_read_with_retry(file, cached_position, cache_length)
    out = get_byte_from_cache(CACHE[cached_position], position - cached_position, file, cached_position, cache_length)
    return out


def disconnect(obj):
    try:
        obj.disconnect()
    except Exception:
        pass


def restart_connection():
    global CONNECTION
    global SESSION
    global TREE
    
    disconnect(CONNECTION)
    disconnect(SESSION)
    disconnect(TREE)
    
    CONNECTION = Connection(uuid.uuid4(), server, 445)
    CONNECTION.connect(Dialects.SMB_3_0_2)

    SESSION = Session(CONNECTION, user, password)
    SESSION.connect()

    TREE = TreeConnect(SESSION, "\\\\{}\\{}".format(server, share))
    TREE.connect()


def open_file_smb(file_path):
    open_file = Open(TREE, file_path)
    
    impersonation_level = ImpersonationLevel.Impersonation
    desired_access = FilePipePrinterAccessMask.FILE_READ_DATA | FilePipePrinterAccessMask.FILE_READ_EA | FilePipePrinterAccessMask.FILE_READ_ATTRIBUTES | FilePipePrinterAccessMask.READ_CONTROL | FilePipePrinterAccessMask.SYNCHRONIZE
    file_attributes = FileAttributes.FILE_ATTRIBUTE_NORMAL
    share_access = ShareAccess.FILE_SHARE_READ | ShareAccess.FILE_SHARE_WRITE
    create_disposition = CreateDisposition.FILE_OPEN
    create_options = CreateOptions.FILE_NON_DIRECTORY_FILE | CreateOptions.FILE_NON_DIRECTORY_FILE
    # create_contexts = None
    oplock_level = RequestedOplockLevel.SMB2_OPLOCK_LEVEL_NONE
    send = True
    
    create_context_data = binascii.unhexlify(b"""
28 00 00 00 10 00 04 00 00 00 18 00 10 00 00 00
44 48 6e 51 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 18 00 00 00 10 00 04 00
00 00 18 00 00 00 00 00 4d 78 41 63 00 00 00 00
00 00 00 00 10 00 04 00 00 00 18 00 00 00 00 00
51 46 69 64 00 00 00 00
""".replace(b' ', b'').replace(b'\n', b''))
    
    print(f"{impersonation_level=}, {desired_access=}, {file_attributes=}, {share_access=}, {create_disposition=}, {create_options=}, {create_context_data=}, {oplock_level=},{send=}")
    
    open_file.create(
        impersonation_level = impersonation_level,
        desired_access = desired_access,
        file_attributes = file_attributes,
        share_access = share_access,
        create_disposition = create_disposition,
        create_options = create_options,
        create_contexts = create_context_data,
        oplock_level = oplock_level,
        send = send
    )

    return open_file


def open_file_safely(file_path):
    global TREE
    if not TREE:
        restart_connection()
    
    # open the file
    while True:
        try:
            open_file = open_file_smb(file_path)
            break
        except (SMBResponseException, SharingViolation, SMBConnectionClosed, SMBException, RequestNotAccepted):
            Time.sleep(1, verbose=True)
            restart_connection()

    return open_file


def read_file(open_file, position, last_position, first_run, num_lines, previous_line):
    lines = []
    bytes_newline = b'\n'
    buffer = bytearray()

    cnt_lines = 0
    cnt_chars = 0
    while (len(lines) < num_lines and first_run) or position > last_position:
        if position < 0:
            break
        if cnt_chars % 1000 == 0 or len(lines) != previous_line:
            of = f"/{num_lines}" if first_run else ""
            Print.rewrite(f"{cnt_lines}{of} lines, {cnt_chars} chars")
            previous_line = len(lines)
        # read one character
        character = read_cached(open_file, position)

        # move the position
        position -= 1

        # append the character to the buffer
        if character == bytes_newline:
            lines.append(decode_utf8(buffer))

            buffer = bytearray()
            cnt_lines += 1
        else:
            buffer.extend(character)
        cnt_chars += 1
    # append the last line
    if buffer:
        lines.append(decode_utf8(buffer))

    return lines


def get_colors(row, line_print_number):
    level = row[3]
    username = row[6]

    if username.strip() == "Егоров Егор":
        color = "magenta"
        back = "on_white"
    elif username.strip() == "Мулинов Ерик":
        color = "green"
        back = "on_white"
    else:
        color = "black"
        back = "on_white"

    if line_print_number % 2 == 1:
        back = ""

    if level in ["Warning"]:
        color = "yellow"
    elif level in ["Error"]:
        color = "red"
    elif level in ["Fatal", "Unknown"]:
        color = "white"
        back = "on_red"
    elif level in ["Debug", "Info"]:
        color = "blue"

    return color, back


def csv_line_to_list(string):
    reader = csv.reader([string], delimiter=';', quotechar='"')
    row = reader.__next__()
    return row


def get_widths():
    widths = [19, 45, 52, 5, 999, 999, 44]
    sum_widths = sum(widths) + 20
    console_width = Console.width()
    if sum_widths > console_width:
        widths[4] -= math.ceil((sum_widths - console_width) / 2)
        widths[5] -= math.ceil((sum_widths - console_width) / 2)
    return widths


def get_time(row):
    time = row[0]
    time = time.replace("\ufeff", "")
    time = time.replace('"', "")
    try:
        time = datetime.strptime(time, "%d.%m.%Y %H:%M:%S")
    except ValueError:
        Print.debug(time)
        raise
    return time


def format_substring(substring, row_cnt, width, is_any):
    substring = f"{substring}".replace("\t", "\\t")

    start = width * (9 - row_cnt)
    end = start + width

    if start < 0 and end < 0:
        start = 0
        end = 0
    if end < 0:
        end = len(substring)
    if start < 0:
        start = 0

    substring = substring[start:end]

    if substring:
        is_any = True
    substring = f"{substring.ljust(width)} |"
    if row_cnt == 0 and len(substring.strip()) != 1:
        substring = substring[:-4] + ">>>|"
    return substring, is_any


def get_substrings(row, row_cnt, widths):
    substrings = []
    is_any = False
    for i, subline in enumerate(row):
        try:
            width = widths[i]
        except IndexError:
            break
        if i == 2:
            subline = subline.replace("МуравьинаяЛогистика.", "")
        substring, is_any = format_substring(subline, row_cnt, width, is_any)
        substrings.append(substring)
    return substrings, is_any


def get_time_color(diff):
    time_color = ["white", "on_green"]
    time_suffix = 8

    minutes = diff.seconds // 60
    minutes += diff.days * 1440
    
    if minutes in Int.from_to(5, 14):
        time_color = ["on_light_green"]
        time_suffix -= 1
    elif minutes in Int.from_to(15, 29):
        time_color = ["white", "on_yellow"]
        time_suffix -= 2
    elif minutes in Int.from_to(30, 59):
        time_color = ["on_light_yellow"]
        time_suffix -= 3
    elif minutes in Int.from_to(60, 119):
        time_color = ["white", "on_blue"]
        time_suffix -= 4
    elif minutes in Int.from_to(120, 179):
        time_color = ["on_light_blue"]
        time_suffix -= 5
    elif minutes in Int.from_to(180, 239):
        time_color = ["white", "on_red"]
        time_suffix -= 6
    elif minutes in Int.from_to(240, 1439):
        time_color = ["on_light_red"]
        time_suffix -= 7
    elif minutes >= 1440:
        time_color = ["white", "on_black"]
        time_suffix -= 8

    time_suffix = " " * time_suffix

    return time_suffix, time_color


def get_diff_and_formatted(last_time):
    now = datetime.now()
    diff = now - last_time
    if now < last_time:
        diff = timedelta(0, 0, 0, 0, 0, 0, 0)
    diff_formatted = f"{diff.seconds // 3600:02}:{(diff.seconds // 60) % 60:02}:{diff.seconds % 60:02}"
    if diff.days > 0:
        days = diff.days
        days_suffix = "" if days == 1 else "s"
        diff_formatted = f"{days} day{days_suffix} {diff_formatted}"
    return now, diff, diff_formatted


def is_printable(row):
    level_string = row[3]
    level = LOG_LEVELS.index(level_string)
    return level >= MIN_LOG_LEVEL


def close_file(file):
    if file is None:
        return
    #if not file.connected:
    #    return
    
    Print.rewrite()
    cnt = 0
    while True:
        
        cnt += 1
        if cnt != 1:
            Print(f"Trying to release file, try {cnt}")
        try:
            file.close()
        except Exception:
            Time.sleep(1, verbose=True)
            continue
        Print.rewrite()
        if cnt != 1:
            Print(f"file released try {cnt}")
        # Print(f"file released try {cnt}")
        return


def main():
    
    # init logic
    try:
        csv.field_size_limit(sys.maxsize)
    except OverflowError:
        csv.field_size_limit(pow(2,31)-1)  # windows
    line_cnt = ID()
    last_time = datetime.now()
    first_run = True
    num_lines = int(sys.argv[1])
    last_position = 0
    file_path = "Public\\Logs\\МуравьинаяЛогистика.csv"
    open_file = None

    while True:
        close_file(open_file)
        
        try:
            print(f"opened {file_path=}")
            open_file = open_file_safely(file_path)

            # get the file size
            position = open_file.end_of_file - 1

            # save the position
            position_end = position
            previous_line = 0
            if first_run:
                last_position = position

            # read the file
            lines_from_file = read_file(open_file, position, last_position, first_run, num_lines, previous_line)
        except Exception:
            raise
        finally:
            input("debug, file not closed, press Enter to run further")
            close_file(open_file)

        # update the position
        last_position = position_end

        # print the lines
        len_lines = len(lines_from_file)
        for cnt_line, line in enumerate(lines_from_file[::-1]):
            if line.strip() == "":
                continue

            # skip last SKIP_LINES lines
            if (len_lines - cnt_line) <= SKIP_LAST:
                continue

            row = csv_line_to_list(line)

            if not is_printable(row):
                continue
                
            line_print_number = line_cnt.get()

            color, back = get_colors(row, line_print_number)
            widths = get_widths()
            last_time = get_time(row)
            lines_to_print = []

            for cnt in reversed(range(10)):
                substrings, is_any = get_substrings(row, cnt, widths)

                if is_any:
                    lines_to_print.append(" ".join(substrings))
                else:
                    break

            for line_current in lines_to_print:
                if back:
                    Print.colored(line_current, back, color)
                else:
                    Print.colored(line_current, color)

        # print current time and time since last log
        now, diff, diff_formatted = get_diff_and_formatted(last_time)
        time_suffix, time_color = get_time_color(diff)
        Print.colored(f'{now.strftime("%d.%m.%Y %H:%M:%S")} | {diff_formatted} since last log in {server_name}{time_suffix}',
                      *time_color, end="\n" if FAST_EXIT else "\r")

        if FAST_EXIT:
            break

        clear_cache()
        first_run = False

        Time.sleep(1, verbose=False)


CACHE = {}
TREE = None
CONNECTION = None
SESSION = None

SKIP_LAST = 0
for arg in sys.argv:
    if arg.startswith("--skip="):
        SKIP_LAST = int(arg.split("=")[1])

FAST_EXIT = "--fast-exit" in sys.argv

if __name__ == "__main__":
    main()
