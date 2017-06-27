#! python3
# -*- coding: utf-8 -*-
import sys
import os
# import win_unicode_console
from utils import *
from current_paths import *
import barsprint_nogui_codegen_latex

# init


__scriptname__ = "bartendernogui"


ifDebug = False
# win_unicode_console.enable()
scripts_sub_folder_name = "BarsPrint"
scripts_sub_folder = path_extend(scripts_dir, scripts_sub_folder_name) # S:\scripts\BarsPrint

LaTeX_file_name = "LaTeX_bars_codegened.tex"
LaTeX_file = path_extend(scripts_sub_folder, LaTeX_file_name)
# "S:\scripts\BarsPrint\LaTeX_bars_codegened.tex"

settingsJsonName = "settings.json"
settingsJsonFile = path_extend(scripts_sub_folder, settingsJsonName)
# "S:\scripts\BarsPrint\settings.json"

logfile_name = "bartender.log"
logfile = path_extend(scripts_sub_folder, logfile_name)
dir_create(scripts_sub_folder)
file_create(settingsJsonFile)
file_backup(settingsJsonFile, quiet = True)
if ifDebug is True:
    file_backup(path_extend(scripts_sub_folder, "barsprint_nogui.py"))
    print("settingsJsonFile:", end="")
    print(settingsJsonFile)
jsonStringInMemory = loadjson(settingsJsonFile, quiet = True)
savejson(settingsJsonFile, jsonStringInMemory, quiet = True)

# создаём группу фрукты
# jsonStringInMemory["group_fruit"] = {} # имя группы
# jsonStringInMemory["group_fruit"]["prefix"] = "FA" # префикс
# jsonStringInMemory["group_fruit"]["lastnum"] = 0 # последний номер
# savejson(settingsJsonFile, jsonStringInMemory)
# sys.exit()


def print_bars(cnt_bars, group_name, outoput_file=LaTeX_file):
    jsonStringInMemory = loadjson(settingsJsonFile)
    prefix = jsonStringInMemory[group_name]["prefix"]
    startCnt = jsonStringInMemory[group_name]["lastnum"]
    cnt = startCnt + 1
    endCnt = startCnt + cnt_bars
    jsonStringInMemory[group_name]["lastnum"] = endCnt
    savejson(settingsJsonFile, jsonStringInMemory)

    barsprint_nogui_codegen_latex.main(arg1, arg2, arg3)????
    # todo start gen LaTeX code from here

    plog(logfile, "Напечатано " + str(cnt_bars) + " бирок для " + group_name
         + " с " + str(prefix) + str(startCnt + 1) + " по " + str(prefix) + str(endCnt))




    # file = open(file_save_name, 'w')
    #
    #
    # while cnt <= endCnt:
    #     if len(str(cnt)) > 6:
    #         print("!Переполнение бирок для", group_name)
    #         print("Остановка скрипта...")
    #         sys.exit()
    #     file.write(str(prefix) + str(cnt).zfill(6) + '\n')
    #     if ifDebug is True:
    #         print(str(prefix) + str(cnt))
    #     cnt += 1
    # file.close()


def runBartender(database=outputFile, type="kompl", size="58*60"):
    database = None
    # todo разные файлы для разного количества символов
    # todo isprint check from json
    time.sleep(1)
    if type == "kompl" and size == "58*60":
        bartenderFile = bartenderMineDocument("Бирки 58x60")
        subprocess.call([bartenderExec, bartenderFile, "/P", "/X"])
    if type == "cell" and size == "58*60":
        bartenderFile = bartenderMineDocument("Бирки 58x60 9 симв")
        subprocess.call([bartenderExec, bartenderFile, "/P", "/X"])
    if type == "gruzch" and size == "58*60":
        bartenderFile = bartenderMineDocument("Бирки 58x60 грузчики")
        subprocess.call([bartenderExec, bartenderFile, "/P", "/X"])
    if type == "justtext" and size == "58*60":
        bartenderFile = bartenderMineDocument("Бирки 58x60 text py")
        subprocess.call([bartenderExec, bartenderFile, "/P", "/X"])
    if type == "justopen":
        subprocess.call([bartenderExec])


