from creds import server, share, user, password
import uuid
import sys
import csv
import math
from datetime import datetime
from commands import Time, Console, Print, ID
from smbprotocol.connection import Connection, Dialects
from smbprotocol.open import Open, CreateDisposition, FilePipePrinterAccessMask, FileAttributes, ImpersonationLevel, \
    ShareAccess, CreateOptions, DirectoryAccessMask, FileInformationClass
from smbprotocol.session import Session
from smbprotocol.tree import TreeConnect
from smbprotocol.exceptions import SMBResponseException, SharingViolation, SMBConnectionClosed

csv.field_size_limit(sys.maxsize)
line_cnt = ID()


def clear_cache():
    global cache
    cache = {max(cache.keys()): cache[max(cache.keys())]}


def decode_utf8(bytearray, reverse=True):
    bytes = bytearray
    if reverse:
        bytes = bytearray[::-1]
    try:
        return bytes.decode('utf-8', errors='replace')
    except UnicodeError:
        print(bytes)
        raise


cache = {}


def smb_read_with_retry(file, position, length):
    while True:
        try:
            return file.read(position, length)
        except SMBResponseException:
            Time.sleep(1, verbose=True)


def get_byte_from_cache(bytes, position, file, cached_position, length):
    cached = bytes[position:position + 1]
    if cached:
        return cached
    else:
        new_cache = smb_read_with_retry(file, cached_position, length)
        cache[cached_position] = new_cache
        return new_cache[position:position + 1]


def read_cached(file, position, cache_length=4096):
    if cache_length == 1:
        return file.read(position, 1)

    cached_position = position - position % cache_length
    if not cached_position in cache:
        cache[cached_position] = smb_read_with_retry(file, cached_position, cache_length)
    out = get_byte_from_cache(cache[cached_position], position - cached_position, file, cached_position, cache_length)
    return out


file_path = "Public\\Logs\\МуравьинаяЛогистика.csv"
folder_path = "Public\\Logs\\"

# Set up the SMB connection
connection = Connection(uuid.uuid4(), server, 445)
connection.connect(Dialects.SMB_3_0_2)

# Start an SMB session
session = Session(connection, user, password)
session.connect()

# Connect to the SMB share
tree = TreeConnect(session, "\\\\{}\\{}".format(server, share))
tree.connect()

# get list of files
# Open the directory
directory = Open(tree, folder_path)
desired_access=DirectoryAccessMask.FILE_LIST_DIRECTORY
file_attributes=FileAttributes.FILE_ATTRIBUTE_DIRECTORY
share_access=ShareAccess.FILE_SHARE_READ
create_disposition=CreateDisposition.FILE_OPEN
create_options=CreateOptions.FILE_DIRECTORY_FILE
file_information_class=FileInformationClass.FILE_NAMES_INFORMATION
directory.create(ImpersonationLevel.Impersonation, desired_access, file_attributes, share_access, create_disposition, file_information_class)

# List the files in the directory
files = directory.query_directory("*", file_information_class)

# init logic
newline = "\n"
bnewline = b'\n'
all = False
try:
    num_lines = int(sys.argv[1])
except ValueError:
    if sys.argv[1] == "all":
        all = True
        num_lines = 1_000_000_000
    else:
        raise
first_run = True
last_position = 0
buffer = bytearray()

statistics = {}

def open_file_safely(tree, file_path):
    while True:
        try:
            open_file = Open(tree, file_path)
            open_file.create(
                ImpersonationLevel.Impersonation,
                FilePipePrinterAccessMask.FILE_READ_DATA | FilePipePrinterAccessMask.FILE_READ_ATTRIBUTES,
                FileAttributes.FILE_ATTRIBUTE_NORMAL,
                ShareAccess.FILE_SHARE_READ,
                CreateDisposition.FILE_OPEN,
                CreateOptions.FILE_NON_DIRECTORY_FILE
            )
            break
        except (SharingViolation, SMBConnectionClosed) as e:
            Time.sleep(1, verbose=True)
            continue
    return open_file


