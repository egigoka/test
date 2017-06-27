#! python3
# -*- coding: utf-8 -*-
import sys
import os
import win_unicode_console
import subprocess
import time
import colorama
from utils import *

# init
# win_unicode_console.enable()
# colorama.init()
scriptsFolder = r"\\192.168.99.91\shares\scripts"
scriptsSubFolderName = "SolvoUnload"
scriptsSubFolder = scriptsFolder + "\ "[:1] + scriptsSubFolderName  # "\\192.168.99.91\shares\scripts\SolvoUnload"
settingsJsonName = "settings.json"
settingsJsonFile = scriptsSubFolder + "\ "[:1] + settingsJsonName
# "\\192.168.99.91\shares\scripts\SolvoUnload\settings.json"
dir_create(scriptsFolder)
dir_create(scriptsSubFolder)
file_create(settingsJsonFile)
if __name__ == '__main__':
    jsonStringInMemory = loadjson(settingsJsonFile)
    savejson(settingsJsonFile, jsonStringInMemory)
file_backup(settingsJsonFile, quiet = True)


def get_safe_time():  # конец позапрошлой смены
    gettime = datetime.datetime.now()
    dateandtime = str(gettime.day - 1).zfill(2) + "." + str(gettime.month).zfill(2) + "." + str(gettime.year) + " 03:00"
    return dateandtime


def get_current_time():  # текущее время
    get_time = datetime.datetime.now()
    date_and_time = str(get_time.day).zfill(2) + "." + str(get_time.month).zfill(2) + "." + str(get_time.year) + " " + \
        str(get_time.hour).zfill(2) + ":" + str(get_time.minute).zfill(2) + "." + str(get_time.second).zfill(2)
    return date_and_time

isDebug = 0
if isDebug == True:
    print("settingsJsonFile:")
    print(settingsJsonFile)
    print("jsonStringInMemory:")
    print(jsonStringInMemory)

# todo del
# try:
#     jsonStringInMemory["note"]
# except:
#     jsonStringInMemory["note"] = ""



def main():
    # print("Введите кол-во накладных или выберите пункт меню:")
    # конец позапрошлой смены
    cls()
    print("      Безопасное время                                    -", get_safe_time(), newline)
    print("[l] - Последнее время подтверждённых листов отбора        -", jsonStringInMemory["last_lo"])
    print("[b] - Последнее время отгруженных рейсов                  -", jsonStringInMemory["last_batch"])
    print("[o] - Последнее время отгруженных непривязанных накладных -", jsonStringInMemory["last_onebyone"])
    #print("[s] - Скорость отгрузки накладных                         -", jsonStringInMemory["nakl_per_sec"], newline)
    print()
    print("[k] - Последнее время запуска каналов отбора              -", jsonStringInMemory["kan_otb_time"], "("+jsonStringInMemory["kan_otb_last"]+")", newline)
    print("[n] - Note", "("+jsonStringInMemory["note"]+")")
    #print("[d] - Debug")
    print("[e] - Exit", newline)
    inputMenuItem = input("Введите что-нибудь: ")
    if "b" in inputMenuItem:
        last_batch = leftpad(input("Новое последнее время отгруженных непривязанных накладных: "), 2, 0)
        jsonStringInMemory["last_batch"] = last_batch + jsonStringInMemory["last_batch"][len(last_batch):]
        savejson(settingsJsonFile, jsonStringInMemory)
    elif "o" in inputMenuItem:
        last_onebyone = leftpad(input("Новое последнее время отгруженных непривязанных накладных: "), 2, 0)
        jsonStringInMemory["last_onebyone"] = last_onebyone + jsonStringInMemory["last_onebyone"][len(last_onebyone):]
        savejson(settingsJsonFile, jsonStringInMemory)
        cnt = 0
    elif "s" in inputMenuItem:
        try:
            jsonStringInMemory["nakl_per_sec"] = float(input("Новая скорость отгрузки накладных: "))
            savejson(settingsJsonFile, jsonStringInMemory)
        except ValueError:
            print("Это не число")
    elif "l" in inputMenuItem:
        last_lo = leftpad(input("Новое последнее время подтверждённых листов отбора: "), 2, 0)
        jsonStringInMemory["last_lo"] = last_lo + jsonStringInMemory["last_lo"][len(last_lo):]
        savejson(settingsJsonFile, jsonStringInMemory)
    elif "d" in inputMenuItem:
        subprocess.call([notepadExec, settingsJsonFile])
    elif "e" in inputMenuItem:
        sys.exit()
    elif "k" in inputMenuItem:
        jsonStringInMemory["kan_otb_time"] = get_current_time()
        komment_kan_otb = input("Коммент: ")
        jsonStringInMemory["kan_otb_last"] = komment_kan_otb
        savejson(settingsJsonFile, jsonStringInMemory)
    elif "n" in inputMenuItem:
        jsonStringInMemory["note"] = input("Заметка: ")
        savejson(settingsJsonFile, jsonStringInMemory)
    else:
        try:
            inputMenuItem = int(inputMenuItem)
            if inputMenuItem >= 200:
                inputMenuItem /= 0.7
            inputMenuItem -= 15
            inputMenuItem = float(inputMenuItem)
            count = 15 + (inputMenuItem / 15 * 10)
            count = count / jsonStringInMemory["nakl_per_sec"]
            count = int(count)
            countstart = count
            try:
                while count > 0:
                    mins = str(int(count/60))
                    secs = str(int(count%60))
                    if countstart >= 60:
                        print(mins + "m" + secs.zfill(2) + "s")
                    elif countstart >= 10:
                        print(secs.zfill(2) + "s")
                    else:
                        print(secs + "s")
                    time.sleep(1)
                    count += -1
                screenblink()
            except KeyboardInterrupt as err:
                print("OK")
        except ValueError as err:
            print(err)
            print("Вообще ничего не понял, давай сначала")
        except NameError as err:
            print (err)
if __name__ == '__main__':
    while True:
        main()