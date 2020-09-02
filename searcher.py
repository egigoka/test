import os
import sys
from commands import *
print("searcher 0.2.5")

whoami = Console.get_output("whoami").strip()
username = whoami.split(backslash)[1] + "." + whoami.split(backslash)[0]

paths=['C:\\']
skipped_paths=['']
file_extensions=[".py"]
skipped_file_extensions=['.w2p', '.png', '.gif', '.jpg', '.gz', '.ico', '.pdf', '.jpeg', '.icns', '.sqlite', '.pyc']
match_strings=['bitrix24.ru']
case_sensitive=True
multiple_lines=True
stop_after_every_found_line=False
end_print_files_dict=True

_printed_results = []


def print_result(file, line, line_cnt):
    Print.rewrite()
    if file not in _printed_results:
        Print.colored(file, "green")
    if file not in _printed_results or multiple_lines:
        Print.colored(fr"{line_cnt}:{line}", "yellow")
        _printed_results.append(file)


files_to_read = []

print(f"{Time.dotted()} search files")
for path in paths:
    path = Path.combine(path, "")
    for root, dirs, files in os.walk(path):
        skipped = False
        for skipped_path in skipped_paths:
            if root.lower().startswith(Path.combine(skipped_path, "").lower()) and skipped_path != "":
                skipped = True
                break
        if not skipped:
            for file in files:
                file_path = Path.combine(root, file)
                for ext in file_extensions:
                    if File.get_extension(file) == ext:
                        files_to_read.append(file_path)

print(f"{Time.dotted()} read {len(files_to_read)} files")
for file in files_to_read:
    for line_cnt, line in enumerate(Str.nl(File.read(file))):
        for string in match_strings:
            if case_sensitive:
                if string in line:
                    print_result(file, line, line_cnt)
            else:
                if string.lower() in line.lower():
                    print_result(file, line, line_cnt)

print(f"{Time.dotted()} end")
