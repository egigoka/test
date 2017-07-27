#! python3
__version__ = "2.0.0"
# going to commands7
__version__ = "2.0.1"
# PEP 8 (not full)
__version__ = "2.0.2"
# checkfolder bugfix
from colorama import init
from commands7 import *
# from termcolor import colored, cprint #print_green_on_cyan = lambda x: cprint(x, 'green', 'on_cyan')
from termcolor import cprint
init()


__logfile__ = Path.extend(Path.current(), "ping_.py.log")


class State:
    online = False
    if ("-o" in sys.argv) or ("-online" in sys.argv) or ("--online" in sys.argv):
        online = True
    no81 = False
    if ("-no81" in sys.argv):
        no81 = True

domains = ['192.168.99.3']  # solvo
domains += ['192.168.99.5']  # zabbix
domains += ['192.168.99.7']  # solvo1
domains += ['192.168.99.8']  # solvo2 ??????
domains += ['192.168.99.9']  # solvo_BD ??????
domains += ['192.168.99.11']  # solvo win print
domains += ['192.168.99.18']  # keto
domains += ['192.168.99.91']  # notebook1
domains += ['192.168.99.253']  # share
if not State.no81:
    domains += ['192.168.98.81']  # fingerprint
domains += ['192.168.98.82']  # fingerprint
domains += ['192.168.98.83']  # fingerprint
domains += ['192.168.98.84']  # fingerprint

if State.online:
    domains += ['ya.ru']
errDomains = 0  # количество заведомо плохих доменов
timeout = "5000"  # таймаут пинга в мс
time_sleep = 60  # задержка перед новым проходом в с
count_ping = 2  # количество попыток

# debug_print(dir())


def checkfolder(folder, name):
    cnt_of_files = Dir.number_of_files(folder, quiet=True)
    if cnt_of_files is None:
        cnt_of_files = 0
    font_color = "white"
    if cnt_of_files <= 15:
        bg_color = "on_green"
    elif cnt_of_files <= 50:
        bg_color = "on_yellow"
    else:
        bg_color = "on_red"
    cprint(Str.rightpad(name + " contain " + str(cnt_of_files) + " files", Console.width(), " "),
           font_color, bg_color, end="")


def main():
    # cnt_workin = 2
    while True:
        # os.system('cls') # очистка экрана
        # if cnt_workin <= 1:  # определение цвета верхнего пустого блока
        #     color_upordown = 'on_red'
        # elif cnt_workin < len(domains)-errDomains:
        #     color_upordown = 'on_yellow'
        # else:
        #     color_upordown = 'on_green'
        cnt_workin = 0
        cnt_space_h = Console.height() - len(domains)  # заполнение блока цветными пробалами
        while cnt_space_h > 0:
            # cprint(" " * Console.width() *5, 'white', color_upordown, end = '')
            cnt_space_h += -1
        for hostname in domains:  # сопсна, пинговка
            response = ping(hostname, quiet=True, count=count_ping)
            if response:  # and then check the response...
                cprint(Str.rightpad(hostname + ' is up!', Console.width(), " "), 'white', 'on_green', end='')
                cnt_workin += 1
            else:
                cprint(Str.rightpad(hostname + ' is down!', Console.width(), " "), 'white', 'on_red', end='')
                plog(__logfile__, hostname + " is down", quiet=True)
        if get_os() == "windows":
            folders = [{"name":"wms2host", "location":Locations.wms2host},
                       {"name":"host2wms", "location":Locations.host2wms}]
            for folder in folders:
                checkfolder(folder["location"], folder["name"])
        print(Time.rustime())
        print("Sleep...")
        time.sleep(time_sleep)  # задержка перед новым проходом
main()
