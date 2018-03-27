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


class Arguments:
    notab = False
    if "notab" in sys.argv:
        notab = True
    nonewline = False
    if "nonewline" in sys.argv:
        nonewline = True
    verbose = False
    if "verbose" in sys.argv:
        verbose = True


oldinputstr = ""
while True:
    time.sleep(0.1)
    inputstr = copypaste.paste()
    if inputstr == "":
        continue
    if Arguments.verbose:
        if oldinputstr != inputstr:
            print (repr(inputstr), newline)
            oldinputstr = inputstr
    inputstr = str(inputstr)
    if Arguments.nonewline:
        inputstr = inputstr.replace(newline2, "")
        inputstr = inputstr.replace(newline, "")
    if Arguments.notab:
        inputstr = inputstr.replace("\t", "")
    copypaste.copy(inputstr)