#! python3
#import colorama
import subprocess
import os
#from colorama import init
#init()

from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')


domains = ["ya.ru", "dns-shop.ru", "vk.com", "google.com"]
domains = ["ya.ru"]
for domain in domains:
    cmd = "ping " + domain
    print(cmd)
    output = subprocess.check_output("ping ya.ru", shell = False, universal_newlines=True)
    print("---------------------------")
    print("utf-8")
    print("---------------------------")
    print(output.encode('utf-8',errors = 'replace'))
    print("---------------------------")
    print("ascii")
    print("---------------------------")
    print(output.encode('ascii', errors='replace'))
    print("---------------------------")
    print("koi8-r")
    print("---------------------------")
    print(output.encode('koi8-r', errors='replace'))
    print("---------------------------")
    print("cp866")
    print("---------------------------")
    print(output.encode('cp866', errors='replace'))
    print("---------------------------")
    print("cp1251")
    print("---------------------------")
    print(output.encode('cp1251', errors='replace'))
    print("---------------------------")
    print("cp850")
    print("---------------------------")
    print(output.encode('cp850', errors='replace'))
    print("---------------------------")
    print("iso8859 - 1")
    print("---------------------------")
    print(output.encode('iso8859 - 1', errors='replace'))
    print("---------------------------")
    print("fail")
    print("---------------------------")
    print(output.encode('fail', errors='replace'))
    print("---------------------------")

    out_bytes = subprocess.check_output(['ping', 'ya.ru'])
    out_text = out_bytes.decode('utf-8',errors='replace')
    #out_text2 = out_bytes.decode('utf-8', errors='strict')
    print(out_text.encode('utf-8',errors='replace'))
    #print(out_text2.encode('utf-8', errors='strict'))
    #import WConio
    #WConio.clrscr();
    #output_2 = output.decode('cp866',errors='strict')
    #print(output_2.encode('cp866', errors='replace'))
    print(output.encode('oem1251', errors='replace'))
    print(output.encode('oem-1251', errors='replace'))
    print("!!!")



