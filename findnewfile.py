from commands import *

lbfiles = Dir.list_of_files(r"\\Mac\Home\Desktop\ListBoxerFull\ListBoxer")

s32path = r"C:\Windows\System32"

for file in lbfiles:
    try:
        Print(file, File.get_modification_time(Path.combine(s32path, file)), sep="\t")
    except FileNotFoundError:
        pass
