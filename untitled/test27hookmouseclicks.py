#! python3
# -*- coding: utf-8 -*-

__version__ = "2.0.0"
# totally redesigned
__version__ = "2.0.1"
# bugfix agrument parsing
__version__ = "2.1.0"
# added countdown
__version__ = "2.1.1"
# some improvement in countdown

# import pyHook
# import pythoncom
#
# def onclick(event):
    # print(event.Position)
    # print("Yay!")
    # return True
#
# hm = pyHook.HookManager()
# hm.SubscribeMouseAllButtonsDown(onclick)
# hm.HookMouse()
# pythoncom.PumpMessages()
# hm.UnhookMouse()

# Code to check if left or right mouse buttons were pressed
from commands7 import *

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
# state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128

# while True:
#     a = win32api.GetKeyState(0x01)
#     b = win32api.GetKeyState(0x02)
#
#     if a != state_left:  # Button state changed
#         state_left = a
#         print(a)
        # if a < 0:
        #     print('Left Button Pressed')
        # else:
        #     print('Left Button Released')
    #
    # if b != state_right:  # Button state changed
    #     state_right = b
    #     print(b)
        # if b < 0:
        #     print('Right Button Pressed')
        # else:
        #     print('Right Button Released')
    # time.sleep(0.001)


class State:
    try:
        time_warn = float(sys.argv[1])
    except IndexError:
        time_warn = False


class Timer:
    # init
    time_after_last_click = 0.0

    # settings
    check_every = 0.1  # seconds
    time_warn = 400.0  # seconds
    if State.time_warn:  # check for arguments
        time_warn = State.time_warn

    # methods of config
    @staticmethod
    def what_to_do():  # after timer gone
        Tkinter.warn()

    # methods for support
    @classmethod
    def increase(cls, count=check_every):
        time.sleep(count)
        cls.time_after_last_click += count
    @classmethod
    def reset(cls):
        cls.time_after_last_click = 0.0
    @classmethod
    def check_countdown(cls):
        if cls.time_after_last_click > cls.time_warn:
            cls.reset()
            cls.what_to_do()


class RealButton:
    state_left = win32api.GetKeyState(0x01)
    @classmethod
    def check_left_button_release(cls):
        left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
        if left != cls.state_left:  # Button state changed
            cls.state_left = left
            if left >= 0:
                Timer.reset()


while True:
    try:
        RealButton.check_left_button_release()
        Timer.increase()
        Timer.check_countdown()
    except KeyboardInterrupt:
        print("OK!")
        sys.exit(0)

    if str("%.1f" % Timer.time_after_last_click)[-1:] == "0":
        print("%.0f" % (Timer.time_warn - Timer.time_after_last_click))
    # if str("%.1f" % Timer.time_after_last_click)[-1:] == "5":
    #     print("%.1f" % (Timer.time_warn - Timer.time_after_last_click))