#! python3
# -*- coding: utf-8 -*-
from commands7 import *

arguments = list(sys.argv)
arguments.pop(0)
string = "small update (default message)"
try:
    arguments[0]
    string = ""
    for arg in arguments:
        string += arg + " "
    string = string.rstrip(" ")
except IndexError:
    input_string = input("Enter a description or press Enter to defaul message: ")
    if input_string:
        string = input_string
Git.update(string)
