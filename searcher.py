import os
import sys
from commands import *
print("searcher 0.2.4")

whoami = Console.get_output("whoami").strip()
username = whoami.split(backslash)[1] + "." + whoami.split(backslash)[0]

paths = ["c:"]
file_extensions= [".py"]
match_strings = ["Dump"]
case_sensitive = True
multiple_lines = True
skipped_paths = [fr"c:\Program Files (x86)",
                 fr"c:\Users\{username}\AppData\Local\atom",
                 fr"c:\Program Files",
                 fr"c:\Users\{username}\AppData\Local\Wox",
                 fr"c:\Users\{username}\.PyCharmCE2019.1",
                 fr"c:\cs\venv\Lib\site-packages\pip-19.0.3-py3.7.egg"]

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

print(f"{Time.dotted()} read files")
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
