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

oldinputstr = ""
while True:
    time.sleep(0.1)
    inputstr = copypaste.paste()
    if inputstr == "":
        continue
    if oldinputstr != inputstr:
        print (repr(inputstr), newline)
        oldinputstr = inputstr
    inputstr = str(inputstr)
    inputstr = inputstr.replace(newline2, "")
    inputstr = inputstr.replace(newline, "")
    inputstr = inputstr.replace("\t", "")
    outputstr = inputstr
    copypaste.copy(outputstr)