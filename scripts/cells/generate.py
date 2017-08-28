#! python3
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, "..")
sys.path.insert(0, "../..")
sys.path.insert(0, "..\..")
from commands7 import *  # mine commands


prefix = "N22-"
roots = Int.from_to(28, 33, to_str=True)
suffixes = []
#suffixes.append("-0A")
#suffixes.append("-0B")
#suffixes.append("-0C")
suffixes.append("-1A")
suffixes.append("-1B")
suffixes.append("-1C")
#suffixes.append("-2A")
#suffixes.append("-2B")
#suffixes.append("-2C")
#suffixes.append("-3")
#suffixes.append("-4")
#suffixes.append("-5")
#suffixes.append("-6")
#suffixes.append("-7")

count = 0
#for prefix in [prefix, "S10-", "S11-", "S12-", "S13-", "S14-", "S48-"]:
if True:
    Codegen.start("output.txt")
    for root in roots:
        for suffix in suffixes:
            root = Str.leftpad(root, 2, 0)
            Codegen.add_line(prefix + root + suffix + newline)
            print(prefix, root, suffix, sep='')
            count += 1
    Codegen.end()

cprint("Напечатано " + str(count) + " ячеек для  группы", "grey", "on_white")
