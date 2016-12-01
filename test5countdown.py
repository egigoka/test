#! python3
import test
import time
from datetime import datetime, date

test.printNoBr("Input countdown (in secs):")
timer=input()
try:
    timer=int(timer)
except ValueError as err:
    test.printNoBr("Ошибка! ")
    print(err)
cnt=timer
test.printNoBr(cnt)
test.printNoSep(" seconds left")
while cnt:
    time.sleep(1)
    cnt -= 1
    test.printNoBr(cnt)
    test.printNoSep(" seconds left")
test.printNoBr("Timer ends! ")
test.printNoBr(timer)
test.printNoSep(" seconds gone!")
print(datetime.now())