import os
from utils import *
__logfile__ = path_extend(currentfolder(), "wifi." + dottedtime() + ".log")
cnt = 0
while cnt < 256:
 cnt += 1
 if not ping("172.16.10." + str(cnt), count = 2):
  plog(__logfile__, "172.16.10." + str(cnt) + " is down :(")