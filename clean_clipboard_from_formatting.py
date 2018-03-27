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

while True:
    input()
    inputstr = copypaste.paste()
    Print.debug("inputstr", inputstr, "type(inputstr)", type(inputstr), "repr(inputstr)", repr(inputstr))
    inputstr = str(inputstr)
    inputstr = inputstr.replace(newline2, "")
    inputstr = inputstr.replace(newline, "")
    outputstr = ""
    for symbol in inputstr:
        if (symbol == newline) or (symbol == newline2):
            continue
        try:
            Print.rewrite(symbol)
            time.sleep(0.07)
            copypaste.copy(symbol)
            outputstr += symbol
        except:
            pass

    Print.debug("outputstr", outputstr, "repr(outputstr)", repr(outputstr))
    #print("NOT COPYING NOW!")
    copypaste.copy(outputstr)