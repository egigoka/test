#! python3
# -*- coding: utf-8 -*-

from utils import *
newMenu = True


def definejsonname(jsonname): # Наименование места json-файла и загрузка оного в fullMENU
    fullMENU = loadjson(jsonname)
    __jsonfile__ = jsonname
    global __jsonfile__
    global fullMENU


def sortfullMENU():
    fullMENU = sorted(my_list, key=lambda k: k['priority'])
    global fullMENU


def getlastpriority():
    sortfullMENU()
    if fullMENU == {}:
        print ("MENU is empty")



def savemenuitem(item_description, item_command): # todo Формат итема = {priority : [common_command, [command_aliases], description]}
    fullMENU +=
    global fullMENU


def definemenuitem(): # todo приоритет, главная комманда, алиасы к комманде
    itemDescription = ""
    while itemDescription == "":
        itemDescription = input("Описание новой комманды: ")
    itemCommand = ""
    while itemCommand == "":
        itemCommand = input("Комманда для нового пункта меню: ")
    savemenuitem(itemDescription, itemCommand)


# Создание меню
while newMenu:
    definemenuitem()
    file_backup(__jsonfile__)



if __name__ == '__main__':
    definejsonname("test.menu")

# Генерация меню
    # Кириллическая раскладка
    # str.strip([chars]) method
    # Избегание коллизий
# Сохранение меню

# Исправление меню
    # Изменение приоритета
    # Изменение главной комманды
    # Изменение алиасов
    # Изменение описания
# Загрузка меню

# Вывод меню

# Запуск команд??? Возможно ли вообще?