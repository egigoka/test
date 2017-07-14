#! python3
# -*- coding: utf-8 -*-

from commands7 import *
if get_os() == "macos":
    File.copy(Path.extend("..", "..", "commands7.py"), "commands7.py")


prefix = "B33-"
cnt_start = 22
cnt_end = 24
roots = range(cnt_start, cnt_end+1)
suffixes = []
#suffixes.append("-0A")
#suffixes.append("-0B")
#suffixes.append("-0C")
suffixes.append("-1A")
#suffixes.append("-1B")
#suffixes.append("-1C")
suffixes.append("-2A")
#suffixes.append("-2B")
#suffixes.append("-2C")
suffixes.append("-3")
suffixes.append("-4")
suffixes.append("-5")
suffixes.append("-6")
#suffixes.append("-7")

count = 0
#for prefix in [prefix, "S10-", "S11-", "S12-", "S13-", "S14-", "S48-"]:
if True:
    Codegen.start("output.txt")
    for root in roots:
        for suffix in suffixes:
            root = Str.leftpad(root, 2, 0)
            Codegen.add_line(prefix + str(root) + suffix + newline)
            print(prefix, root, suffix, sep='')
            count += 1
    Codegen.end()

cprint("Напечатано " + str(count) + " ячеек для  группы", "grey", "on_white")
