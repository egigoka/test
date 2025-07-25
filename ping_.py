﻿#! python3
# -*- coding: utf-8 -*-
import requests
from commands import *

__version__ = "3.7.0"

# init
domains = []


# dynamic config
class State:
    ping_timeout = 4000  # in ms
    ping_count = 1
    sleep = 10  # between iterations
    count_of_ignored_timeouts = 1  # how much errors ignore
    first_iterate = True
    internet_status = False

    online = ("-o" in OS.args) or ("-online" in OS.args) or ("--online" in OS.args)

    if ("-f" in OS.args) or ("-fast" in OS.args) or ("--fast" in OS.args):
        sleep = 1
    
    clear_cache = ("-c" in OS.args) or ("-cache" in OS.args) or ("--cache" in OS.args) or ("--clear-cache" in OS.args)

    router = "-r" in OS.args

    verbose = ("-v" in OS.args) or ("-verbose" in OS.args) or ("--verbose" in OS.args)

    print_ip = ("-ip" in OS.args) or ("--ip" in OS.args)

    check_ip = ("-csc" in OS.args) or ("--check-safe-country" in OS.args)

    for arg in OS.args[1:]:
        if not arg.startswith("-"):
            domains.append(arg)

    fix_win_cmd = 0
    if OS.windows:
        fix_win_cmd = 1

    longest_hostname = 0
    cnt_working = 0

    failed_runs = 0

    countries_that_create_fear = ("ru", "kz", "cn")


if State.router:
    domains += ['192.168.1.1']  # router by default
    if State.verbose:
        print(f"adding router, now {domains=}")

if State.online:
#    domains += ['router.egigoka.me']
    domains += [Network.check_internet_apple]
    domains += [Network.check_internet_microsoft]

#    def egigokas_server(debug=False):
#        return Network.check_response("https://isup.egigoka.me/", "yep", debug=debug)
#
#    domains += [egigokas_server]


def get_country_of_ip(ip):
    endpoint = f'https://ipinfo.io/{ip}/json'
    try:
        response = requests.get(endpoint, verify=True)

        if response.status_code != 200:
            country = 'Status:', response.status_code, 'Problem with the request. Exiting.'
            Print.prettify(response)
            if OS.macos:
                macOS.notification(title="ping_", subtitle="Failed to get country",
                                   message=str(response),
                                   sound="Basso")
        else:
            data = response.json()
            if "country" in data.keys():
                country = data['country']
            elif "bogon" in data.keys():
                country = "bogon" if data["bogon"] else Print.prettify(data, quiet=True)
            else:
                macOS.notification(title="ping_", subtitle="Failed to get country",
                                   message=str(data),
                                   sound="Basso")
                Print.prettify(data)
                country = data
    except requests.exceptions.ConnectionError as e:
        country = e
    return str(country)


get_country_of_ip = CachedFunction(get_country_of_ip, 60*60)


def colorful_ping(hostname_or_external_function, args=()):
    b = Bench()
    if callable(hostname_or_external_function):
        kwargs = {"timeout", State.ping_timeout / 1000}
        response = hostname_or_external_function(*args, debug=False)
        if not isinstance(response, bool):
            raise TypeError(f"response must be bool, got {type(response)} instead")
        hostname = hostname_or_external_function.__name__
        ip = hostname
    else:
        response = Network.ping(hostname_or_external_function, timeout=State.ping_timeout, quiet=True, count=State.ping_count)
        ip = Network.get_ip(hostname_or_external_function)
        hostname = hostname_or_external_function
    time = b.end() * 1000
    timeout = State.ping_timeout
    time_f = f"{time:.2f}"
    time_prefix = " " * (len(f"{timeout:.2f}") - len(time_f))
    hostname_prefix = " " * (State.longest_hostname + 2 - len(hostname))

    if response:
        status = "up!  "
        color_bg = "on_green"
        State.cnt_working += 1
    else:
        status = "down!"
        color_bg = "on_red"

    formatted_text = Str.rightpad(f"{hostname} is {status} {time_prefix}{time_f}ms{hostname_prefix}IP {ip}",
                     Console.width() - State.fix_win_cmd, " ")



    colored_text = Print.colored(formatted_text, 'white', color_bg, verbose=False)

    Print(f"{colored_text}")


def failed_notification(subtitle, message):
    State.failed_runs += 1
    if State.failed_runs > 1:
        macOS.notification(title="ping_", subtitle=subtitle,
                           message=message,
                           sound="Basso")


def ossystem(command):
    if State.verbose: Print.colored(command, "magenta")
    stdout, stderr = Console.get_output(command, return_merged=False)
    if State.verbose: Print.colored(stdout, "green")
    if stderr: Print.colored(stderr, "red")
    return stdout + stderr 


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
        
        if State.clear_cache:
            ossystem("nbtstat -R")
            ossystem("ipconfig /flushdns")
        State.cnt_working = 0
        if State.print_ip or State.check_ip:
            Print.rewrite("Getting ip...")
            ip = Network.get_public_ip()
        if State.print_ip:
            Print(f"Your public IP: {ip}")
        if State.check_ip:
            Print.rewrite("Getting country...")
            country = get_country_of_ip(ip)
                
            if country.lower() in State.countries_that_create_fear:
                if OS.macos:
                    macOS.notification(title="ping_", subtitle='VPN is malfunctioning',
                                                                   message=f"current country is {country}",
                                                                   sound="Basso")
            Print.rewrite()
            print(f"Country: {country}")

        threads = Threading()
        for hostname in domains:
            threads.add(colorful_ping, args=(hostname,))
        threads.start(wait_for_keyboard_interrupt=True)
        print()
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
