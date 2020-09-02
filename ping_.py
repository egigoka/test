#! python3
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from commands import *
__version__ = "3.2.5"


class State:
    ping_timeout = 20000  # in ms
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

    if ("-f" in sys.argv) or ("-fast" in sys.argv):
        sleep = 10

    print_ip = "-ip" in sys.argv

    fix_win_cmd = 0
    if OS.windows:
        fix_win_cmd = 1

    longest_hostname = 0
    cnt_workin = 0

    failed_runs = 0


domains = []

if not State.online_only:
    domains += ['192.168.1.1']  # router by default

if State.online:
    domains += ['google.com']
    domains += ['8.8.8.8']
    domains += ['8.8.4.4']
    domains += ['gmail.com']
    domains += ['egigoka.me']
    domains += [Network.check_internet_apple]
    domains += [Network.check_internet_microsoft]


def colorful_ping(hostname_or_external_function):
    if callable(hostname_or_external_function):
        response = hostname_or_external_function(debug=True)  # temp debug
        hostname = hostname_or_external_function.__name__
        ip = hostname
    else:
        response = Network.ping(hostname_or_external_function, timeout=State.ping_timeout, quiet=True, count=State.ping_count, return_ip=True)
        ip = response[1]
        response = response[0]
        hostname = hostname_or_external_function
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
        try:
            length = len(hostname)
        except TypeError:
            length = len(hostname.__name__)
        if length > State.longest_hostname:
            State.longest_hostname = length

    while True:
        if OS.macos:
            if State.first_iterate:
                macOS.notification(title="ping_", subtitle="Please, wait...", message="Check is running.")
        State.cnt_workin = 0
        if State.print_ip:
            Print(f"Your IP: {Network.get_ip()}")
        threads = Threading()
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


if __name__ == '__main__':
    main()
