﻿#! python3
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from commands import *
__version__ = "3.0.3"


class State:
    ping_timeout = 2000  # in ms
    ping_count = 5
    sleep = 60  # between iterations
    count_of_ignored_timeouts = 1  # how much errors ignore
    online = False
    online_only = False
    first_iterate = True
    internet_status = False
    extended_rkn_list = False
    if ("-o" in sys.argv) or ("-online" in sys.argv) or ("--online" in sys.argv):
        online = True
    if ("-oo" in sys.argv) or ("-online-only" in sys.argv) or ("--online-only" in sys.argv):
        online_only = True
        online = True
    if ("-frkn" in sys.argv):
        online = True
        extended_rkn_list = True
    if ("-f" in sys.argv) or ("-fast" in sys.argv):
        sleep = 10

domains = ['192.168.0.1']  # router by default

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

if State.extended_rkn_list:
    # domains += ['1password.com']  # they doesn't reply to ICMP echo
    # domains += ['dlang.org']  # something strange
    # domains += ['ggpht.com']  # no DNS records, it use something unknown for me
    domains += ['gmail.com']
    domains += ['google.com.ua']
    domains += ['google.fr']
    domains += ['google.ru']
    # domains += ['googleusercontent.com']  # no DNS records, it use something unknown for me
    domains += ['gstatic.com']
    domains += ['youtube.com']
    # domains += ['ytimg.com']  # no DNS records, it use something unknown for me


# Json.save(Path.extend(Path.working(), "ping_configs", "ping_online_domains"), domains)

def main():
    while True:
        if State.extended_rkn_list:
            if OS.windows: Process.start("ipconfig", "/flushdns")
        if OS.macos:
            if State.first_iterate:
                macOS.notification(title="ping_", subtitle="Please, wait...", message="Check is running.")
        fix_win_cmd = 0
        if OS.windows:
            fix_win_cmd = 1
        cnt_workin = 0
        longest_hostname = 0
        for hostname in domains:
            if len(hostname) > longest_hostname:
                longest_hostname = len(hostname)
        for hostname in domains:
            response = Network.ping(hostname, timeout=State.ping_timeout, quiet=True, count=State.ping_count, return_ip=True)
            ip = response[1]
            # Print.debug(response[2])
            response = response[0]
            if response:
                Print.colored(Str.rightpad(hostname + ' is up!' + " "*(longest_hostname+2-len(hostname)) + ' IP ' + str(ip), Console.width()-fix_win_cmd, " "), 'white', 'on_green')
                cnt_workin += 1
            else:
                Print.colored(Str.rightpad(hostname + ' is down!' + " "*(longest_hostname-len(hostname)) + ' IP ' + str(ip), Console.width()-fix_win_cmd, " "), 'white', 'on_red')
        print(Time.dotted())
        if cnt_workin < len(domains)-State.count_of_ignored_timeouts:
            if OS.macos: macOS.notification(title="ping_", subtitle="Something is wrong!", message=str(cnt_workin)+" domains of "+str(len(domains))+" is online.", sound="Basso")
            State.internet_status = False
        elif cnt_workin < len(domains):
            if OS.macos: macOS.notification(title="ping_", subtitle="Just one timeout, worry?", message=str(cnt_workin)+" domains of "+str(len(domains))+" is online.", sound="Basso")
            State.internet_status = False
        else:
            if State.internet_status==False:
                subtitle = "You are back online!"
                if State.first_iterate:
                    subtitle = "You are online!"
                if OS.macos: macOS.notification(title="ping_", subtitle=subtitle, message="All "+str(len(domains))+" domains is online.", sound="Purr")
                State.internet_status = True
        State.first_iterate = False
        if State.internet_status:
            Time.sleep(State.sleep)

if __name__ == '__main__':
    main()
