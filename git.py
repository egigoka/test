#! python3
# -*- coding: utf-8 -*-
from commands7 import *

arguments = list(sys.argv)
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
    message = "default message used to commit " + string
    Print.debug("message", message)
    warning(" ")
    warning(string)
    warning(message)
Git.update(string)
