#! python3
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from commands import *
__version__ = "3.2.3"


class State:
    ping_timeout = 10000  # in ms
    ping_count = 1
    sleep = 60  # between iterations
    count_of_ignored_timeouts = 1  # how much errors ignore
    first_iterate = True
    internet_status = False

    online = False
    if ("-o" in sys.argv) or ("-online" in sys.argv) or ("--online" in sys.argv):
        online = True

    online_only = False
    if ("-oo" in sys.argv) or ("-online-only" in sys.argv) or ("--online-only" in sys.argv):
        online_only = True
        online = True

    extended_rkn_list = False
    if ("-frkn" in sys.argv):
        online = True
        extended_rkn_list = True

    if ("-f" in sys.argv) or ("-fast" in sys.argv):
        sleep = 10

    print_ip = "-ip" in sys.argv

    fix_win_cmd = 0
    if OS.windows:
        fix_win_cmd = 1

    longest_hostname = 0
    cnt_workin = 0

    failed_runs = 0


domains = ['192.168.0.1']  # router by default

if State.online_only:
    domains = []

if State.online:
    domains += ['google.com']
    domains += ['8.8.8.8']
    domains += ['8.8.4.4']
    domains += ['gmail.com']
#    domains += ['starbounder.org']

if State.extended_rkn_list:
    domains += ['gmail.com']
    domains += ['google.com.ua']
    domains += ['google.fr']
    domains += ['google.ru']
    domains += ['gstatic.com']
    domains += ['youtube.com']


def colorful_ping(hostname):
    response = Network.ping(hostname, timeout=State.ping_timeout, quiet=True, count=State.ping_count, return_ip=True)
    ip = response[1]
    response = response[0]
    if response:
        Print.colored(
            Str.rightpad(hostname + ' is up!' + " " * (State.longest_hostname + 2 - len(hostname)) + ' IP ' + str(ip),
                         Console.width() - State.fix_win_cmd, " "), 'white', 'on_green')
        State.cnt_workin += 1
    else:
        Print.colored(Str.rightpad(hostname + ' is down!' + " " * (State.longest_hostname - len(hostname)) + ' IP ' + str(ip),
                                   Console.width() - State.fix_win_cmd, " "), 'white', 'on_red')


def failed_notification(subtitle, message):
    State.failed_runs += 1
    if State.failed_runs > 1:
        macOS.notification(title="ping_", subtitle=subtitle,
                           message=message,
                           sound="Basso")


def main():
    for hostname in domains:
        if len(hostname) > State.longest_hostname:
            State.longest_hostname = len(hostname)

    while True:
        Print.debug(State.failed_runs)
        if State.extended_rkn_list:
            Print.rewrite("Removing DNS cache...")
            if OS.windows:
                Process.start("ipconfig", "/flushdns")
        if OS.macos:
            if State.first_iterate:
                macOS.notification(title="ping_", subtitle="Please, wait...", message="Check is running.")
        State.cnt_workin = 0
        if State.print_ip:
            Print(f"Your IP: {Network.get_ip()}")
        threads = Threading(quiet=True)
        for hostname in domains:
            threads.add(colorful_ping, args=(hostname,))
        threads.start(wait_for_keyboard_interrupt=True)
        Print(Time.dotted())
        if State.cnt_workin < len(domains)-State.count_of_ignored_timeouts:
            if OS.macos:
                failed_notification("Something is wrong!",
                                    str(State.cnt_workin) + " domains of " + str(len(domains)) + " is online.")
            State.internet_status = False
        elif State.cnt_workin < len(domains):
            if OS.macos:
                failed_notification("Just one timeout, worry?",
                                    str(State.cnt_workin)+" domains of "+str(len(domains))+" is online.")
            State.internet_status = False
        else:
            if not State.internet_status:
                subtitle = "You are back online!"
                if State.first_iterate:
                    subtitle = "You are online!"
                if OS.macos:
                    macOS.notification(title="ping_", subtitle=subtitle, message="All "+str(len(domains))+" domains is online.", sound="Purr")
                State.internet_status = True
        State.first_iterate = False
        if State.internet_status:
            State.failed_runs = 0
            Time.sleep(State.sleep)
        Print.debug(State.failed_runs)


if __name__ == '__main__':
    main()
