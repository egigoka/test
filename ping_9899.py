#! python3
import os
import time
from colorama import init
from utils import ping, checkWidthOfConsole, plog, currentfolder, path_extend, rustime
init()
import sys
from termcolor import colored, cprint #print_green_on_cyan = lambda x: cprint(x, 'green', 'on_cyan')

cmdWidth = checkWidthOfConsole() # symbols
cmdHeigth = 24 # symbols

__logfile__ = path_extend(currentfolder(), "ping_9899.py.log")


cnt = 230
domains = []
while cnt < 254:
    cnt += 1
    domains += ['192.168.98.' + str(cnt)]
cnt = 0
while cnt < 254:
    cnt += 1
    domains += ['192.168.99.' + str(cnt)]
errDomains = 0 # количество заведомо плохих доменов
timeout = "5000" # таймаут пинга в мс
time_sleep = 60 # задержка перед новым проходом в с
count_ping = 2 # количество попыток

def main():
    cnt_workin = 2
    while True:
        cmdWidth = checkWidthOfConsole()  # symbols
        #os.system('cls') # очистка экрана
        if cnt_workin <= 1: # определение цвета верхнего пустого блока
            color_upordown = 'on_red'
        elif cnt_workin < len(domains)-errDomains:
            color_upordown = 'on_yellow'
        else:
            color_upordown = 'on_green'
        cnt_workin = 0
        cnt_space_h = cmdHeigth - len(domains) # заполнение блока цветными пробалами
        while cnt_space_h > 0:
            #cprint(" " * cmdWidth *5, 'white', color_upordown, end = '')
            cnt_space_h += -1
        for hostname in domains: # сопсна, пинговка
            space = " " * (cmdWidth - len(hostname))
            response = ping(hostname, quiet = True, count = count_ping)
            if response == True: #and then check the response...
                cprint(hostname + ' is up!' + space[0:-7], 'white', 'on_green', end = '')
                cnt_workin += 1
            else:
                cprint(hostname + ' is down!' + space[0:-9], 'white', 'on_red', end = '')
                plog(__logfile__, hostname + " is down", quiet = True)
                #os.system("echo " + str(hostname) + " is down>> ping_.py.txt")

        print(rustime())
        print("Sleep...")
        time.sleep(time_sleep) # задержка перед новым проходом
main()

