#! python3
# -*- coding: utf-8 -*-
from commands import *
__version__ = "3.5.1"

# init
domains = []


# dynamic config
class State:
    ping_timeout = 20000  # in ms
    ping_count = 1
    sleep = 10  # between iterations
    count_of_ignored_timeouts = 1  # how much errors ignore
    first_iterate = True
    internet_status = False

    online = False
    if ("-o" in OS.args) or ("-online" in OS.args) or ("--online" in OS.args):
        online = True

    if ("-f" in OS.args) or ("-fast" in OS.args):
        sleep = 1

    router = "-r" in OS.args

    verbose = "-v" in OS.args

    print_ip = "-ip" in OS.args

    for arg in OS.args[1:]:
        if not arg.startswith("-"):
            domains.append(arg)

    fix_win_cmd = 0
    if OS.windows:
        fix_win_cmd = 1

    longest_hostname = 0
    cnt_working = 0

    failed_runs = 0


if State.router:
    domains += ['192.168.1.1']  # router by default
    if State.verbose:
        print(f"adding router, now {domains=}")

if State.online:
    domains += ['router.egigoka.me']
    domains += [Network.check_internet_apple]
    domains += [Network.check_internet_microsoft]

    def egigokas_server(debug=False):
        return Network.check_response("https://isup.egigoka.me/", "yep", debug=debug)

    domains += [egigokas_server]


def colorful_ping(hostname_or_external_function, args=()):
    if callable(hostname_or_external_function):
        response = hostname_or_external_function(*args, debug=False)
        if not isinstance(response, bool):
            raise TypeError(f"response must be bool, got {type(response)} instead")
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
        State.cnt_working += 1
    else:
        Print.colored(Str.rightpad(hostname + ' is down!' + " " * (State.longest_hostname - len(hostname)) + ' IP ' + str(ip),
                                   Console.width() - State.fix_win_cmd, " "), 'white', 'on_red')


def failed_notification(subtitle, message):
    State.failed_runs += 1
    if State.failed_runs > 1:
        macOS.notification(title="ping_", subtitle=subtitle,
                           message=message,
                           sound="Basso")


if State.verbose:
    print("init done")


def main():

    if State.verbose:
        print("finding longest hostname")

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

                if State.verbose:
                    print("sending first notification")

                macOS.notification(title="ping_", subtitle="Please, wait...", message="Check is running.")

        State.cnt_working = 0
        if State.print_ip:
            Print(f"Your IP: {Network.get_ip()}")
        threads = Threading()
        for hostname in domains:
            threads.add(colorful_ping, args=(hostname,))
        threads.start(wait_for_keyboard_interrupt=True)
        Print(Time.dotted())
        if State.cnt_working < len(domains)-State.count_of_ignored_timeouts:
            if OS.macos:
                failed_notification("Something is wrong!",
                                    str(State.cnt_working) + " domains of " + str(len(domains)) + " is online.")
            State.internet_status = False
        elif State.cnt_working < len(domains):
            if OS.macos:
                failed_notification("Just one timeout, worry?",
                                    str(State.cnt_working) + " domains of " + str(len(domains)) + " is online.")
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
            Time.sleep(State.sleep, verbose=True)


if __name__ == '__main__':
    main()
