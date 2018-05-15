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
from mouse8 import Mouse
from random8 import Random
from time8 import Time

while True:
    Mouse.move(Random.integer(-100,100), Random.integer(-100,100)., rel=True, quiet=True)
    Time.sleep(Random.integer(60,180), quiet=True)
