#! python3
# -*- coding: utf-8 -*-
# http://python.su/forum/topic/15531/?page=1#post-93316
from commands8 import *


strings = Str.nl(Console.get_output('tasklist /svc /fi "imagename eq svchost.exe"'))
strings = strings[3:]  # remove table legend


def get_full_name_of_service(short_name):
    output = Console.get_output("sc GetDisplayName "+short_name)
    name = Str.substring(output, before="Name = ", after="\r\n")
    return name


services = {}
executable = None
pid = None

for string in strings:
    print(string)
    for i in Int.from_to(1, len(string)):
        string = string.replace("  ", " ")
    words = string.split(" ")
    if len(words) == 1: continue
    skip = 0
    if ".exe" in words[0]:
        executable = words[0]
        skip += 1
    try:
        pid = int(words[1])
        skip += 1
    except ValueError:
        pass
    for service in words[skip:]:
        if len(service) == 0: continue
        service = service.rstrip(",")
        services[service] = {"pid":pid, "executable":executable, "full_name":get_full_name_of_service(service)}

services = Dict.sorted_by_key(services, case_insensitive=True)

for service, values in Dict.iterable(services):
    print(service, values)

service_name = "SSDPSRV"

Process.start("net", "start", service_name)
# print(services[service_name]["full_name"], "is started?")

Process.kill(services[service_name]["pid"])
print(services[service_name]["full_name"], "is killed")
