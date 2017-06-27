#! python3
# -*- coding: utf-8 -*-

from utils import *

series = [
         "10. Звездный путь / Star Trek - 1966 год",
         "9. Лексс / Lexx - 1997 года",
         "8. Звёздные врата / Stargate - 1997 год",
         "7. Звездный крейсер Галактика / Battlestar Galactica - 2004 год",
         "6. Далеко во Вселенной / Farscape - 1999 год",
         "5. Halo: Сумерки / Halo: Nightfall - 2014 год",
         "4. Тёмные дела / Dark Matter - 2015 год",
         "3. Киллджойс / Killjoys - 2015 год",
         "2. Светлячок / Firefly - 2002 год",
         "1. Пространство / The Expanse - 2015 год"
         ]

for serial in series:
    current_serial = substring(serial, ". ", r" / ")
    year = getIntegers(serial)[1]
    print(current_serial, "сериал", year,  "года")