#! python3
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "..")
sys.path.insert(0, "../..")
sys.path.insert(0, "..\..")
from commands7 import *  # mine commands

for cnt in Int.from_to(1,100):
    time.sleep(0.1)
    print(cnt, end='\r')