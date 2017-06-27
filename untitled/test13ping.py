#! python3
import os
import time
from colorama import init
init()
import sys
from termcolor import colored, cprint #print_green_on_cyan = lambda x: cprint(x, 'green', 'on_cyan')

cmdWidth = 80 # symbols
cmdHeigth = 24 # symbols
cnt_workin = 2

domains = ['google.com', 'ya.ru', 'vk.com', 'appleinsider.ru', '192.168.1.1', 'dns-shop.ru'] # домены
errDomains = 1 # количество заведомо плохих доменов
timeout = "5000" # таймаут пинга в мс
time_sleep = 2 # задержка перед новым проходом в с

def main():
    while True:
        os.system('cls') # очистка экрана
        if cnt_workin <= 1: # определение цвета верхнего пустого блока
            color_upordown = 'on_red'
        elif cnt_workin < len(domains)-errDomains:
            color_upordown = 'on_yellow'
        else:
            color_upordown = 'on_green'
        cnt_workin = 0
        cnt_space_h = cmdHeigth - len(domains) # заполнение блока цветными пробалами
        while cnt_space_h > 0:
            cprint(" " * cmdWidth *5, 'white', color_upordown, end = '')
            cnt_space_h += -1
        for hostname in domains: # сопсна, пинговка
            space = " " * (cmdWidth - len(hostname))
            response = os.system("ping -n 1 " + hostname + " -w " + timeout + " > NUL")
            if response == 0: #and then check the response...
                cprint (hostname + ' is up!' + space[0:-7], 'white', 'on_green', end = '')
                cnt_workin += 1
            else:
                cprint(hostname + ' is down!' + space[0:-9], 'white', 'on_red', end = '')
        print("Sleep...", end = '')
        time.sleep(2) # задержка перед новым проходом
main()