#! python3
# -*- coding: utf-8 -*-
from commands8 import *

B = get_Bench()
B.start()
import pkgutil

modules = []
for item in pkgutil.iter_modules():
    #print(item[1])
    modules.append(item[1])

B.end()

print(modules)
print("paramiko" in modules)
