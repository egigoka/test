#! python3
# -*- coding: utf-8 -*-

from commands7 import *

if get_os() == 'macos':
    Process.start("cp", r"../../commands7.py", "commands7.py")

debug_print('Path.extend("..","..","something")',Path.extend("..","..","something"))
