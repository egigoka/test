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
from commands7 import *
import os
print (os.path.abspath(os.path.dirname(__file__)))
print (os.getcwd())
os.chdir("..")
print (os.path.abspath(os.path.dirname(__file__)))
print (os.getcwd())

Print.debug(__file__)
