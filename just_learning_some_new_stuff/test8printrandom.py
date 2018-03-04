#! python3
import os
import random
import sys

## Все переменные для старта


def initiate():
    global choices
    choices = []
    global choices2
    choices2 = []
    global cnt2
    cnt2=4
    global directory
    directory = 'D:\Облака\Box Sync\!Work\!Real walls'
    global directoryToPrint_name
    directoryToPrint_name = "toPrintPython"
    global directoryToPin_name
    directoryToPin_name = "toPinPython"
    global directoryPinned_name
    directoryPinned_name = "pinned"
    global directoryPinnedReal_name
    directoryPinnedReal_name = "pinnedReal"
    global directoryToPrint
    directoryToPrint = directory + "\ "[:-1] + directoryToPrint_name
    global directoryToPin
    directoryToPin = directory + "\ "[:-1] + directoryToPin_name
    global directoryPinned
    directoryPinned = directory + "\ "[:-1] + directoryPinned_name
    global directoryPinnedReal
    directoryPinnedReal = directory + "\ "[:-1] + directoryPinnedReal_name
initiate()

def chooseSomePic(): ## Выбор рандомной картинки
    global choices, choice
    global files
    choice = random.choice(files)
    choices.append(choice)
    files.remove(choice)

def gotPrintback_function(gotallback="select"): ## Очистка папки подготовки
    if gotallback == "y":
        exit
    else:
        gotallback = input("Вернуть всё на место? (y/n):")
    if gotallback == "y":
        listdirpythontoPrint=os.listdir(directoryToPrint)
        while listdirpythontoPrint:
            cmd = 'move "' + directoryToPrint + "\ "[:-1] + listdirpythontoPrint.pop() + '"' + ' "' + directory + '"'
            os.system(cmd)
    elif gotallback == "n":
        exit
    else:
        gotPrintback_function()

def gotPinback_function(gotallback="select"): ## Очистка папки подготовки
    if gotallback == "y":
        exit
    else:
        gotallback = input("Вернуть всё на место? (y/n):")
    if gotallback == "y":
        gotPrintback_function("y")
        listdirpythontoPin=os.listdir(directoryToPin)
        while listdirpythontoPin:
            cmd = 'move "' + directoryToPin + "\ "[:-1] + listdirpythontoPin.pop() + '"' + ' "' + directory + '"'
            os.system(cmd)
    elif gotallback == "n":
        exit
    else:
        gotPinback_function()

def loadFileList(): ## Загрузка списка фалов без папок
    global files
    files = os.listdir(directory) ## загрузка списков фалов, далее исключения
    toremove = ["never", directoryToPrint_name, directoryToPin_name, directoryPinned_name, directoryPinnedReal_name, ".nomedia"]
    for i in toremove:
        print (i)
        try:
            files.remove(i)
        except ValueError:
            continue

def createFolders(): ## создание папок
    tocreate = [directory, directoryToPrint, directoryToPin, directoryPinned, directoryPinnedReal]
    for i in tocreate:
        try:
            os.mkdir(i)
        except FileExistsError:
            continue

def cntPages_function(new="nope"): ## Количество страниц печати
    global cnt3
    if new == "new":
        cntPages = input("Введите количество новых листов:")
    else:
        cntPages = input("Введите количество листов (не забудь про vk):")
    try:
        if cntPages == 0:
            quit
        else:
            cntPages = int(cntPages)
            cnt3 = cntPages * cnt2
            if new == "new":
                moveToToPrint()
    except ValueError:
        print("Это не число")
        cntPages_function()

