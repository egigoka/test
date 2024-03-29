﻿#! python3
import sys
import os
#from utils import *
from commands7 import *
__version__ = "1.0.0"
# init release
__version__ = "1.0.1"
# bugfix
__version__ = "1.0.2"
# disable utils legacy module
__version__ = "1.0.3"
# commands7 more support
__version__ = "1.0.4"
# bugfix

pycharmName = "pycharm.exe"
pycharmFolder = r"C:\Program Files (x86)\JetBrains\PyCharm Community Edition 2016.3.2\bin"
pycharmExec = Path.extend(pycharmFolder, pycharmName)


# todo menu with items and its settings.json: solvounload, pycharm.py, utilsupdate, utils_dev, bartendernogui,
# todo parse__local, allocal


def openFile(fileFullPath):
    if fileFullPath[len(fileFullPath)-4:] == ".bat": # открытие не бат файла (я их использую лишь как ссылки), а .py
        batfilepathIO = open(fileFullPath, "r") # открытие файла
        pathOfRealFile = batfilepathIO.readline() # чтение первой строчки
        batfilepathIO.close() # закрытие файла
        if pathOfRealFile[:1] == "@":  # обработка случая, когда в бат файле указаны различные аргументы
            pathOfRealFile = substring(pathOfRealFile, before="@", after=" %")
        if "pyw" in pathOfRealFile:
            pathOfRealFile = substring(pathOfRealFile, "pyw ")
        if "py" in pathOfRealFile:
            pathOfRealFile = substring(pathOfRealFile, "py ")
        pathOfRealFile = Path.full(pathOfRealFile)
        pathOfRealFile = pathOfRealFile.rstrip(newline2)
        pathOfRealFile = pathOfRealFile.rstrip(newline)
        print(pathOfRealFile)
        Process.start(pycharmExec, pathOfRealFile, new_window=True)
    else:
        Process.start(pycharmExec, fileFullPath, new_window=True) # простое открытие файла



fileFullPath = sys.argv[1] # больше, больше магии

if os.path.isfile(fileFullPath):
    openFile(fileFullPath)
else: # обработка случая, когда не существует файла
    try:
        File.create(fileFullPath) # shutils.copy2 (shengbang.py)
    except FileNotFoundError: # обработка случая, когда указано лишь имя файла в текущей папке
        File.create(Path.full(fileFullPath))
    openFile(fileFullPath)
