#! python3
# -*- coding: utf-8 -*-

from commands7 import *
from copypaste import *

class Cnt:
    cnt = 46100
    @classmethod
    def deinc(cls, integeri):
        integer = int(integeri)
        cls.cnt += -integer
    @classmethod
    def copy(cls):
        copy(r" " + backslash + str(cls.cnt))
        
while True:
    integer = input_int()
    Cnt.deinc(integer)
    Cnt.copy()