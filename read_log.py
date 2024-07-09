import uuid
import sys
import csv
import math
from datetime import datetime
from datetime import timedelta
from commands import Time, Console, Print, ID, Int, OS
from smbprotocol.connection import Connection, Dialects
from smbprotocol.open import (Open, CreateDisposition, FilePipePrinterAccessMask, FileAttributes, ImpersonationLevel,
                              ShareAccess, CreateOptions)
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


def restart_connection():
    # Set up the SMB connection
    connection = Connection(uuid.uuid4(), server, 445)
    connection.connect(Dialects.SMB_3_0_2)

    # Start an SMB session
    session = Session(connection, user, password)
    session.connect()

    # Connect to the SMB share
    tree = TreeConnect(session, "\\\\{}\\{}".format(server, share))
    tree.connect()

    return tree


def open_file_smb(tree, file_path):
    open_file = Open(tree, file_path)
    open_file.create(
        ImpersonationLevel.Impersonation,
        FilePipePrinterAccessMask.FILE_READ_DATA | FilePipePrinterAccessMask.FILE_READ_ATTRIBUTES,
        FileAttributes.FILE_ATTRIBUTE_NORMAL,
        ShareAccess.FILE_SHARE_READ,
        CreateDisposition.FILE_OPEN,
        CreateOptions.FILE_NON_DIRECTORY_FILE)

    return open_file


def open_file_safely(file_path):
    global TREE
    if not TREE:
        TREE = restart_connection()

    # open the file
    while True:
        try:
            open_file = open_file_smb(TREE, file_path)
            break
        except (SMBResponseException, SharingViolation, SMBConnectionClosed, SMBException, RequestNotAccepted):
            Time.sleep(1, verbose=True)
            TREE = restart_connection()

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
    time_color = ["light_white", "on_green"]
    time_suffix = 8

    minutes = int(diff.seconds / 60)

    if minutes in Int.from_to(5, 14):
        time_color = ["on_light_green"]
        time_suffix = 7
    elif minutes in Int.from_to(15, 29):
        time_color = ["light_white", "on_yellow"]
        time_suffix = 6
    elif minutes in Int.from_to(30, 59):
        time_color = ["on_light_yellow"]
        time_suffix = 5
    elif minutes in Int.from_to(60, 119):
        time_color = ["light_white", "on_blue"]
        time_suffix = 4
    elif minutes in Int.from_to(120, 179):
        time_color = ["on_light_blue"]
        time_suffix = 3
    elif minutes in Int.from_to(180, 239):
        time_color = ["light_white", "on_red"]
        time_suffix = 2
    elif minutes >= 240:
        time_color = ["on_light_red"]
        time_suffix = 1

    time_suffix = " " * time_suffix

    return time_suffix, time_color


def get_diff_and_formatted(last_time):
    now = datetime.now()
    diff = now - last_time
    if now < last_time:
        diff = timedelta(0, 0, 0, 0, 0, 0, 0)
    diff_formatted = f"{diff.seconds // 3600:02}:{(diff.seconds // 60) % 60:02}:{diff.seconds % 60:02}"
    return now, diff, diff_formatted


def main():
    # init logic
    csv.field_size_limit(sys.maxsize)
    line_cnt = ID()
    last_time = datetime.now()
    first_run = True
    num_lines = int(sys.argv[1])
    last_position = 0
    file_path = "Public\\Logs\\МуравьинаяЛогистика.csv"

    while True:
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
        open_file.close()

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

            line_print_number = line_cnt.get()
            row = csv_line_to_list(line)
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
                      *time_color, end="\r")

        clear_cache()
        first_run = False

        Time.sleep(1, verbose=False)

        if FAST_EXIT:
            break


CACHE = {}
TREE = None

SKIP_LAST = 0
for arg in sys.argv:
    if arg.startswith("--skip="):
        SKIP_LAST = int(arg.split("=")[1])

FAST_EXIT = "--fast-exit" in sys.argv

if __name__ == "__main__":
    main()