def main(arg1=None, arg2=None, arg3=None, arg4 = None):  # todo печать просто текста и повторяющегося текста
    # taskkill("bartend")
    if not arg1:
        print("Выберите группу:")
        print("[1] - 1 группа")
        print("[2] - 2 группа")
        print("[3] - 3 группа")
        print("[4] - 4 группа")
        print("[5] - 5 группа")
        print("[6] - Грузы")
        print("[7] - Форпост")
        print("[8] - Алкоголь")
        print("[9] - Фрукты")
        print("[10]- 10 группа")
        print("[g] - Грузчики логины")
        print("[t] - 1 ячейку")
        print("[mt]- Несколько ячеек")
        print("[jt]- Просто 4 строки на 58*60")
        print("[gp]- Грузчики логин (не сделано)")  # todo сделать
        print("[e] - Выход")
        print("[dk]- Debug kompl")
        print("[dc]- Debug cell")
        print("[djt]- Debug just text")
        print("[kill] - kill bartender processes")
        print("[l] ---- добавить в лог что-либо")
        print("[ol] --- открыть лог")
    if arg1:
        inputGroupAndCount = arg1
    else:
        inputGroupAndCount = input("Введите номер: ")
    groupName = False
    if "10" in inputGroupAndCount:
        groupName = "group10"
    elif "1" in inputGroupAndCount:
        groupName = "group1"
    elif "2" in inputGroupAndCount:
        groupName = "group2"
    elif "3" in inputGroupAndCount:
        groupName = "group3"
    elif "4" in inputGroupAndCount:
        groupName = "group4"
    elif "5" in inputGroupAndCount:
        groupName = "group5"
    elif "6" in inputGroupAndCount:
        groupName = "shipments"
    elif "7" in inputGroupAndCount:
        groupName = "group_forp"
    elif "8" in inputGroupAndCount:
        groupName = "group_alco"
    elif "9" in inputGroupAndCount:
        groupName = "group_fruit"
    elif "g" in inputGroupAndCount:
        if arg2:
            login = arg2
        else:
            login = input("Введи логин грузчика:")
        login = login.upper()
        login = login.strip(" ")
        if arg3:
            name = arg3
        else:
            name = input("Введи имя и фамилию грузчика:")
        name = name.title()
        name = name.strip(" ")
        cnt = "jabla"
        if arg4:
            cnt = int(arg4)
        else:
            while cnt == "jabla":
                try:
                    cnt = input("Введи количество:")
                    cnt = int(cnt)
                except ValueError:
                    cnt = "jabla"
        file = open(bartenderMineDocument("Бирки 58x60 грузчики") + ".txt", 'w')
        if login != "":
            plog(logfile, "Напечатано " + str(cnt) + " бирок для грузчика " + name + " (" + login + ")", quiet=True)
        while cnt >= 1:
            file.write(str(login) + "," + str(name) + "\n")
            cnt -= 1
        file.close()
        runBartender(type="gruzch")
    elif "mt" in inputGroupAndCount:
        file_wipe(outputFile)
        subprocess.call([notepadExec, outputFile])
        runBartender(type="cell")
    elif ("jt" in inputGroupAndCount) or ("ое" in inputGroupAndCount):
        text = input("Text:")
        cnt = int(input("Cnt of bars:"))
        file = open(outputFile, 'w')
        while cnt > 0:
            file.write(text + "\n")
            cnt -= 1
        file.close()
        runBartender(type="justtext")
    elif ("e" in inputGroupAndCount) or ("у" in inputGroupAndCount):
        sys.exit()
    elif "t" in inputGroupAndCount:
        text = input("Text:")
        file = open(outputFile, 'w')
        file.write(text)
        file.close()
        runBartender(type="cell")
    elif "runbartender" in inputGroupAndCount:
        runBartender(type="justopen")
    elif "dk" in inputGroupAndCount:
        bartenderFile = bartenderMineDocument("Бирки 58x60")
        barsCnt = int(input("Сколько нужно бирок каждой группы?"))
        groupNames = ["group1", "group2", "group3", "group4", "group5", "shipments", "group_forp", "group_alco",
                      "group10", "group_fruit"]
        if barsCnt != 0:
            for group in groupNames:
                print_bars(barsCnt, group)
                runBartender()
        subprocess.call([bartenderExec, bartenderFile])
        subprocess.call([notepadPlusPlusExec, settingsJsonFile])
        subprocess.call([notepadPlusPlusExec, outputFile])
    elif "dc" in inputGroupAndCount:
        bartenderFile = bartenderMineDocument("Бирки 58x60 9 симв")
        subprocess.call([bartenderExec, bartenderFile])
        subprocess.call([notepadPlusPlusExec, outputFile])
    elif "djt" in inputGroupAndCount:
        bartenderFile = bartenderMineDocument("Бирки 58x60 text py")
        subprocess.call([bartenderExec, bartenderFile])
        subprocess.call([notepadPlusPlusExec, outputFile])
    elif "kill" in inputGroupAndCount:
        print("Killing bartend*")
        os.system("taskkill /f /im bartend*")
    elif "ol" in inputGroupAndCount:
        openInNewWindow(notepadExec, logfile)
    elif "l" in inputGroupAndCount:
        string = input("Что занести в лог? ")
        plog(logfile, string)
    else:
        print("error")
        print(inputGroupAndCount)
    try:
        if groupName:
            if arg2:
                print_bars(int(arg2), groupName)
            else:
                print_bars(int(input("Сколько нужно бирок?")), groupName)
            runBartender()
    except ValueError as err:
        print(err)

try:
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
except IndexError:
    try:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    except IndexError:
        try:
            main(sys.argv[1], sys.argv[2])
        except IndexError:
            try:
                main(sys.argv[1])
            except IndexError:
                while True:
                    main()

    # todo different files for different line len
    # todo ean13