#! python3
# -*- coding: utf-8 -*-
# version 3.1.5
# init ver
# f createdirs
# f createfile
# f savejson
# f loadjson
# f pathInWindowsWithSpacesToQuotes
# f pathInWindowsExtend
# ver 1.0.1
# f taskkill
# f jsonload print "json loaded" output
# f jsonsave print "json saved" output
# ver 1.0.2
# f file_wipe
# ver 1.0.3
# f filebackup
# f jsonrestorebak todo
# f jsoncheck todo
# f timestamp
# ver 1.0.4
# f screenblink
# ver 1.0.5
# update pathInWindowsExtend - three path extend now
# ver 1.0.6
# update pathInWindowsExtend - unlimited args now#
# ver 1.0.7
# update pathInWindowsExtend - bugfix
# ver 1.0.8
# update pathInWindowsExtend - bugfix
# ver 1.0.9
# update screenblink - bugfix
# ver 1.0.10
# update screenblink - bugfix
# ver 1.0.11
# update screenblink - bugfix
# ver 1.0.12
# update screenblink - bugfix
# ver 1.0.13
# update screenblink - add change size of console window
# ver 1.0.14
# getOutPutFromCommand
# getIntegers
# stringWidthNewlinesToString todo
# checkWidthOfConsole
# update screenblink
# ver 1.0.15
# enable new functionality in screenblink
# todo вместо вывода кучи строк вывести одну длинную?
# ver 1.0.16
# f homePath
# ver 1.0.17
# loadjson warning expanded
# ver 1.0.18
# f plog
# const newline
# f rustime
# ver 1.0.19
# plog add custom time
# rustime add custom time
# ver 1.0.20
# loadjson quiet option
# ver 1.0.21
# filebackup quiet option
# ver 1.0.22
# f ping
# ver 1.0.23
# f currentfolder
# ver 1.0.24
# gettime debug
# rustime update
# ver 1.0.25
# f winRepair_UnicodeEncodeError
# ver 1.0.26
# loadjson now create clean json if file not exist
# const ruble
# f cls
# ver 1.0.27
# f dottedtime
# ver 1.0.28
# f hidefile
# filebackup hidefile enable
# ver 1.0.29
# f winRepair_UnicodeEncodeError
# ver 1.0.30
# f doNothing
# ver 1.0.31
# savejson now can be quiet
# ver 1.0.32
# f deletefile
# ver 1.0.33
# f bigdigits
# ver 1.0.34
# f inputint
# ver 1.0.35
# fix savejson
# ver 1.0.36
# f isPython3
# ver 1.1.0
# openInNewWindow todo debug
# f getDomainOfUrl
# enabled getDomainOfUrl in ping
# const backslash
# f substring (string, before, after=None)
# ver 1.1.1
# f leftpad beta version todo fix all exceptions
# ver 1.1.2
# allias to f currentfolder as currentdir
# ver 1.1.3
# allias to f openInNewWindow as openInCurrentWindow
# ver 1.1.4
# f openInCurrentWindow now isn't allias
# ver 1.1.5
# f openInCurrentWindow doesn't work need fix
# ver 1.1.6
# fix f openInCurrentWindow
# ver 1.1.7
# fix get_time
# ver 1.1.8
# f run_code
# ver 1.1.7
# del f run_code(code): exec(code, globals()) (work only in local code)
# ver 1.1.8
# f tkinter_color
# ver 1.1.9
# loadjson, savejson print option
# ver 1.2.0
# allias to_quotes pathInWindowsWithSpacesToQuotes(path)
# ver 1.3.0
# f path_check
# ver 2.0.0
# pathInWindowsExtend now crossplatfowm and names path_extend # done
# ver 2.0.1
# wipefile mow file_wipe
# deletefile now file_delete # done
# filebackup now  # done
# pathInWindowsWithSpacesToQuotes now path_to_quotes
# homePath now home_path  # done
# createfile now file_create  # done
# ver 3.0.0
# file_backup now creates file in subfolder
# createdirs now dir_create # done
# wipefile now file_wipe
# ver 3.1.0
# f close_all_gone_wrong(error_while, try_to_do)
# ver 3.1.1
# f debug_print
# ver 3.1.2
# add some tests

# todo fix createfile

# todo backupfile backup to subfolder without doing crap
# todo countdown
# todo version diff

