#! python3
# -*- coding: utf-8 -*-

from copypaste import copy, paste

start_int = input("Начинаем с: ")

while True:
    input_check = input("Введите новое начальное число или нажмите Enter: ")
    try:
        start_int = int(input_check)
        print("new start_int =", start_int)
    except:
        start_int = int(start_int) - int(paste())
        print("input =", input_check, "output =", start_int)
    copy(" /" + str(start_int))