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
from commands8 import *


__json__ = Path.extend(Path.current(), "speedtest_2.json")

Bench_all = get_Bench()
Bench = get_Bench()

sjson = {"noimport":[], "stock":[]}
Json.save(__json__, sjson, quiet=True)

Bench_all.start()

while len(sjson["noimport"]) < 100:
    print(len(sjson["noimport"]))
    json = Json.load(__json__, quiet=True)


    Bench.start()
    Process.start("python3", "commands8.py")
    sjson["stock"].append(Bench.end())


    Bench.start()
    Process.start("python3", "commands8_internal_import_test.py")
    sjson["noimport"].append(Bench.end())



    Json.save(__json__,sjson, quiet=True)
Bench_all.prefix = "100 runs in:"
Bench_all.end()
