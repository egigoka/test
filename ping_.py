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
__version__ = "2.6.0"
# macOS notifcation and deleted old staff
__version__ = "2.7.0"
# update to c8

from commands8 import *

class State:
    ping_timeout = 2000  # in ms
    ping_count = 5
    sleep = 60  # between iterations
    count_of_ignored_timeouts = 1  # how much errors ignore
    online = False
    online_only = False
    first_iterate = True
    internet_status = False
    if ("-o" in sys.argv) or ("-online" in sys.argv) or ("--online" in sys.argv):
        online = True
    if ("-oo" in sys.argv) or ("-online-only" in sys.argv) or ("--online-only" in sys.argv):
        online_only = True
        online = True
    if ("-f" in sys.argv) or ("-fast" in sys.argv):
        sleep = 10

domains = ['192.168.1.1']  # router by default

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

def main():
    while True:
        if OS.name == "macos":
            if State.first_iterate:
                macOS.notification(title="ping_", subtitle="Please, wait...", message="Check is running.")
        print_end = newline
        if OS.name == 'windows':
            print_end = ''
        cnt_workin = 0
        for hostname in domains:  # сопсна, пинговка
            response = Network.ping(hostname, timeout=State.ping_timeout, quiet=True, count=State.ping_count)
            if response:  # and then check the response...
                cprint(Str.rightpad(hostname + ' is up!', Console.width(), " "), 'white', 'on_green', end=print_end)
                cnt_workin += 1
            else:
                cprint(Str.rightpad(hostname + ' is down!', Console.width(), " "), 'white', 'on_red', end=print_end)
        print(Time.rustime())
        # notification on macOS
        if OS.name == "macos":
            if cnt_workin < len(domains)-State.count_of_ignored_timeouts:
                macOS.notification(title="ping_", subtitle="Something is wrong!", message=str(cnt_workin)+" domains of "+str(len(domains))+" is online.", sound="Basso")
                State.internet_status = False
            elif cnt_workin < len(domains):
                macOS.notification(title="ping_", subtitle="Just one timeout, worry?", message=str(cnt_workin)+" domains of "+str(len(domains))+" is online.", sound="Basso")
                State.internet_status = False
            else:
                if State.internet_status==False:
                    subtitle = "You are back online!"
                    if State.first_iterate:
                        subtitle = "You are online!"
                    macOS.notification(title="ping_", subtitle=subtitle, message="All "+str(len(domains))+" domains is online.", sound="Purr")
                    State.internet_status = True
            State.first_iterate = False
        Time.timer(State.sleep)
main()
