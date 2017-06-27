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
#win_unicode_console.enable()
#colorama.init()
scriptsFolder = r"\\192.168.99.91\shares\scripts"
scriptsSubFolderName = "Series"
scriptsSubFolder = scriptsFolder + "\ "[:1] + scriptsSubFolderName  # "\\192.168.99.91\shares\scripts\SolvoUnload"
settingsJsonName = "settings.json"
settingsJsonFile = scriptsSubFolder + "\ "[:1] + settingsJsonName
notepadExec = "notepad"
# "\\192.168.99.91\shares\scripts\SolvoUnload\settings.json"
dir_create(scriptsFolder)
dir_create(scriptsSubFolder)
file_create(settingsJsonFile)
jsonStringInMemory = loadjson(settingsJsonFile, quiet=True)
savejson(settingsJsonFile, jsonStringInMemory, quiet=True)
file_backup(settingsJsonFile, quiet=True)


debugprint = 0
if debugprint == True:
    print("settingsJsonFile:")
    print(settingsJsonFile)
    print("jsonStringInMemory:")
    print(jsonStringInMemory)

if __name__ == '__main__':
    def main():
        #конец позапрошлой смены
        for serial in jsonStringInMemory:
            print (serial, jsonStringInMemory[serial])
        print("[a] - Добавить сериал")
        print("[d] - Debug")
        print("[e] - Exit")
        print ("Надо бы писать своё меню, а то так неудобно редактировать этот список, ыхых")
        inputMenuItem = input("Введите что-нибудь: ")
        if ("а" in inputMenuItem) or ("a" in inputMenuItem):
            doNothing()
            newItem = input("Введи новый сериал: ")
            newItemValue = input("Введи значение: ")
            jsonStringInMemory[newItem] = newItemValue
            savejson(settingsJsonFile, jsonStringInMemory)
        elif "b" in inputMenuItem:
            last_batch = input("Новое последнее время отгруженных непривязанных накладных: ")
            jsonStringInMemory["last_batch"] = last_batch + jsonStringInMemory["last_batch"][len(last_batch):] # todo важная строка
            savejson(settingsJsonFile, jsonStringInMemory)
        elif "d" in inputMenuItem:
            subprocess.call([notepadExec, settingsJsonFile])
        elif "e" in inputMenuItem:
            sys.exit()
        else:
            try:
                inputMenuItem = int(inputMenuItem)
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
    while True:
        main()
    # todo open bartender