import os, \
       json, \
       sys, \
       shutil, \
       time, \
       random, \
       subprocess, \
       datetime
from tkinter import *

import termcolor, \
       colorama, \
       win_unicode_console, \
       win32api, \
       win32con

#from path import path
#win_unicode_console.enable()
colorama.init()
colorama.deinit()
from termcolor import colored, cprint #print_green_on_cyan = lambda x: cprint(x, 'green', 'on_cyan')

newline = '\n'
ruble = u"\u20bd" # \u20bd is ₽
backslash = "\ "[:1]


def isPython3():
    PY3K = sys.version_info >= (3, 0)
    return PY3K


def path_check(path):
    # try:
    #     path.rindex(backslash)
    # except ValueError:
    #     path = pathInWindowsExtend(currentfolder(), path)
    # return path
    return os.path.abspath(path)


def dir_create(filename):
    if os.path.isfile(filename):
        dir = os.path.dirname(filename)
    else:
        dir = filename
    if not os.path.exists(dir):
        os.makedirs(dir)


def file_create(filename):
    dir = os.path.dirname(filename)
    if not os.path.exists(dir):
        os.makedirs(dir)
    if not os.path.exists(filename):
        open(filename, 'a').close()
    if not os.path.exists(filename):
        close_all_gone_wrong("creating file " + str(filename), "script at path", sys.argv[0])


def file_delete(path, quiet = False):
    try:
        os.remove(path)
        if not quiet:
            print("file", path, "is deleted")
    except PermissionError:
        try:
            subprocess.call(["del", path])
        except:
            print("file", path, "is not deleted")


def timestamp():
    ts = time.time()
    return ts


def currentfolder():
    return os.path.dirname(os.path.realpath(__file__))


def currentdir():
    return currentfolder()


def dottedtime():
    gettime = datetime.datetime.now()
    dateandtime = str(gettime.year) + "." + str(gettime.month) + "." + str(gettime.day) + "_at_" + str(gettime.hour) \
                  + "." + str(gettime.minute) + "." + str(gettime.second) + "." + str(gettime.microsecond)
    return dateandtime


def get_time(size):
    command = "str(datetime.datetime.now()." + size + ")"
    print(command)
    time_output = exec(command)
    print(time_output)
    return time_output


def hidefileWin(filename, quiet=True):
    win32api.SetFileAttributes(filename, win32con.FILE_ATTRIBUTE_HIDDEN)
    if not quiet:
        print ("file", filename, "is hidden now")


def close_all_gone_wrong(error_while, try_to_repair):
    print("Error while", error_while)
    print("Try to repair", try_to_repair)
    print("Script is closing")
    sys.exit(1)


def debug_print(*arguments):
    print("Debug shit:")
    for arg in arguments:
        print("-" * checkWidthOfConsole(), end="")
        print(arg)
        print("-" * checkWidthOfConsole(), end="")


def file_backup(filename, subfolder = "bak", quiet = False):
    filename = path_check(filename) # normalize filename
    backupfilename = str(filename) + "." + dottedtime() + ".bak"  # add dottedtime to backup filename
    backupfilename = os.path.split(backupfilename)  # splitting filename to folder and file
    try:  # if subfolder has no len
        if len(subfolder) < 1:  # if subfolder has non-zero len
            subfolder = "bak"  # set subfolder to default
            print("len(subfolder) < 1, so subfolder = 'bak'")  # print error
    except:  # if subfolder has no len
        subfolder = "bak"  # set subfolder to default
        print("len(subfolder) < 1, so subfolder = 'bak'")  # print error
    subfolder = path_extend(backupfilename[0], subfolder)  # append subfolder name
    dir_create(subfolder)  # create subfolder
    backupfilename = path_extend(subfolder, backupfilename[1])  # backup file name full path
    shutil.copy2(filename, backupfilename)  # finnaly backup file
    hidefileWin(backupfilename)  # hiding file
    if not os.path.isfile(backupfilename):  # if file is not created
        close_all_gone_wrong("backup file", "script at path " + sys.argv[0])  # raise except
    if not quiet:  # if finction is not shutted up
        print("backup of file", filename, "created as", backupfilename) # all is ok, print that


def jsoncheck(filename):
    try:
        loadjson(filename)
    except:
        print("JSON is bad")


