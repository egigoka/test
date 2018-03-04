#! python3
# -*- coding: utf-8 -*-
from commands7 import *

arguments = sys.argv
arguments.pop(0)
print(arguments)
string = "small update (default message)"
try:
    arguments[0]
    string = ""
    for arg in arguments:
        string += arg + " "
    string = string.rstrip(" ")
except IndexError:
    warning("default message used to commit: " + string)
Git.update(string)
