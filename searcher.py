import os
import sys
from commands import *
print("searcher 0.5.2")

file_extensions=[]  # cached
skipped_file_substrings = []  # cached

case_sensitive=False  # cached partially

match_strings=['navigation']  # not cached
skipped_strings = []  # not cached
multiple_lines=True  # not cached
end_print_files_dict=True  # not cached
skip_over_this_size = 2 * GiB  # not cached
stop_after_every_found_line=False # not cached
end_print_files_dict=True # not cached

folder = OS.args[1]

if Dir.exist(folder):
	paths = [folder]
else:
	paths=['.']

skipped_paths=['/mnt/c/Windows/',
               '/mnt/c/program files/',
               '/mnt/c/program files (x86)/',
               '/mnt/c/programdata/',
               '/mnt/c/MSOCache',
               r'c:\Windows',
               r'c:\program files',
               r'c:\program files (x86)',
               r'c:\MSOCache',
               r'c:\programdata',
               r'C:\Users\Egorov\Documents\!Не моё']

whoami = Console.get_output("whoami").strip()
if OS.windows:
    username = whoami.split(backslash)[1] + "." + whoami.split(backslash)[0]
else:
    username = whoami

cache_create = "--cache-create" in OS.args or "--create-cache" in OS.args
cache_load = "--cache-load" in OS.args or "--load-cache" in OS.args
debug = "--debug" in OS.args

if cache_create:
    print("creating cache...")
if cache_load:
    print("loading cache...")


_printed_results = []

def print_result(file, line, line_cnt, found_string):
    Print.rewrite()
    if file not in _printed_results:
        Print.colored(file, "green")
    if file not in _printed_results or multiple_lines:
        line = line.replace(found_string, Print.colored(found_string, "red", verbose=False))
        Print.colored(fr"{line_cnt}:{line}"[:(Console.width() * 5) - 3] + "...")
        _printed_results.append(file)


def check_strings(string, substring, case_sensitive):
    if case_sensitive:
        string_needed_case = string
        substring_needed_case = substring
    elif not case_sensitive:
        string_needed_case = string.lower()
        substring_needed_case = substring.lower()
    
    return substring in string


files_to_read = []

if cache_create or cache_load:
    files_to_read = JsonList("searcher_cache.json")
if cache_create:
    files_to_read.string = []

print(f"{Time.dotted()} search files")

cnt = 0
if not cache_load:
    for path in paths:
        path = Path.combine(path, "")
        for root, dirs, files in os.walk(path):
            cnt += 1
            if cnt % 100 == 0:
                Print.rewrite(f"{cnt}/???", root)
            skipped = False
            for skipped_path in skipped_paths:
                
                if root.lower().startswith(skipped_path.lower()) and skipped_path != "":
                    skipped = True
                    break
            
            if not skipped:
                for file in files:
                    skipped_file = False
                    for skipped_substring in skipped_file_substrings:
                        skipped_substring = skipped_substring if case_sensitive else skipped_substring.lower()
                        file_needed_case = file if case_sensitive else file.lower()
                        if skipped_substring in file_needed_case:
                            skipped_file = True
                            break
                    if skipped_file:
                        continue
                    file_path = Path.combine(root, file)
                    if not file_extensions: ## if empty
                        files_to_read.append(file_path)
                        continue
                    for ext in file_extensions:
                        if file.lower().endswith(ext.lower()):
                            files_to_read.append(file_path)
                            break

if cache_create:
    files_to_read.save()

len_files_to_read = len(files_to_read)

Print.rewrite()
print(f"{Time.dotted()} {len_files_to_read} files to read from {cnt} folders")
cnt = 0
files = []
b = Bench()
for file in files_to_read:
    if File.get_size(file) > skip_over_this_size:
        if debug:
            print("BEEG file, skip " + file)
        continue
    if debug:
        print(file)
    time = b.end(start_immediately=True)
    if time > 1:
        print(time, b.prefix)
    cnt += 1
    if cnt % 100 == 0:
        Print.rewrite(f"{cnt}/{len_files_to_read}", file)
    try:
        file_content = File.read(file)
    except (PermissionError, FileNotFoundError) as e:
        Print.rewrite()
        print(e)
        continue
    file_lines = Str.nl(file_content)
    for line_cnt, line in enumerate(file_lines):
        skip = False
        for string in skipped_strings:
            if check_strings(line, string, case_sensitive):
                skip = True
                break
        if skip:
            break
    if skip:
            continue
    add_to_result = False
    for line_cnt, line in enumerate(file_lines):
        for string in match_strings:
            if check_strings(line, string, case_sensitive):
                print_result(file, line, line_cnt, string)
                add_to_result = True
    if add_to_result:
        files.append(file)
    b.prefix = file

time = b.end(start_immediately=True)
if time > 1:
    print(time, b.prefix)

print(f"{Time.dotted()} end")

print()

if end_print_files_dict:
    for file in files:
        print('npp "' + file + '"')
    
