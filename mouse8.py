#! python3
# -*- coding: utf-8 -*-
# http://python.su/forum/topic/15531/?page=1#post-93316
from time8 import Time
try:
    import pyautogui
except:
    print("trying to install pyautogui")
    from installreq8 import pyautogui
__version__ = "0.0.8"

class Settings_Mouse:
    mouse_move_duration = 0.5
    sleep_before_click = 0.1

class Mouse:

    class Scroll:  # doesnt work good at new windows
        def scroll(value, up):
            value = int(value)
            if not up:
                value = 0-value
            pyautogui.vscroll(clicks=value)
            print("scrolled", value)

        @classmethod
        def up(cls, value=100):
            cls.scroll(value, up=True)

        @classmethod
        def down(cls, value=100):
            cls.scroll(value, up=False)

    class Click:
        @staticmethod
        def click(button, position, quiet=False):
            Time.sleep(Settings_Mouse.sleep_before_click)
            if position:
                pyautogui.click(x=position[0],y=position[1],button=button)
            else:
                pyautogui.click(button=button)
            if not quiet:
                print("click mouse " + button)

        @classmethod
        def right(cls,position=None, quiet=False):
            cls.click(button='right',position=position, quiet=quiet)

        @classmethod
        def left(cls,position=None, quiet=False):
            cls.click(button='left',position=position, quiet=quiet)

    @staticmethod
    def move(x, y=None, x2=None, y2=None, duration=Settings_Mouse.mouse_move_duration, tween=pyautogui.easeInOutQuad, rel=False, quiet=False):
        if isinstance(x, tuple):
            if len(x) == 2:
                y = x[1]
                x = x[0]
            elif len(x) == 4:
                y = x[1]
                x2 = x[2]
                y2 = x[3]
                x = x[0]
        if x2 and y2:
            x,y = pyautogui.center((x,y,x2,y2))
        if not quiet:
            if rel:
                how = "relative"
            else:
                how = "to"
            print("moved mouse", how, x, y)

        if rel:
            pyautogui.moveRel(x, y, duration=duration, tween=tween)
        else:
            pyautogui.moveTo(x, y, duration=duration, tween=tween)
