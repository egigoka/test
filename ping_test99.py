import os
from utils import *
__logfile__ = path_extend(currentfolder(), "wifi." + dottedtime() + ".log")
cnt = 0
while cnt < 255:
 cnt += 1
 if not ping("192.168.99." + str(cnt), count = 2):
  print("Clean!")
  #plog(__logfile__, "172.16.10." + str(cnt) + " is down :(")