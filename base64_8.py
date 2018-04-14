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
import base64

class Base64
    @staticmethod
    def to_png(string, filename)
        png_recovered = base64.decodestring(string.encode('ascii'))  # decode string to pure picture
        f = open(str(cnt)+".png", "wb")
        f.write(png_recovered)
        f.close()
