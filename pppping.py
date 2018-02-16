from commands7 import *
for ip in [21,20,30,38,42,43,44]:
    ping("172.16.10."+str(ip), count=4)
