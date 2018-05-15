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
from pip8 import *

Pip.uninstall("pyautogui")
Pip.uninstall("paramiko")
Pip.uninstall("win_unicode_console")
Pip.uninstall("pywin32")
Pip.uninstall("termcolor")
Pip.uninstall("colorama")
Pip.uninstall("termcolor")
Pip.uninstall("pyperclip")
Pip.uninstall("copypaste")

#os.system(Locations.py + " ./commands8.py")
