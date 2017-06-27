#! python3
import sys
import os
from utils import *

pycharmName = "pycharm.exe"
pycharmFolder = r"C:\Program Files (x86)\JetBrains\PyCharm Community Edition 2016.3.2\bin"
pycharmExec = path_extend(pycharmFolder, pycharmName)


# todo menu with items and its settings.json: solvounload, pycharm.py, utilsupdate, utils_dev, bartendernogui,
# todo parse__local, allocal


def openFile(fileFullPath):
    if fileFullPath[len(fileFullPath)-4:] == ".bat": # открытие не бат файла (я их использую лишь как ссылки), а .py
        batfilepathIO = open(fileFullPath, "r") # открытие файла
        pathOfRealFile = batfilepathIO.readline() # чтение первой строчки
        batfilepathIO.close() # закрытие файла
        if pathOfRealFile[:1] == "@":  # обработка случая, когда в бат файле указаны различные аргументы
            pathOfRealFile = substring(pathOfRealFile, "@", "%")
        if "pyw" in pathOfRealFile:
            pathOfRealFile = substring(pathOfRealFile, "pyw ")
        print(pathOfRealFile)
        openInNewWindow(pycharmExec, pathOfRealFile)
    else:
        openInNewWindow(pycharmExec, fileFullPath) # простое открытие файла



fileFullPath = sys.argv[1] # больше, больше магии

if fileFullPath.find(backslash) == -1:
    fileFullPath = path_extend(currentdir(), fileFullPath)

if os.path.isfile(fileFullPath):
    openFile(fileFullPath)
else: # обработка случая, когда не существует файла
    try:
        file_create(fileFullPath) # shutils.copy2 (shengbang.py)
    except FileNotFoundError: # обработка случая, когда указано лишь имя файла в текущей папке
        file_create(path_extend(currentdir(), fileFullPath))
    openFile(fileFullPath)
