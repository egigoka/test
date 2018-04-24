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

filename = "gigabytefile.txt"

def write(len):
    File.write(filename, Random.string(len))

for i in Int.from_to(1,1024-245):
    Print.rewrite(i)
    write(1024*1024)