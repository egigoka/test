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
from winreg import *  # https://docs.python.org/3.6/library/winreg.html
Registry = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
RawKey = OpenKey(Registry, "SYSTEM\CurrentControlSet\Services")


list = []
dict = {}

cnt = 0
try:
    while True:
        #print(EnumKey(RawKey,cnt))
        cnt_ = 0

        TempKey = OpenKey(Registry, "SYSTEM\CurrentControlSet\Services" + backslash + EnumKey(RawKey,cnt))
        while True:
            try:
                #print("   ", EnumValue(TempKey,cnt_)[0])
                if EnumValue(TempKey,cnt_)[0] not in list:
                    list.append(EnumValue(TempKey,cnt_)[0])
                    dict[EnumValue(TempKey,cnt_)[0]] = EnumKey(RawKey,cnt)
                cnt_ +=1
            except OSError:
                break
        cnt += 1
except OSError:
    pass
#print(list)
#print(dict)
for k in sorted(dict.keys()):  # yep, i copied that and dont understand that code :(
    #print (k, ':', dict[k])
    print(k + " (first found at '"+dict[k]+"')")
#for key, value in Dict.iterable(dict): print(key + " (first found at '"+value+"')")