def savejson(filename, jsonstring, quiet=False, debug=False):
    try:
        settingsJsonTextIO = open(filename, "w")
        json.dump(jsonstring, settingsJsonTextIO)
        settingsJsonTextIO.close()
        if not quiet:
            print("JSON format succesfull saved")
        if debug:
            print("sys.argv[0] =",sys.argv[0])
            print(jsonstring)
    except:
        close_all_gone_wrong("savingJSON", "script at path " + sys.argv[0])
    json_test_string = loadjson(filename, quiet=True)
    if jsonstring != json_test_string:
        close_all_gone_wrong("savingJSON", "script at path " + sys.argv[0])


def loadjson(filename, quiet = False, debug=False):
    try:
        if not os.path.isfile(filename):
            file_create(filename)
            cleanjson = {}
            savejson(filename, cleanjson)
        settingsJsonTextIO = open(filename)
        jsonStringInMemory = json.load(settingsJsonTextIO)
        settingsJsonTextIO.close()
        if not quiet:
            print("JSON format succesfull loaded")
        if debug:
            print(jsonStringInMemory)
        return jsonStringInMemory
    except:
        close_all_gone_wrong("loadingJSON", "JSON at path" + filename)


def path_to_quotes(path):
    path = '"' + str(path) + '"'
    return path


def in_quotes(string):
    return path_to_quotes(string)


# def pathInWindowsExtend(*paths):
    # for path_ in paths:
    #     try:
    #         path
    #         path = str(path) + backslash + str(path_)
    #     except:
    #         path = path_
    # return path


def path_extend(*paths):
    for path_ in paths:
        try:
            path
            path = os.path.join(str(path), str(path_))
        except:
            path = path_ + backslash
    return path


def taskkill(process):
    command_ = "taskkill /f /im " + str(process) + ".exe"
    os.system(command_)
    return command_


def cls():
    os.system("cls")


def file_wipe(path):
    file = open(path, 'w')
    file.close()


def getIntegers(string):
    string = str(string)
    integerFinded = False
    integers = []
    # cnt = 0
    currentinteger = 0
    for symbol in string:
        try:
            int(symbol)
            currentinteger = currentinteger*10 + int(symbol)
            integerFinded = True
        except:
            if integerFinded:
                integers = integers + [currentinteger]
                currentinteger = 0
                integerFinded = False
            #print(integers)
    return integers


def stringWidthNewlinesToString(string): #todo сделать!
    return string


def getOutPutFromCommand(command, quiet = True):
    p = subprocess.check_output(command, shell=True)
    #p = subprocess.getoutput(command)
    # S.split(newline2) - todo сделать разделение по линиям
    pstr = p.decode("cp866")
    strings = stringWidthNewlinesToString(pstr)
    return strings


def checkWidthOfConsole():
    modecon = getOutPutFromCommand("mode con")
    width = getIntegers(modecon)[1]
    return width


def checkHeightOfConsole():
    modecon = getOutPutFromCommand("mode con")
    height = getIntegers(modecon)[0]
    if height > 100:
        height = 100
    return height


