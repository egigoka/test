#! python3
# -*- coding: utf-8 -*-
import subprocess
#import win_unicode_console
#win_unicode_console.enable()
pi = subprocess.check_output("ping ya.ru -n 1", shell=True)
pistr = pi.decode("cp866")
print (pistr)
#print(pistr.find("/n"))
# todo разбить на строки нормально
p = subprocess.check_output("mode con", shell=True)
pstr = p.decode("cp866")
print (pstr)
cnt = 0
for symbol in pstr:
    print (cnt, symbol)
    cnt += 1
print("fuck")
print(pstr[1])
