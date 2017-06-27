#! python3
# -*- coding: utf-8 -*-

from copypaste import copy, paste
from utils import *

#! python3
# -*- coding: utf-8 -*-
from utils import *

list_ = []

file = open("new 3.txt", encoding='utf-8')
for line in file:
    line = line.rstrip(newline)
    list_ += [line]
# print(list)
# print(len(list))

import win32api
import time

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128

count = 1

while True:
    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)
    if b != state_right:  # Button state changed
        state_right = b
        if b < 0:
            if count == 3:
                count = 1
                peremesh = list_.pop(0)
                copy(peremesh)
                print(peremesh)
            else:
                count +=1
    if a != state_left:  # Button state changed
        state_left = a
        if a < 0:
            count = 1

    time.sleep(0.001)
