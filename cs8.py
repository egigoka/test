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

#some shitty functions that i wrote million time in other shitty scripts

def dirify(object):
    for subobj in dir(object):
        if "__" not in subobj:
            print(subobj)

def sleep(time):
    if time >= 1:
        Time.timer(time)
    else:
        print("sleeping", time)
        time.sleep(time)
