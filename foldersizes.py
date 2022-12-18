from commands import *

folders = OS.args

for folder in folders:
    if not Dir.exist(folder):
        folders.pop(folders.index(folder))

previous = {}

try:
    while True:
        for folder in folders:
            total_size = 0
            for root, dirs, files in OS.walk(folder):
                for file in files:
                    total_size += File.get_size(Path.combine(root, file))
            print(folder, File.format_size_human_readable(total_size))
except KeyboardInterrupt:
    print("^C")
