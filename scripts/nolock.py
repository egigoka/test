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
from mouse8 import Mouse, Settings_Mouse
from random8 import Random
from time8 import Time

Settings_Mouse.set_mouse_move_duration(0.1)

while True:
    Mouse.move(Random.integer(-2,2), Random.integer(-2,2), rel=True, quiet=True)
    Time.sleep(Random.integer(60,180), quiet=True)
