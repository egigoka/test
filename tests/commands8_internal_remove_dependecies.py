#! python3
# -*- coding: utf-8 -*-
# http://python.su/forum/topic/15531/?page=1#post-93316
import sys
sys.path.append("../..")
sys.path.append("..\..")
sys.path.append(".")
sys.path.append("..")
sys.path.append("./term")
sys.path.append(r".\term")
from commands8 import *

Pip.uninstall("pyautogui", force=True)
Pip.uninstall("paramiko", force=True)
Pip.uninstall("win_unicode_console", force=True)
Pip.uninstall("pywin32", force=True)
Pip.uninstall("termcolor", force=True)
Pip.uninstall("colorama", force=True)
Pip.uninstall("termcolor", force=True)
Pip.uninstall("pyperclip", force=True)
Pip.uninstall("copypaste", force=True)

#os.system(Locations.py + " ./commands8.py")