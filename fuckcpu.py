from commands import *


def fucker():
    while True:
        pass


t = Threading(verbose = True)

for i in range(100):
    t.add(fucker)

t.start(wait_for_keyboard_interrupt=True)