def moveToToPrint(): ## перемещение выбранных файлов в toPrintPython
    ## Выбор списка файлов для обработки
    i=1
    while i<=cnt3:
        chooseSomePic()
        i+=1
    ## Вывод списка файлов для обработки
    print()
    print("All choices:", choices)
    print()
    ## Само перемещение файлов
    choices2 = list(choices)
    while choices2:
        global choices
        cmd = 'move "' + directory + "\ "[:-1] + choices2.pop() + '"' + ' "' + directoryToPrint + '"'
        os.system(cmd)
    if choices2 == []:
        print("Пройдено по всем файлам, они перемещены (скорее всего) в", directoryToPrint)
        cmd = 'start "" "' + directoryToPrint + '"'
        #todo проверка на перемещение файлов (и не только здесь)

def questPrint(new="nope"): ## перемещение выбранных файлов в toPinPython (тип файлы распечатаны)
    if new == "new":
        os.system('start "" "' + directoryToPrint + '"')
        inputvar = input("Распечатал новые? (y/n)")
    else:
        os.system('start "" "' + directoryToPrint + '"')
        inputvar = input("Распечатал? (y/n)")
    global choices, choices2
    if inputvar == "y":
        choices2 = list(choices)
        while choices2:
            cmd = 'move "' + directoryToPrint + "\ "[:-1] + choices2.pop() + '"' + ' "' + directoryToPin + '"'
            os.system(cmd)
            #print(cmd)
        if new == "new":
            questPin_lv1("all")
        else:
            questPin_lv1()
    elif inputvar == "n":
        gotPrintback_function("y") ## очистка папки подготовки после прохода
    else:
        questPrint()


def questPin_lv1(all="nope"):
    if all == "all":
        os.system('start "" "' + directoryToPin + '"')
        inputvar = input("Все-все прицепил? (y/n)")
    else:
        os.system('start "" "' + directoryToPin + '"')
        inputvar = input("Прицепил? (y/n)")
    if inputvar == "y":
        questPin_lv2()
    elif inputvar == "n":
        while True:
            inputvar2 = input("А хотя бы распечатал? (y/n)")
            if inputvar2 == "n":
               gotPinback_function("y")
            else:
                initiate()
                cntPages_function("new")
                if cnt3 == 0:
                    quit
                else:
                    questPrint("new")
    else:
        questPin_lv2()

def questPin_lv2(): ## перемещение выбранных файлов в toPinPython (тип файлы распечатаны)
    inputvar = input("Точно прицепил? (это действие не отменить) (y/n/real)")
    global choices, choices2
    if inputvar == "y":
        choices2 = os.listdir(directoryToPin)
        while choices2:
            cmd = 'move "' + directoryToPin + "\ "[:-1] + choices2.pop() + '"' + ' "' + directoryPinned + '"'
            os.system(cmd)
            os.system('start "" "' + directoryPinned + '"')
            #print(cmd)
    elif inputvar == "real":
        choices2 = os.listdir(directoryToPin)
        while choices2:
            cmd = 'move "' + directoryToPin + "\ "[:-1] + choices2.pop() + '"' + ' "' + directoryPinnedReal + '"'
            os.system(cmd)
            os.system('start "" "' + directoryPinnedReal + '"')
            #print(cmd)
    elif inputvar == "n":
        gotPinback_function("select") ## очистка папки подготовки после прохода
    else:
        questPin_lv2()

loadFileList()

## Очистка экрана
os.system("cls")

## Вывод списка всех файлов
#print("Files:")
#print(files)
#print()

## Проверка на существование и создание недостающих папок
createFolders()

## Очистка папки подготовки перед стартом
gotPrintback_function("y")

## todo проверка папки toPinPython на отсутствие файлов
test = os.listdir(directoryToPin)
if test:
    questPin_lv1()

## Количество страниц печати
cntPages_function()

if cnt3!=0:
    ## Открытие папки
    #os.system('start "" "D:\Clouds\Box Sync\!Work\!Real walls"')

    moveToToPrint()

    ## перемещение выбранных файлов в toPinPython (тип файлы распечатаны)
    questPrint()

    # todo Из всех папок принтед переместить в основную
    # todo qt вывод картинок
