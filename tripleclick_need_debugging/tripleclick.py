#! python3
# -*- coding: utf-8 -*-

from commands7 import *
from copypaste import copy, paste

# __version__ = "2.0.0"
# totally redesigned
# __version__ = "2.0.1"
# bugfix agrument parsing
# __version__ = "2.1.0"
# added countdown
__version__ = "2.1.1"
# some improvement in countdown
__version__ = "2.2.0"
# some new functionality
__version__ = "2.2.1"
# warning on non-windows system

# import pyHook
# import pythoncom
#
# def onclick(event):
#      print(event.Position)
#      print("Yay!")
#      return True
#
# hm = pyHook.HookManager()
# hm.SubscribeMouseAllButtonsDown(onclick)
# hm.HookMouse()
# pythoncom.PumpMessages()
# hm.UnhookMouse()

# Code to check if left or right mouse buttons were pressed


# state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
# state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128

# while True:
#     a = win32api.GetKeyState(0x01)
#     b = win32api.GetKeyState(0x02)
#
#     if a != state_left:  # Button state changed
#         state_left = a
#         print(a)
#         if a < 0:
#             print('Left Button Pressed')
#         else:
#             print('Left Button Released')
#
#     if b != state_right:  # Button state changed
#         state_right = b
#         print(b)
#         if b < 0:
#             print('Right Button Pressed')
#         else:
#             print('Right Button Released')
#     time.sleep(0.001)


class State:
    #try:
    #    time_warn = float(sys.argv[1])
    #except IndexError:
    #    time_warn = False
    time_warn = 400.0
    timeout = 1


class ShittyTime:
    Ben = get_Bench()

    @classmethod
    def start(cls):
        cls.Ben.start()

    @classmethod
    def end(cls):
        if cls.first_time:
            cls.second_time = cls.first_time
        cls.first_time = cls.Ben.end(quiet=True)

    @classmethod
    def reset(cls):
        cls.first_time = None
        cls.second_time = None

    @classmethod
    def notimeout(cls):
        summary = cls.first_time + cls.second_time
        # print("first_time " + str(cls.first_time) +
        #       ", second_time " + str(cls.second_time) +
        #       ", summary ", summary)
        if cls.first_time and cls.second_time:
            if summary <= State.timeout:
                cls.reset()
                return True
            else:
                return False
ShittyTime.reset()


class Counter:
    increase_by = 1
    cnt = 0
    trigger = increase_by * 3

    @classmethod
    def reset(cls):
        cls.cnt = 0

    @classmethod
    def increase(cls, n=increase_by):
        ShittyTime.end()
        ShittyTime.start()
        cls.cnt += n

    @classmethod
    def check(cls):
        if cls.cnt >= cls.trigger:
            return True
        else:
            return False


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


class legacy_RealButton:
    state_left = win32api.GetKeyState(0x01)
    state_right = win32api.GetKeyState(0x02)

    @classmethod
    def check_left_button_release(cls):
        left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
        if left != cls.state_left:  # Button state changed
            cls.state_left = left
            if left >= 0:
                return True
            else:
                return False

    @classmethod
    def check_right_button_release(cls):
        right = win32api.GetKeyState(0x02)  # Left button down = 0 or 1. Button up = -127 or -128
        if right != cls.state_right:  # Button state changed
            cls.state_right = right
            if right >= 0:
                while win32api.GetKeyState(0x02) >= 0:
                    print("left button pressed?!")
                return True
            else:
                return False


class RealButton:

    
    @staticmethod
    def human_to_winapi_button_name(button):
        buttons = {"left":0x01, "right":0x02}
        return buttons[button]
      
    @classmethod
    def winapi_button_state(cls, button):
        return win32api.GetKeyState(cls.human_to_winapi_button_name(button))
        
    @classmethod
    def pressed(cls, button):
        state = cls.winapi_button_state(button)
        if state in [0, 1]:
            return False
        elif state in [-127, -128]:
            return True
        
    
    


def reset():
    Counter.reset()
    ShittyTime.reset()


def main():
    print("tripleclick work okay")
    print("define a function in your code and shadow main function in tripleclick")
    print("like this:")
    print("import tripleclick")
    print("def some_function()")
    print("    pass  # do what you want")
    print("tripleclick.main = some_function")

def start():
    while True:  # крутить до остановки
        print (RealButton.pressed("right"))
        print (RealButton.pressed("left"))
        # print(win32api.GetKeyState(0x02))
        #try:# обработка остановки программы
        #    time.sleep(0.01)  # небольшая задержка
        #    if RealButton.check_right_button_release():  # if button pressed
        #        Counter.increase()  # increase counter
        #        Print.debug("Counter.cnt increased", Counter.cnt)
        #        if Counter.check():  # if counter triggered
        #            if ShittyTime.notimeout():  # if timeout not reached
        #                main()  # run main function
        #                reset()  # reset classes
        #    if RealButton.check_left_button_release():
        #        reset()
        #except KeyboardInterrupt:
        #    print("OK!")
        #    sys.exit(0)

    # if str("%.1f" % Timer.time_after_last_click)[-1:] == "0":
    #     print("%.0f" % (Timer.time_warn - Timer.time_after_last_click))
    # if str("%.1f" % Timer.time_after_last_click)[-1:] == "5":
    #     print("%.1f" % (Timer.time_warn - Timer.time_after_last_click))
