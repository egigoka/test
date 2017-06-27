#! python3
from utils import getIntegers, plog
logfile = r"\\192.168.99.91\shares\scripts\BartenderPrint\testlog_.log"

file = open(logfile, "r")
cnt = 0
for line in file:
    cnt += getIntegers(line)[6]
print(cnt)
plog(logfile, "Итого за февраль напечатано" + str(cnt) + "термочеков для групп, что составляет"
     + str(int(cnt/300)) + "роликов или " + str(cnt/300/60) + "коробок")
plog(logfile, "рассчёты произведены без учёта термочеков для грузчиков или другого использования, такого как наклейки для овощей или фруктов")