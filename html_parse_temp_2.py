#! python3
# -*- coding: utf-8 -*-
# http://python.su/forum/topic/15531/?page=1#post-93316
import sys
sys.path.append("../..")
sys.path.append("..\..")
sys.path.append(".")
sys.path.append("..")
sys.path.append("./term")
sys.path.append(r".\term")
sys.path.append("./scripts/from_metropolis_work_mine")
sys.path.append(r".\scripts\from_metropolis_work_mine")
from commands8 import *
from solvounloader import State, \
    Click, Timer_wait_locate, \
    get_img_name, move, locate_by_shards, \
    locate, wait_locate, hotkey, sleep, \
    message, Scroll

db = Json.load("films.json")
#print(db)

import pyautogui
import copypaste

command = "command"
c = "c"
v = "v"
mouse_duration = 0.5


def tab():
    pyautogui.hotkey('tab')
    time.sleep(0.1)

def paste(text=None, notab=True):
    if text:
        time.sleep(0.1)
        copypaste.copy(text)
    time.sleep(0.1)
    pyautogui.hotkey("command", "v")
    time.sleep(0.1)
    if not notab: tab()

def enter():
    time.sleep(0.1)
    pyautogui.hotkey("enter")
    time.sleep(0.1)

def nl():
    def left():
        time.sleep(0.1)
        pyautogui.hotkey("left")

    for bl in Int.from_to(1,7):
        left()

    time.sleep(0.1)
    pyautogui.hotkey("down")


def copy():
    time.sleep(0.1)
    pyautogui.hotkey(command, c)
    time.sleep(0.1)

def mouse_to(x, y):
    time.sleep(0.1)
    pyautogui.moveTo(x, y, duration=mouse_duration)
    time.sleep(0.1)

def click():
    time.sleep(0.1)
    pyautogui.click(button="left")
    time.sleep(0.1)

Time.timer(5)
macOS.notification("html_parse_temp_2", "start")



for film in Int.from_to(1,20):
    pass
    copy()
    if copypaste.paste() == newline:
        hotkey("down")
        time.sleep(1)
        continue
    mouse_to(417, 131)
    click()
    mouse_to(464, 335)
    click()
    paste()
    enter()
    Time.timer(10)
    mouse_to(345, 681)
    click()
    time.sleep(3)
    mouse_to(1006, 725)
    click()
    pyautogui.mouseDown()
    mouse_to(287, 709)
    pyautogui.mouseUp()
    hotkey("escape")
    hotkey("down")
    for i in Int.from_to(1,8):
        hotkey("left")
    for i in Int.from_to(1,7):
        hotkey("right")
