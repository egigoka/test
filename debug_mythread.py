import time
from commands import *
import commands

print(commands.__version__)
print(commands.threading9.__version__)

def a():
    while True:
        print("mythread")
        time.sleep(10)

t = MyThread(a, quiet=False)

t.start()

time.sleep(4)

t.kill()
