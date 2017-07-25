import os
from utils import *
__logfile__ = path_extend(currentfolder(), "wifi." + dottedtime() + ".log")

networks = ["10","11"]

for network in networks:
    cnt = 0
    while cnt < 255:
     cnt += 1
     if not ping("172.16."+network+"." + str(cnt), count = 2):
      plog(__logfile__, "172.16.10." + str(cnt) + " is down :(")