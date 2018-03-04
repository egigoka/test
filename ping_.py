#! python3
# -*- coding: utf-8 -*-
__version__ = "2.0.0"
# going to commands7
__version__ = "2.0.1"
# PEP 8 (not full)
__version__ = "2.0.2"
# checkfolder bugfix
__version__ = "2.0.3"
# refactor for new commands7
# add coding in shebang
__version__ = "2.1.0"
# -online argument
__version__ = "2.2.0"
# -online-only argument
__version__ = "2.3.0"
# -wms-folders argument
__version__ = "2.4.0"
# check server avg load
__version__ = "2.5.0"
# -fast argument

from colorama import init
from commands7 import *
from termcolor import cprint

__logfile__ = Path.extend(Path.current(), "ping_.py.log")

class State:
    ping_timeout = 2000  # in ms
    ping_count = 5
    sleep = 60  # between iterations
    online = False
    online_only = False
    if ("-o" in sys.argv) or ("-online" in sys.argv) or ("--online" in sys.argv):
        online = True
    if ("-oo" in sys.argv) or ("-online-only" in sys.argv) or ("--online-only" in sys.argv):
        online_only = True
        online = True
    if ("-f" in sys.argv) or ("-fast" in sys.argv):
        sleep = 10


domains = ['192.168.1.1']  # router by default

if (not (State.online_only or State.wms_folders)) and (lin_servers):
    for ip, login in lin_servers.items():
        lin_servers[ip]['username'] = input("Username for " + str(ip) + ":")
        # todo сделать проверку пароля перед его установкой в словарь
        lin_servers[ip]['password'] = Str.input_pass("Password for " + str(ip) + ":")


if State.online_only:
    domains = []

if State.online:
    domains += ['yandex.ru']
    domains += ['google.com']
    domains += ['8.8.8.8']
    domains += ['8.8.4.4']
    domains += ['gmail.com']
    domains += ['vk.com']
    domains += ['starbounder.org']

errDomains = 0  # количество заведомо плохих доменов





def main():
    while True:

        print_end = newline
        if OS.name == 'windows':
            print_end = ''
        cnt_workin = 0
        for hostname in domains:  # сопсна, пинговка
            response = ping(hostname, timeout=State.ping_timeout, quiet=True, count=State.ping_count)
            if response:  # and then check the response...
                cprint(Str.rightpad(hostname + ' is up!', Console.width(), " "), 'white', 'on_green', end=print_end)
                cnt_workin += 1
            else:
                cprint(Str.rightpad(hostname + ' is down!', Console.width(), " "), 'white', 'on_red', end=print_end)
                plog(__logfile__, hostname + " is down", quiet=True)
        print(Time.rustime())
        # notification on macOS
        if OS.name == "macos":
            if cnt_workin < len(domains)-errDomains:
                color_upordown = 'on_yellow'
            else:
                color_upordown = 'on_green'

        Time.timer(State.sleep)
main()