for file in files:

    bytes_field = file['file_name']
    # Assuming `bytes_field` is your BytesField object
    raw_bytes = bytes_field.get_value()

    # Decode the bytes to a string using utf-8 encoding or another appropriate encoding
    string_value = raw_bytes.decode('utf-16-le')

    if not string_value.endswith(".csv"):
        continue

    print(f"Reading {string_value}")

    file_path = f"{folder_path}{string_value}"

    # init
    lines = []

    # open the file
    open_file = open_file_safely(tree, file_path)

    # Query the file size
    position = open_file.end_of_file - 1
    last_position = position

    if not all:
        # read last line
        # print(f"{len(lines)} < {num_lines} and {first_run} or {position} > {last_position}")
        previous_line = 0
        cnt_lines = 0
        cnt_chars = 0
        # Print.rewrite()
        # print(f"{len(lines)} < {num_lines * 2}")
        while len(lines) < num_lines:
            if position < 0:
                break
            if cnt_chars % 100 == 0 or len(lines) != previous_line:
                of = f"/{num_lines}" if first_run else ""
                Print.rewrite(f"{cnt_lines}{of} lines, {cnt_chars} chars")
                previous_line = len(lines)
            # read one character
            character = read_cached(open_file, position)

            # move the position
            position -= 1

            # append the character to the buffer
            # print(f"{character=} {character == bnewline=} {position=}")
            if character == bnewline:
                # lines.insert(0, decode_utf8(buffer))
                lines.append(decode_utf8(buffer))
                buffer = bytearray()
                cnt_lines += 1
            else:
                buffer.extend(character)
            cnt_chars += 1

        # append the last line
        if buffer:
            # lines.insert(0, decode_utf8(buffer))
            lines.append(decode_utf8(buffer))
            # lines.append(decode_utf8(buffer))
            buffer = bytearray()

        lines_last = lines[::-1]
        lines = []

    # read first line
    first_line = True
    cnt_lines = 0
    cnt_chars = 0
    position = 0

    while len(lines) < num_lines or all:
        if position > last_position:
            break
        if cnt_chars % 1000 == 0 or len(lines) != previous_line:
            of = f"/{num_lines}" if first_run else ""
            Print.rewrite(f"{cnt_lines}{of} lines, {cnt_chars} chars, {cnt_chars / last_position * 100:.2f}%, {cnt_chars / 1024 / 1024:.2f}MB")
            previous_line = len(lines)
        # read one character
        character = read_cached(open_file, position)

        # move the position
        position += 1

        # append the character to the buffer
        # print(f"{character=} {character == bnewline=} {position=}")
        if character == bnewline:
            new_line = decode_utf8(buffer, reverse=False)
            new_line = new_line.replace("\r", "")
            if not new_line.strip():
                continue
            # lines.insert(0, new_line)
            lines.append(new_line)
            buffer = bytearray()
            cnt_lines += 1
        else:
            buffer.extend(character)
        cnt_chars += 1

    # append the last line
    if buffer:
        # lines.insert(0, decode_utf8(buffer, reverse=False))
        lines.append(decode_utf8(buffer, reverse=False))
        buffer = bytearray()




    # close the file
    open_file.close()

    if not all:
        lines += lines_last

    # print the lines
    for line in lines:
        if line.strip() == "":
            continue
        color = None
        cnt_line = line_cnt.get()
        if line.strip().endswith('"Егоров Егор"'):
            color = "magenta"
            back = "on_white"
        elif line.strip().endswith('"Мулинов Ерик"'):
            color = "blue"
            back = "on_white"
        else:
            color = "black"
            back = "on_white"

        if cnt_line % 2 == 1:
            back = ""
        reader = csv.reader([line], delimiter=';', quotechar='"')
        row = reader.__next__()
        line = "| "
        widths = [19, 46, 79, 5, 999, 999, 42]
        sum_widths = sum(widths) + 20
        console_width = Console.width()
        if sum_widths > console_width:
            widths[4] -= math.ceil((sum_widths - console_width) / 2)
            widths[5] -= math.ceil((sum_widths - console_width) / 2)
        lines_current = []
        for cnt in reversed(range(10)):
            sublines = []
            is_any = False
            for i in range(len(row)):
                try:
                    width = widths[i]
                except IndexError:
                    break
                subline = f"{row[i]}".replace("\t", "\\t")

                start = width * (9 - cnt)
                end = start + width

                if start < 0 and end < 0:
                    start = 0
                    end = 0
                if end < 0:
                    end = len(subline)
                if start < 0:
                    start = 0

                # print(f"{start} {end} {subline}")
                subline = subline[start:end]

                # print(f"{start} {end} {subline}")
                # print()
                if subline:
                    is_any = True
                subline = f"{subline.ljust(width)} |"
                width = width + 2
                if cnt == 0 and len(subline.strip()) != 1:
                    subline = subline[:-4] + ">>>|"
                sublines.append(subline)

            try:
                value1 = row[0]
                value1 = value1.replace("\ufeff", "")[0:10]
                value1 = value1.replace('"', "")
                value1 = value1.replace(" ", "")
                key1 = value1[6:10] + " " + value1[3:5] + " " + value1[0:2]
            except IndexError:
                key1 = ""

            try:
                statistics[key1]
            except KeyError:
                statistics[key1] = {}

            try:
                key2 = row[6].replace("\x1a", "")
            except IndexError:
                key2 = ""

            try:
                statistics[key1][key2]
            except KeyError:
                statistics[key1][key2] = {}

            try:
                key3 = row[2]
            except IndexError:
                key3 = ""

            try:
                statistics[key1][key2][key3]
            except KeyError:
                statistics[key1][key2][key3] = 0

            try:
                statistics[key1][key2][key3] += 1
            except KeyError:
                statistics[key1][key2][key3] = 1


            # print(f"{cnt} {sublines} {is_any=}")
            if is_any:
                lines_current.append(" ".join(sublines))
            else:
                break
        if not all:
            for line_current in lines_current:
                if back:
                    Print.colored(line_current, back, color)
                else:
                    Print.colored(line_current, color)
    clear_cache()
    first_run = False

    print()

Print.prettify(statistics)