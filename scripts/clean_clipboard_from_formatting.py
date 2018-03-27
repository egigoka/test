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
    if oldinputstr != inputstr:
        print (repr(inputstr), newline)
        oldinputstr = inputstr
    #Print.debug("inputstr", inputstr, "type(inputstr)", type(inputstr), "repr(inputstr)", repr(inputstr))
    #print(repr(inputstr))
    inputstr = str(inputstr)
    inputstr = inputstr.replace(newline2, "")
    inputstr = inputstr.replace(newline, "")
    inputstr = inputstr.replace("\t", "")
    outputstr = inputstr
    #for symbol in inputstr:
    #    if (symbol == newline) or (symbol == newline2):
    #        continue
    #    try:
    #        Print.rewrite(symbol)
    #        copypaste.copy(symbol)
    #        outputstr += symbol
    #    except:
    #        pass
    
    #Print.debug("outputstr", outputstr, "repr(outputstr)", repr(outputstr))
    #print(repr(outputstr))
    copypaste.copy(outputstr)