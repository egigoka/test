#! python3
# -*- coding: utf-8 -*-

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
import win32api
import time

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128

while True:
    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)

    if a != state_left:  # Button state changed
        state_left = a
        # print(a)
        if a < 0:
            print('Left Button Pressed')
        else:
            print('Left Button Released')

    if b != state_right:  # Button state changed
        state_right = b
        # print(b)
        if b < 0:
            print('Right Button Pressed')
        else:
            print('Right Button Released')
    time.sleep(0.001)
