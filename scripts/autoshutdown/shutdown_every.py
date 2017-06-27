#! python3
# -*- coding: utf-8 -*-
__version__ = "1.1.0"
# 1.1.0 add countdown


import os
import time
from sys import argv
from utils import file_backup, loadjson, savejson, backslash, newline, in_quotes

# ---------------------------------- JSON workaround ----------------------------------
json_on_disk = "settings.json"


def reloadJSON():
    global json_in_memory
    json_in_memory = loadjson(json_on_disk, quiet=True)
try:
    reloadJSON()
except FileNotFoundError:
    json_in_memory = {}

def saveJSON():
    savejson(json_on_disk, json_in_memory, quiet=True)
saveJSON()
# ---------------------------------- JSON workaround ----------------------------------


def countdown(secs):
    while cnt > 0:
        print("shutdown", not reboot and not hilbernate,
              newline + "reboot", reboot,
              newline + "hilbernate", hilbernate,
              newline + "after", secs, "secs")
        time.sleep(1)
        cnt += -1


def shutdown_after(mins, reboot=False, hilbernate=False):
    try:
        countdown.sleep(mins*60)
        if hilbernate:
            global hilbernated
            hilbernated = True
            os.system(r"shutdown /h")
        elif reboot:
            os.system(r"shutdown /r /t 0")
        else:
            os.system(r"shutdown /t 0")
    except KeyboardInterrupt:
        print("Cancelled")


def gettime():
    try:
        time_ = input("Через сколько минут ввести в сон компьютер? ")
        if time_ == "":
            time_ = input("Через сколько часов ввести в сон компьютер? ")
            time_ = int(time) * 60
    except:
        pass
    try:
        time_
    except:
        time_ = ""
    return time_

def hilbernate():
    time_ = gettime()
    if time != "":
        shutdown_after(time_, hilbernate=True)

hilbernated = False

if json_in_memory["hilbernate_manual"]:
    while hilbernated == False:
        hilbernate()
elif json_in_memory["auto_reboot"]:
    command = "copy " + in_quotes(argv[0]) + " " + in_quotes("%appdata%\Microsoft\Windows\Start Menu\Programs\Startup")
	command = "copy " + "utils.py" + " " + in_quotes("%appdata%\Microsoft\Windows\Start Menu\Programs\Startup")
    os.system(command)
    print(command)
    shutdown_after(json_in_memory["auto_reboot_every"], reboot=True)
