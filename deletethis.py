#! python3
# -*- coding: utf-8 -*-
# mine commands
import sys
sys.path.append("../..")
sys.path.append("..\..")
sys.path.append(".")
sys.path.append("..")
sys.path.append("./term")
sys.path.append(r".\term")
from commands8 import *
#import os
#print (os.path.abspath(os.path.dirname(__file__)))
#print (os.getcwd())
#os.chdir("..")
#print (os.path.abspath(os.path.dirname(__file__)))
#print (os.getcwd())
#Print.debug(__file__)

__json__ = Path.extend(Path.current(), "speedtest_2.json")


sjson = Json.load(__json__, quiet=True)
lcnt = {}
for name in ["noimport", "stock"]:
    cnt = 0
    for item in sjson[name]:
        cnt+=item

    cnt = cnt / len(sjson[name])
    lcnt[name] = cnt
    print(name, cnt)
print(lcnt)
print(lcnt["noimport"]-lcnt["stock"])