def screenblink(width = None, height = None, symbol = "#", sleep = 0.5, mode = "fast"):
    if width != None and height != None:
        os.system("mode con cols=" + str(width) + " lines=" + str(height))
    if width == None:
        width = checkWidthOfConsole()
    if height == None:
        height = checkHeightOfConsole()
    colorama.reinit()
    while True:
        colors = ["grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
        highlights = ["on_grey", "on_red", "on_green", "on_yellow", "on_blue", "on_magenta", "on_cyan", "on_white"]
        string = symbol * width
        color = random.choice(colors)
        colors.pop(colors.index(color))
        highlight = random.choice(highlights)
        if mode == "fast":
            try: # New version with one long line. Works perfect, as I see.
                string = string * height
                print(termcolor.colored(string, color, highlight))
                time.sleep(sleep)
            except KeyboardInterrupt as err:
                print (termcolor.colored("OK", "white", "on_grey"))
                colorama.deinit()
                cls()
                break
        else:
            try: #old multiline version. Have bug with get width of console and so create blank lines. Unexpected
                height_ = height
                while height_ > 0:
                    print(termcolor.colored(string, color, highlight))
                    height_ -= 1
                time.sleep(sleep)
            except KeyboardInterrupt as err:
                print (termcolor.colored("OK", "white", "on_grey"))
                colorama.deinit()
                cls()
                break
    colorama.deinit()


def home_path():
    homepath = getOutPutFromCommand("echo %userprofile%")
    homepath = homepath.rstrip("\r\n") # todo взять на заметку в getOutputFromCommand & stringWidthNewlinesToString
    return homepath


def rustime(customtime = None):
    if customtime:
        # onworktime = datetime.datetime.fromtimestamp(int(customtime)).strftime('%Y-%m-%d %H:%M:%S')
        # onworktime = datetime.datetime.fromtimestamp(int(customtime)).strftime(r'%d числа %m месяца %Y года в %H:%M:%S')
        # print(onworktime)
        # rustime = onworktime
        day = datetime.datetime.fromtimestamp(customtime).strftime('%d')
        month = datetime.datetime.fromtimestamp(customtime).strftime('%m')
        year = datetime.datetime.fromtimestamp(customtime).strftime('%Y')
        hour = datetime.datetime.fromtimestamp(customtime).strftime('%H')
        minute = datetime.datetime.fromtimestamp(customtime).strftime('%M')
        second = datetime.datetime.fromtimestamp(customtime).strftime('%S')
    else:
        gettime = datetime.datetime.now()
        day = gettime.strftime("%d")
        month = gettime.strftime('%m')
        year = gettime.strftime('%Y')
        hour = gettime.strftime('%H')
        minute = gettime.strftime('%M')
        second = gettime.strftime('%S')
    rustime = str(day) + " числа " + str(month) + " месяца " + str(year) + " года в " \
    + str(hour) + ":" + str(minute) + ":" + str(second)
    return rustime


def plog(logfile, logstring = "some shit happened", customtime = None, quiet = False):
    if not quiet:
        print(logstring)
    file_create(logfile)
    file_backup(logfile, quiet=True)
    file = open(logfile, "a")
    if customtime:
        file.write(rustime(customtime) + " " + str(logstring) + newline)
    else:
        file.write(rustime() + " " + str(logstring) + newline)
    file.close()


def ping(domain ="127.0.0.1", count = 1, quiet = False, logfile = None, timeout = 10000): # с таким эксепшном можно сделать куда проще это всё
    domain = getDomainOfUrl(domain)
    if not quiet:
        colorama.reinit()
        print("Pinging", domain, count, "times...")
        upmessage = domain + " is up!"
        downmessage = domain + " is down."
    try:
        pingoutput = getOutPutFromCommand("ping " + domain + " -n " + str(count) + " -w " + str(timeout))
    except KeyboardInterrupt:
        sys.exit()
    except:
        pingoutput = ""
    if "TTL" in pingoutput:
        up = True
    else:
        up = False
    if logfile:
        if up:
            plog(logfile, domain + " is up!", quiet=True)
            cprint(upmessage, "white", "on_green")
        else:
            plog(logfile, downmessage, quiet=True)
            cprint(downmessage, "white", "on_red")
    elif not quiet:
        if up:
            cprint(upmessage, "white", "on_green")
        else:
            cprint(downmessage, "white", "on_red")
        colorama.deinit()
    return up


def winRepair_UnicodeEncodeError(quiet = ""):
    if quiet == True:
        quiet = " > null"
    os.system("chcp 65001" + quiet)
    os.system("set PYTHONIOENCODING = utf - 8")


def doNothing():
    pass


def input_int(message = "Введите число: ", minimum = None, maximum = None, default = None, quiet = False):
    output_int = "jabla fitta"
    if default:
        message = "(Enter = " + str(default) + ")"
    while output_int == "jabla fitta": # цикл, пока не получит итоговое число
        try:
            integer = input(message)
            if integer != "":
                try:
                    integer = getIntegers(integer)[0]
                except:
                    print("Это не число")
                    raise ValueError
            elif default and integer != "":
                output_int = default
            elif integer == "":
                print("Это не число")
                raise ValueError
            if minimum:
                if int < minimum:
                    print("Число должно быть больше", minimum)
                    raise ValueError
            if maximum:
                if int > maximum:
                    print("Число должно быть меньше", maximum)
                    raise ValueError
            output_int = integer
            break
        except:
            pass
    if not quiet:
        print("Итоговое число:", output_int)
    return output_int


def openInNewWindow(*arguments):
    for argument_ in arguments:
        try:
            command
            command = command + " " + path_to_quotes(argument_)
        except:
            command = 'start "" ' + path_to_quotes(argument_)
    os.system(command)


def openInCurrentWindow(*arguments, commands = []):
    for argument_ in arguments:
        commands.append(str(argument_))
    subprocess.call(commands)


def substring(string, before, after=None):
    startfrom = string.find(before)
    if startfrom != -1:
        startfrom = string.find(before) + len(before)
    else:
        startfrom = 0
    if after:
        end_at = string[startfrom:].find(after)
        if end_at != -1:
            end_at = startfrom + string[startfrom:].find(after)
            substring = string[startfrom:end_at]
        else:
            substring = string[startfrom:]
    else:
        substring = string[startfrom:]
    return substring


def getDomainOfUrl(url):
    url_output = substring(url, "://", "/")
    if url_output == "":
        url_output = substring(url, "://")
    return url_output


def leftpad(string, leng, ch="0", rightpad=False):
    strOfCh = str(ch) * leng
    string = strOfCh[len(string):leng] + string
    if rightpad: # добавление символов справа из аллиаса (rightpad) функции
        string = strOfCh[len(string):leng] + string
    return string


def rightpad(string, leng, ch = "0"):
    leftpad(string, leng, ch = ch, rightpad=True)


def bigdigits(digits):
    def digits_init(height = False):
        Zero = ["   ###   ",
                "  #   #  ",
                " #     # ",
                "#       #",
                " #     # ",
                "  #   #  ",
                "   ###   ", ]
        One = ["    #    ",
               "   ##    ",
               "  # #    ",
               "    #    ",
               "    #    ",
               "    #    ",
               " ####### ", ]
        Two = [" ####### ",
               "#       #",
               "        #",
               " ####### ",
               "#        ",
               "#        ",
               "#########", ]
        Three = [" ####### ",
                 "#       #",
                 "        #",
                 "     ### ",
                 "        #",
                 "#       #",
                 " ####### ", ]
        Four = ["#       #",
                "#       #",
                "#       #",
                "#########",
                "        #",
                "        #",
                "        #", ]
        Five = ["#########",
                "#        ",
                "#        ",
                "######## ",
                "        #",
                "#       #",
                " ####### ", ]
        Six = [" ####### ",
               "#       #",
               "#        ",
               "######## ",
               "#       #",
               "#       #",
               " ####### ", ]
        Seven = ["#########",
                 "#       #",
                 "      ## ",
                 "    ##   ",
                 "  ##     ",
                 " #       ",
                 "#        ", ]
        Eight = [" ####### ",
                 "#       #",
                 "#       #",
                 " ####### ",
                 "#       #",
                 "#       #",
                 " ####### ", ]
        Nine = [" ####### ",
                "#       #",
                "#       #",
                " ########",
                "        #",
                "#       #",
                " ####### ", ]
        Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]
        height_int = len(Zero)
        if height:
            return height_int
        else:
            return Digits
    Digits = digits_init()
    column = 0
    while column < digits_init(height = True):
        line = ""
        digits = str(digits)
        for digit in digits:
            # try:
            digit = int(digit)
            line = line + Digits[digit][column] + " "
        print(line)
        column += 1


def tkinter_color(red, green, blue):
    my_color = str('#%02x%02x%02x' % (red, green, blue))
    return my_color


if __name__ == "__main__":
    file_backup(r"\\192.168.99.91\shares\scripts\utilsupdate\utils_dev.py")
    #print(rustime(1487646452.7141206))
    #ping(ip="192.168.99.91")
    #ping(ip="192.168.99.777")
    #screenblink()
    #print(checkWidthOfConsole())
    #print(checkHeightOfConsole())
    #import UtilsUpdate
    while True:
        try:
            command = input(">>")
            exec (command)
            exec("print(" + substring(command, before = '', after=' ') + ")", globals())
        except KeyboardInterrupt:
            sys.exit()
        except SyntaxError as err:
            print(err)



# Есть словарь: my_list = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]
# Сортировка словаря по одному ключу:
# my_list = sorted(my_list, key=lambda k: k['name'])
# Сортировка словаря по нескольким ключам:
# my_list = sorted(my_list, key=lambda x,y : cmp(x['name'], y['name']))
# или
# my_list.sort(lambda x,y : cmp(x['name'], y['name']))