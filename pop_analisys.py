import datetime
from commands import *

pp = Str.nl(File.read("poops-2025-11-14-0820.csv"))

ppp = {}

for p in pp[1:]:
    d = datetime.datetime.strptime(p[:10], "%Y-%m-%d")
    dd = d.isocalendar()
    k = str(d.year) + "-" + str(dd.week)
    try:
        ppp[k]
    except KeyError:
        ppp[k] = 0
    ppp[k] += 1
#    break

for k, v in ppp.items():
    print(k, v)


yy = {}

for k, v in ppp.items():
    y = k[:4]
    try:
        yy[y]
    except KeyError:
        yy[y] = {"weeks": 0, "pops": 0}
    yy[y]["weeks"] += 1
    yy[y]["pops"] += v

for key, value in yy.items():
    print(key, value)

for key, value in yy.items():

    pd = value["weeks"]/365
    wpy = pd*7
    

    pw = value["pops"]/wpy/365*7
    print(key, pw)
    





print("done")




