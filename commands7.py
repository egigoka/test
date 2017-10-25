#! python3
# -*- coding: utf-8 -*-
import os
import sys
if True:
    import datetime
    start_bench_no_bench = datetime.datetime.now()
if True:
    __version__ = "1.0.0"
    # f createdirs
    # f createfile
    # f savejson
    # f loadjson
    # f pathInWindowsWithSpacesToQuotes
    # f pathInWindowsExtend
    __version__ = "1.1.0"
    # f taskkill
    # f jsonload print "json loaded" output
    # f jsonsave print "json saved" output
    __version__ = "1.2.0"
    # f file_wipe
    __version__ = "1.3.0"
    # f filebackup
    # f jsonrestorebak todo
    # f jsoncheck todo
    # f timestamp
    __version__ = "1.4.0"
    # f screenblink
    __version__ = "1.4.1"
    # update pathInWindowsExtend - three path extend now
    __version__ = "1.4.2"
    # update pathInWindowsExtend - unlimited args now#
    __version__ = "1.4.3"
    # update pathInWindowsExtend - bugfix
    __version__ = "1.4.4"
    # update pathInWindowsExtend - bugfix
    __version__ = "1.4.5"
    # update screenblink - bugfix
    __version__ = "1.4.6"
    # update screenblink - bugfix
    __version__ = "1.4.7"
    # update screenblink - bugfix
    __version__ = "1.4.8"
    # update screenblink - bugfix
    __version__ = "1.4.9"
    # update screenblink - add change size of console window
    __version__ = "1.5.0"
    # f getOutPutFromCommand
    # f getIntegers
    # stringWidthNewlinesToString todo
    # f checkWidthOfConsole
    # update screenblink
    __version__ = "1.5.1"
    # enable new functionality in screenblink
    # todoed вместо вывода кучи строк вывести одну длинную?
    __version__ = "1.6.0"
    # f homePath
    __version__ = "1.6.1"
    # loadjson warning expanded
    __version__ = "1.7.0"
    # f plog
    # const newline
    # f rustime
    __version__ = "1.7.0"
    # plog add custom time
    # rustime add custom time
    __version__ = "1.7.1"
    # loadjson quiet option
    __version__ = "1.7.2"
    # filebackup quiet option
    __version__ = "1.8.0"
    # f ping
    __version__ = "1.9.0"
    # f currentfolder
    __version__ = "1.9.1"
    # gettime debug
    # rustime update
    __version__ = "1.10.0"
    # f winRepair_UnicodeEncodeError
    __version__ = "1.11.0"
    # loadjson now create clean json if file not exist
    # const ruble
    # f cls
    __version__ = "1.12.0"
    # f dottedtime
    __version__ = "1.13.0"
    # f hidefile
    # filebackup hidefile enable
    __version__ = "1.14.0"
    # f winRepair_UnicodeEncodeError
    __version__ = "1.15.0"
    # f doNothing
    __version__ = "1.15.1"
    # savejson now can be quiet
    __version__ = "1.16.0"
    # f deletefile
    __version__ = "1.17.0"
    # f bigdigits
    __version__ = "1.18.0"
    # f inputint
    __version__ = "1.18.1"
    # fix savejson
    __version__ = "1.19.0"
    # f isPython3
    __version__ = "1.20.0"
    # openInNewWindow
    # f getDomainOfUrl
    # enabled getDomainOfUrl in ping
    # const backslash
    # f substring (string, before, after=None)
    __version__ = "1.21.0"
    # f leftpad beta version todo fix all exceptions
    __version__ = "1.22.0"
    # allias to f currentfolder as currentdir
    __version__ = "1.23.0"
    # allias to f openInNewWindow as openInCurrentWindow
    __version__ = "1.24.0"
    # f openInCurrentWindow now isn't allias
    __version__ = "1.25.0"
    # f openInCurrentWindow doesn't work need fix
    __version__ = "1.25.1"
    # fix f openInCurrentWindow
    __version__ = "1.25.2"
    # fix get_time
    __version__ = "1.26.0"
    # f run_code
    __version__ = "1.25.2"
    # del f run_code(code): exec(code, globals()) (work only in local code)
    __version__ = "1.26.0"
    # f tkinter_color
    __version__ = "1.26.1"
    # loadjson, savejson print option
    __version__ = "1.27.0"
    # allias to_quotes pathInWindowsWithSpacesToQuotes(path)
    __version__ = "1.28.0"
    # f path_check
    __version__ = "2.0.0"
    # pathInWindowsExtend is crossplatfowm and now names path_extend # done
    __version__ = "3.0.0"
    # wipefile mow file_wipe
    # deletefile now file_delete # done
    # filebackup now  # done
    # pathInWindowsWithSpacesToQuotes now path_to_quotes
    # homePath now home_path  # done
    # createfile now file_create  # done
    __version__ = "4.0.0"
    # file_backup now creates file in subfolder
    # createdirs now dir_create # done
    # wipefile now file_wipe
    __version__ = "4.1.0"
    # f close_all_gone_wrong(error_while, try_to_do)
    __version__ = "4.2.0"
    # f debug_print
    __version__ = "4.2.1"
    # add some tests
    __version__ = "4.3.0"
    # f get_os
    __version__ = "4.3.1"
    # add some crossplatformity
    __version__ = "4.3.2"
    # add some crossplatformity
    __version__ = "4.3.3"
    # add some crossplatformity
    __version__ = "4.3.4aplha1"
    # add some crossplatformity
    __version__ = "4.3.4aplha2"
    # add some crossplatformity plog, path_extend
    __version__ = "5.0.0alpha1"
    # hidefileWin now file_hide
    # add some crossplatformity file_hide
    # f file_rename
    # f file_move
    # file_hide bugfix
    # add some crossplatformity ping
    # path_check now path_full
    __version__ = "5.0.0alpha2"
    # rightpad bugfix
    __version__ = "5.0.0alpha3"
    # path_extend bugfix
    __version__ = "5.0.0alpha4"
    # path_extend bugfix
    __version__ = "5.0.0alpha5"
    # path_extend bugfix
    __version__ = "5.0.0alpha6"
    # path_extend bugfix
    __version__ = "5.0.0alpha7"
    # path_extend debugging
    __version__ = "5.0.0alpha8"
    # path_extend bugfix
    __version__ = "5.1.0"
    # file_backup now return backupfilename
    __version__ = "5.1.1"
    # path_extend bugfix
    __version__ = "5.1.2"
    # path_extend support for windows \\ip_or_pcname\paths
    __version__ = "5.1.3"
    # path_extend bugfix
    __version__ = "5.1.4"
    # path_extend bugfix
    __version__ = "5.1.5"
    # path_extend bugfix
    __version__ = "5.1.6"
    # file_create bugfix
    __version__ = "5.1.7"
    # file_create bugfix
    __version__ = "5.1.8"
    # file_create bugfix
    __version__ = "5.1.9"
    # add some crossplatformity cls
    __version__ = "5.1.10"
    # file_hide bugfix
    __version__ = "5.1.11"
    # screenblink simplification
    __version__ = "5.1.12"
    # stringWidthNewlinesToString now work
    __version__ = "5.1.13"
    # getOutPutFromCommand(split_lines=False)
    __version__ = "5.1.14"
    # stringWidthNewlinesToString now crossplatfowm
    __version__ = "5.1.15"
    # file_hide simplification
    __version__ = "5.1.16"
    # getOutPutFromCommand bugfix
    __version__ = "6.0.0"
    # isPython3 now is_python3
    # currentfolder and currentdir now path_current
    __version__ = "7.0.0alpha1"
    # now most of functions in classes
    # Time.get bugfix
    __version__ = "7.0.0alpha2"
    # File.delete bugfix
    __version__ = "7.0.0alpha2"
    # f Dir.list_of_files
    __version__ = "7.0.0alpha3"
    # getOutPutFromCommand now Console.get_output
    __version__ = "7.0.0alpha4"
    # getIntegers now Str.get_integers
    __version__ = "7.0.0alpha5"
    # Process.start bugfix
    __version__ = "7.0.0alpha6"
    # Str.to_quotes bugfix
    __version__ = "7.0.0alpha7"
    # debug option to Codegen
    # f Str.split_every
    # optimize debug_print
    # debug_print no swearing anymore
    # Str.split_every bugfix
    __version__ = "7.0.0alpha8"
    # f Path.set_current
    __version__ = "7.0.0alpha9"
    # allias to Dir.list_of_files as Dir.contents
    __version__ = "7.0.0alpha10"
    # new to Locations
    __version__ = "7.0.0alpha11"
    # f Dir.number_of_files()
    __version__ = "7.0.0alpha12"
    # f Tkinter.warn()
    __version__ = "7.0.0alpha13"
    # Tkinter.warn() try to grab focus
    __version__ = "7.0.0alpha14"
    # Tkinter.warn() try to grab focus in different way (it works)
    __version__ = "7.0.0alpha15"
    # Time.get() bugfix
    __version__ = "7.1.0alpha1"
    # class Bench for benchmarking
    __version__ = "7.1.0alpha2"
    # bench while loading
    __version__ = "7.1.0alpha3"
    # alias Dir.contain to Dir.contents
    __version__ = "7.1.0alpha4"
    # input_int bugfix
    __version__ = "7.1.0alpha5"
    # Str.rightpad bugfix
    __version__ = "7.1.0alpha6"
    # more like PEP8
    __version__ = "7.2.0alpha1"
    # f Windows.lock
    __version__ = "7.3.0alpha1"
    # f Random.integer
    __version__ = "7.3.0alpha2"
    # f Bench.get
    __version__ = "7.3.0alpha3"
    # Process.kill() now support macOS
    __version__ = "7.4.0alpha1"
    # f Wget.download()
    __version__ = "7.4.0alpha2"
    # bugfix Path.extend
    __version__ = "7.4.0alpha3"
    # bugfix Path.extend
    __version__ = "7.4.0alpha4"
    # bugfix Path.extend
    __version__ = "7.4.0alpha5"
    # bugfix Wget.download
    __version__ = "7.4.0alpha6"
    # bugfix Path.extend
    __version__ = "7.4.0alpha7"
    # bugfix Wget.download
    __version__ = "7.4.0alpha8"
    # bugfix Wget.download
    # f Str.to_quotes_2
    # Process.start now more crossplatfowm
    # debug option to Process.start
    # pureshell option to Process.start
    __version__ = "7.5.0alpha1"
    # substring is now warning and moved to Str.substring
    # Str.strings_to_newlines arg quiet
    __version__ = "7.6.0alpha1"
    # f File.read
    # class Repl
    # f Repl.loop()
    __version__ = "7.6.0alpha2"
    # bugfix File.read
    # Repl.loop safe arg
    __version__ = "7.6.0alpha3"
    # Str.leftpad bugfix
    __version__ = "7.7.0aplha1"
    # cls Int
    # f Int.from_to
    __version__ = "7.7.0aplha2"
    # Int.from_to bugfix
    __version__ = "7.7.0aplha3"
    # Path.extend support for ~ path
    __version__ = "7.7.0aplha4"
    # Path.extend bugfix for ~ path
    __version__ = "7.8.0alpha1"
    # f Dir.batch_rename
    __version__ = "7.8.0alpha2"
    # Wget.download fix for blocking by wget user_agent
    __version__ = "7.8.0alpha3"
    # Process.start bugfix
    __version__ = "7.9.0alpha1"
    # cls OS
    # var OS.name
    # now get_os() is OS.name
    # var OS.family
    # warning bugfix
    __version__ = "7.10.0-alpha"
    # new versioning
    # new arg for debug_print - raw
    __version__ = "7.11.0-alpha"
    # var OS.windows_version
    __version__ = "7.11.1-alpha"
    # var OS.windows_version bugfix
    __version__ = "7.12.0-alpha"
    # screenblink is back, meh
    __version__ = "7.12.1-alpha"
    # Codegen.start bugfix
    __version__ = "7.12.2-alpha"
    # Locations.share bugfix
    __version__ = "7.13.0-alpha"
    # Process.start warning on macOS
    __version__ = "7.13.1-alpha"
    # fix in import how-to
    __version__ = "7.13.2-alpha"
    # Locations.scripts_folder
    __version__ = "7.14.0-alpha"
    # debug_print now Print.debug
    # f Print.rewrite()
    # Time.timer update
    __version__ = "7.14.1-alpha"
    # Print.rewrite bugfix
    # Time.timer bugfix
    __version__ = "7.14.2-alpha"
    # Print.rewrite bugfix on Windows
    __version__ = "7.14.3-alpha"
    # import how-to now kinda interactive
    __version__ = "7.15.0-alpha"
    # f mine_import
    __version__ = "7.15.1-alpha"
    # mine_import update for pyautogui support
    __version__ = "7.16.0-alpha"
    # OS.display


# todo countdown and 1 line option like "Sleep ** seconds..."
# todo version diff
# todo delete all try wide except bugs-hidingers

def is_python3():
    is_true = sys.version_info >= (3, 0)
    return is_true


class OS:
    windows_version = None
    if sys.platform == "linux" or sys.platform == "linux2":
        name = "linux"
    elif sys.platform == "win32" or sys.platform == "cygwin":
        name = "windows"
        windows_version = sys.getwindowsversion().major
    elif sys.platform == "darwin":
        name = "macos"

    if name == "windows":
        family = "nt"
    elif name in ["macos", "linux"]:
        family = "unix"

    try:
        os.environ['DISPLAY']
        display = True
    except KeyError:
        display = False
        print("Your system haven't display -_-")



def mine_import(module_name, objects=None):
    if is_python3():
        pipver = "3"
    else:
        pipver = ""
    ###########RARE###########
    if module_name == "pyautogui":
        if OS.name == "linux":
            if is_python3():
                os.system("apt-get install python-xlib")
            else:
                os.system("apt-get install python3-Xlib")
        if OS.name == "macos":
            os.system("pip" + pipver + " install python" + pipver + "-xlib")
            os.system("pip" + pipver + " install pyobjc-core")
            os.system("pip" + pipver + " install pyobjc")
    ###########RARE###########
    if objects:
        import_command = "from " + module_name + " import " + objects
    else:
        import_command = "import " + module_name
    try:
        exec(import_command, globals())
    except ImportError:

        command = "pip" + pipver + " install " + module_name
        os.system(command)
        print(command)
        input()
        exec(import_command, globals())


if OS.display:
    mine_import("pyautogui")
    mine_import("tkinter", objects="*")
    #from tkinter import *
mine_import("colorama")
import json, \
       shutil, \
       time, \
       random, \
       subprocess, \
       datetime, \
       re, \
       ctypes


# ###############################################!!! HOW TO IMPORT !!!##################################################
# http://python.su/forum/topic/15531/?page=1#post-93316
def how_to_import_this_useless_stuff():
    print("""# import module like this:
# mine commands
import sys
sys.path.append("../..")
sys.path.append("..\..")
sys.path.append(".")
sys.path.append("..")
sys.path.append("./term")
sys.path.append(r".\term")
from commands7 import *""")







def get_os():
    warning("get_os now OS.name")
    return OS.name

if OS.name == "windows":
    import win_unicode_console, \
           win32api, \
           win32con, \
           termcolors

# win_unicode_console.enable()
colorama.init()
colorama.deinit()
mine_import("termcolor", objects="colored, cprint")  # print_green_on_cyan = lambda x: cprint(x, 'green', 'on_cyan')

newline = '\n'
ruble = u"\u20bd"  # \u20bd is ₽
backslash = "\ "[:1]
newline2 = "\r\n"





class Print():
    @staticmethod
    def debug(*arguments, raw=False):
        line = "-" * Console.width()
        print("Debug sheet:")
        for arg in arguments:
            print(line, end="")
            if raw:
                print(repr(arg))
            else:
                print(arg)
            print(line)

    @staticmethod
    def rewrite(*arguments, sep = " ", raw=False):
        line = " " * Console.width()
        if OS.name == "windows":
            line = line[:-1]
        print(line, end="\r")
        print(*arguments, sep=sep, end="\r")

    @classmethod
    def test(cls, string):

        for i in range(100):
            time.sleep(1)
            print("\b" * i)
            print("fuck")

        for i in range(100):
            if i != 0:
                print('\b' * 6)
            else:
                print('header')
            print(str(i) + '%').ljust(4),
            sys.stdout.flush()
            time.sleep(0.05)

        from time import sleep
        for i in range(100):
            sys.stdout.write('%2s%%' % i)
            sys.stdout.flush()
            sleep(1)
            sys.stdout.write('\b' * 3)



#PRINT REWRITE

def debug_print(*arguments, raw=False):
    warning("debug_print now Print.debug")
    Print.debug(*arguments, raw=raw)


class Str:
    @staticmethod
    def to_quotes(some_string):
        return '"' + str(some_string) + '"'

    @staticmethod
    def to_quotes_2(some_string):
        return '"' + str(some_string) + '"'

    @staticmethod
    def get_integers(string): # todo support for -
        string = str(string)
        integer_found = False
        integers = []
        # cnt = 0
        current_integer = 0
        for symbol in string:
            try:
                int(symbol)
                current_integer = current_integer*10 + int(symbol)
                integer_found = True
            except ValueError:
                if integer_found:
                    integers = integers + [current_integer]
                    current_integer = 0
                    integer_found = False
        if integer_found:
            integers = integers + [current_integer]
            current_integer = 0
            integer_found = False
        return integers

    @staticmethod
    def newlines_to_strings(string, quiet=False):
        if string:
            string = str(string)
            if OS.name == "windows":
                strings = string.split(newline2)
            elif OS.name in ["macos", "linux"]:
                strings = string.split(newline)
            return strings
        else:
            if not quiet:
                print("None can't be splitted")

    @classmethod
    def nl(cls, string):
        return cls.newlines_to_strings(string=string)

    @staticmethod
    def split_every(string, chars):
        chars = int(chars)
        output_lines = []
        char_exists = "."
        char_can_be_exists = ".?"
        regexp = char_exists + char_can_be_exists*(chars-1)
        for line in re.findall(regexp, str(string)):
            output_lines += [line]
        return output_lines

    @staticmethod
    def leftpad(string, leng, ch="0", rightpad=False):
        string = str(string)
        if len(string) >= leng:
            return string
        strOfCh = str(ch) * leng
        string_output = strOfCh[len(string):leng] + string
        if rightpad:  # добавление символов справа из аллиаса (rightpad) функции
            string_output = string + strOfCh[len(string):leng]
        return string_output

    @classmethod
    def rightpad(cls, string, leng, ch="0"):
        return cls.leftpad(string, leng, ch=ch, rightpad=True)

    @staticmethod
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

    @staticmethod
    def diff_simple(string_a, string_b):
        import difflib

        strings = [(string_a, string_b)]  # for furthurer support for unlimited srtings

        for a, b in strings:
            print('{} => {}'.format(a, b))
            for i, s in enumerate(difflib.ndiff(a, b)):
                if s[0] == ' ':
                    continue
                elif s[0] == '-':
                    print(u'Delete "{}" from position {}'.format(s[-1], i))
                elif s[0] == '+':
                    print(u'Add "{}" to position {}'.format(s[-1], i))
            print()


class Console():
    @staticmethod
    def clean():
        if OS.name == "windows":
            os.system("cls")
        elif OS.name in ["linux", "macos"]:
            print(newline * shutil.get_terminal_size().lines)

    @staticmethod
    def width():
        if OS.name == "windows":
            io = Console.get_output("mode con")
            width_ = Str.get_integers(io)[1]
        elif OS.name in ["linux", "macos"]:
            io = Console.get_output("stty size")
            width_ = Str.get_integers(io)[1]
        return int(width_)

    @staticmethod
    def height():
        if OS.name == "windows":
            modecon = Console.get_output("mode con")
            height = Str.get_integers(modecon)[0]
        elif OS.name in ["linux", "macos"]:
            sttysize = Console.get_output("stty size")
            height = Str.get_integers(sttysize)[0]
        if height > 100:
            height = 100
        return int(height)

    @classmethod
    def blink(cls, width=None, height=None, symbol="#", sleep=0.5):
        if width is not None and height is not None:
            os.system("mode con cols=" + str(width) + " lines=" + str(height))
        if width is None:
            width = cls.width()
        if height is None:
            height = cls.height()
        colorama.reinit()
        while True:
            colors = ["grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
            highlights = ["on_grey", "on_red", "on_green", "on_yellow", "on_blue", "on_magenta", "on_cyan", "on_white"]
            string = symbol * width
            color = random.choice(colors)
            colors.pop(colors.index(color))
            highlight = random.choice(highlights)
            try: # New version with one long line. Works perfect, as I see.
                string = string * height
                print(termcolor.colored(string, color, highlight))
                time.sleep(sleep)
            except KeyboardInterrupt as err:
                if OS.name == "windows":
                    print(termcolor.colored("OK", "white", "on_grey"))
                colorama.deinit()
                cls.clean()
                break

    @staticmethod
    def get_output(command, quiet=True, split_lines=False):
        p = subprocess.check_output(command, shell=True)
        output = p.decode("cp866")
        if split_lines:
            output = Str.nl(output)
        return output


class Path:
    @staticmethod
    def full(path):
        return os.path.abspath(path)

    @staticmethod
    def current(self=None):
        return os.path.dirname(os.path.realpath(__file__))

    @classmethod
    def extend(cls, *paths):
        for path_ in paths:
            try:
                path = os.path.join(str(path), str(path_))
            except NameError:
                if (OS.name == "windows") and path_ == backslash:  # support for smb windows paths like \\ip_or_pc\dir\
                    path = backslash * 2
                elif (OS.name == "windows") and (len(path_) <= 3):
                    path = os.path.join(path_, os.sep)
                elif OS.name == "windows":
                    path = path_
                elif OS.family == "unix":
                    if path_ == "..":
                        path = path_
                    elif path_ == ".":
                        path = path_
                    elif path_ == "~":
                        path = cls.home()
                    else:
                        path = os.path.join(os.sep, path_)
                else:
                    raise FileNotFoundError("path_" + str(path_) + "is not expected")

        return path

    @staticmethod
    def home():
        if OS.name == "windows":
            path = Console.get_output(r"echo %userprofile%")
            path = path.rstrip(newline2)
        else:
            path = Console.get_output("echo $HOME", split_lines = True)[0]
            path = path.rstrip(newline)
        return path

    @staticmethod
    def set_current(path):
        os.chdir(path)
        debug_print("os.getcwd()  # current directory is", os.getcwd())


class Locations:
    if OS.name == "windows":
        share = Path.extend("S:")
        shares = share

        scripts_folder = Path.extend("T:", "scripts")
        scripts_dir = scripts_folder

        documents_dir = Path.extend("C:", "Users", "Sklad_solvo")

        pycharm_projects = Path.extend(documents_dir, "PycharmProjects", "untitled")

        npp_exec = "notepad++.exe"
        npp_dir = Path.extend("C:", "Program Files", "Notepad++")
        npp = Path.extend(npp_dir, npp_exec)
        notepad_plus_plus = npp

        notepad = "notepad"

        py = "py"
        pyw = "pyw"
        python = Path.extend("C:", "Windows", "py.exe")

        wms2host = Path.extend(backslash, "192.168.99.7", "temp", "wms2host")
        host2wms = Path.extend(backslash, "192.168.99.7", "temp", "host2wms")

    else:
        share = Path.extend(Path.home(), "Desktop", "term")
        shares = share

        scripts_folder = Path.extend(share, "scripts")
        scripts_dir = scripts_folder

        pycharm_projects = Path.extend(Path.home(), "term", "untitled")

        npp = "atom"
        notepad_plus_plus = npp

        notepad = "open"

        py = "python3"
        pyw = "python3"


class Dir:
    @staticmethod
    def create(filename):
        if os.path.isfile(filename):
            directory = os.path.dirname(filename)
        else:
            directory = filename
        if not os.path.exists(directory):
            os.makedirs(directory)

    @staticmethod
    def current(self):
        return Path.current()

    @staticmethod
    def list_of_files(path):
        return os.listdir(path)

    @classmethod
    def contents(cls,path):
        return cls.list_of_files(path)

    @classmethod
    def contain(cls,path):
        return cls.contents(path)

    @staticmethod
    def number_of_files(path, quiet=False):
        try:
            dir_contents = Dir.contents(path)
            if not quiet:
                print(os.path.split(path)[1], "contain", len(dir_contents), "files")
            return len(dir_contents)
        except FileNotFoundError:
            if not quiet:
                print("Path", path, "isn't found")
            return None

    @classmethod
    def batch_rename(cls, directory, input_str, output_str, quiet=False):
        for filename in cls.contain(directory):
            if input_str in filename:
                final_name = filename.replace(input_str, output_str)
                File.rename(filename, final_name)
                if not quiet:
                    print(filename, "renamed to", final_name)

class File:
    @staticmethod
    def create(filename):
        filename = Path.full(filename)
        Dir.create(os.path.split(filename)[0])  # todo change it to just dir_create(filename)
        if not os.path.exists(filename):
            with open(filename, 'a'):  # open file and close after
                os.utime(filename, None)  # changes time of file modification
        if not os.path.exists(filename):
            raise FileNotFoundError("error while creating file " + filename +
                                    "try to repair script at " + Path.full(sys.argv[0]))

    @staticmethod
    def delete(path, quiet = False):
        # try:
        if os.path.isdir(path):
            raise IsADirectoryError(path + " is directory, use Dir.delete to delete")
        try:
            os.remove(path)
        except FileNotFoundError:
            if not quiet:
                print("file", path, "is not exist")
        if not quiet:
            print("file", path, "is deleted")
        # except PermissionError:
        #     try:
        #         if OS.name == "windows"
        #             delete_command = "del"
        #         else:
        #             delete_command = "rm"
        #         subprocess.call([delete_command, path])
        #     except:
        if os.path.exists(path):
            time.sleep(0.05)
            raise FileExistsError(path + " is not deleted")

    @staticmethod
    def move(input_file, output_file):
        shutil.move(input_file, output_file)

    @staticmethod
    def copy(input_file, output_file):
        shutil.copy2(input_file, output_file)

    @staticmethod
    def rename(input_file, output_file):
        File.move(input_file, output_file)

    @staticmethod
    def hide(filename, quiet=True):
        filename = Path.full(filename)  #
        if OS.name == "windows":
            win32api.SetFileAttributes(filename, win32con.FILE_ATTRIBUTE_HIDDEN)  # hiding file like windows do
        dotted_file = os.path.split(filename)  # split path to dir and path
        dotted_file = Path.extend(dotted_file[0], "." + dotted_file[1])  # merging it back and add dot
        File.rename(filename, dotted_file)
        if not quiet:
            print ("file", filename, "is hidden now")
        return dotted_file

    @staticmethod
    def backup(filename, subfolder="bak", quiet = False):
        filename = Path.full(filename) # normalize filename
        backupfilename = str(filename) + "." + Time.dotted() + ".bak"  # add dottedtime to backup filename
        backupfilename = os.path.split(backupfilename)  # splitting filename to folder and file
        try:  # if subfolder has no len
            if len(subfolder) < 1:  # if subfolder has non-zero len
                subfolder = "bak"  # set subfolder to default
                print("len(subfolder) < 1, so subfolder = 'bak'")  # print error
        except TypeError:  # if subfolder has no len
            subfolder = "bak"  # set subfolder to default
            print("len(subfolder) < 1, so subfolder = 'bak'")  # print error
        subfolder = Path.extend(backupfilename[0], subfolder)  # append subfolder name
        Dir.create(subfolder)  # create subfolder
        backupfilename = Path.extend(subfolder, backupfilename[1])  # backup file name full path
        shutil.copy2(filename, backupfilename)  # finally backup file
        backupfilename = File.hide(backupfilename)  # hiding file
        if not os.path.isfile(backupfilename):  # if file is not created
            raise FileNotFoundError(backupfilename + " isn't created while backup")
        if not quiet:  # if finction is not shutted up
            print("backup of file", filename, "created as", backupfilename) # all is ok, print that
        return backupfilename

    @staticmethod
    def wipe(path):
        file = open(path, 'w')
        file.close()

    @staticmethod
    def read(path):
        with open(path, "r") as f:
            return f.read()


class Time:
    @staticmethod
    def stamp():
        return time.time()

    @staticmethod
    def dotted():
        dateandtime = Time.get("year") + "." + Time.get("month", 2) + "." + \
                      Time.get("day", 2) + "_at_" + Time.get("hour", 2) + "." + \
                      Time.get("minute", 2) + "." + Time.get("second", 2) + "." + \
                      Time.get("microsecond", 6)
        return dateandtime

    @staticmethod
    def get(size, zfill=0):
        return Str.leftpad(eval("str(datetime.datetime.now()." + size + ")"), leng=zfill, ch=0)

    @staticmethod
    def rustime(customtime=None):
        if customtime:
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
        if OS.name == "linux":
            rustime = str(day) + "." + str(month) + "." + str(year) + "y at " \
        + str(hour) + ":" + str(minute) + ":" + str(second)
        return rustime

    @classmethod
    def sleep(cls, seconds):
        warning("Time.sleep now Time.timer")
        print("Sleep", seconds, "seconds...")
        cls.timer(seconds=seconds)

    @staticmethod
    def timer(seconds, check_per_sec=10):
        Countdown = Bench
        Countdown.start()
        secs_second_var = int(seconds)
        while Countdown.get() < seconds:
            time.sleep(1/check_per_sec)
            secs_left_int = int(seconds - Countdown.get())
            if secs_left_int != secs_second_var:
                secs_second_var = secs_left_int
                Print.rewrite("Timer for " + str(seconds) + " seconds. " + str(secs_left_int) + " left")
        Print.rewrite("")


class Json():
    @classmethod
    def check(cls, filename):
        try:
            cls.load(filename)
            return True
        except:  # any exception is False
            print("JSON is bad")
            return False

    @classmethod
    def save(cls, filename, jsonstring, quiet=False, debug=False):
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
            raise IOError("error while saving JSON, try to repair script at path " +
                          Path.full(sys.argv[0]))
        json_test_string = cls.load(filename, quiet=True)
        if jsonstring != json_test_string:
            raise IOError("error while saving JSON, try to repair script at path " +
                          Path.full(sys.argv[0]))

    @classmethod
    def load(cls, filename, quiet = False, debug=False):
        try:
            if not os.path.isfile(filename):
                File.create(filename)
                cleanjson = {}
                cls.save(filename, cleanjson)
            settingsJsonTextIO = open(filename)
            jsonStringInMemory = json.load(settingsJsonTextIO)
            settingsJsonTextIO.close()
            if not quiet:
                print("JSON format succesfull loaded")
            if debug:
                print(jsonStringInMemory)
            return jsonStringInMemory
        except:
            raise IOError("error while loading JSON, try to repair script at path " +
                          Path.full(sys.argv[0]))





class Process():
    @staticmethod
    def kill(process):
        if OS.name == "windows":
            command_ = "taskkill /f /im " + str(process) + ".exe"
            os.system(command_)
        if OS.name == "macos":
            command_ = "killall " + str(process)
            os.system(command_)
    @staticmethod
    def start(*arguments, new_window=False, debug=False, pureshell=False):
        if debug:
            debug_print("Process.start arguments", arguments)
        if new_window or pureshell:
            for argument_ in arguments:
                if " " in argument_ and argument_[:1] != "-":
                    if OS.name == "windows":
                        argument_ = Str.to_quotes(argument_)
                    else:
                        argument_ = Str.to_quotes_2(argument_)
                try:
                    command = command + " " + argument_
                except NameError:
                    if new_window:
                        if OS.name == "windows":
                            command = 'start "" ' + argument_
                        elif OS.name == "macos":
                            warning("macOS doesn't support creating new window now")
                            #command = "" +
                    else:
                        command = argument_
            os.system(command)
        else:
            if OS.name == "windows":
                commands = []
                for argument_ in arguments:
                    commands.append(str(argument_))
                subprocess.call(commands)
            elif OS.name == "macos":
                commands = ""
                for argument_ in arguments:
                    commands += argument_ + " "
                os.system(commands)



class Codegen:
    debug = False

    @classmethod
    def start(cls, file_path):
        File.wipe(file_path)
        cls.file = open(file_path, "wb")

    @classmethod
    def add_line(cls, code):
        cls.file.write(code.encode('utf8'))
        if cls.debug:
            print(code)

    @classmethod
    def end(cls, quiet=False):
        cls.file.close()

    shebang = "#! python3" + newline + \
              "# -*- coding: utf-8 -*-" + newline


def plog(logfile, logstring="some shit happened", customtime=None, quiet=False, backup=True):
    if not quiet:
        print(logstring)
    File.create(logfile)
    if backup:
        File.backup(logfile, quiet=True)
    file = open(logfile, "a")
    if customtime:
        file.write(Time.rustime(customtime) + " " + str(logstring) + newline)
    else:
        file.write(Time.rustime() + " " + str(logstring) + newline)
    file.close()


def ping(domain ="127.0.0.1", count=1, quiet=False, logfile=None, timeout=10000):
    # с таким эксепшном можно сделать куда проще это всё
    domain = getDomainOfUrl(domain)
    if not quiet:
        colorama.reinit()
        print("Pinging", domain, count, "times...")
        up_message = domain + " is up!"
        down_message = domain + " is down."
    try:
        if OS.name == "windows":
            count_arg = "n"
            timeout_arg = "w"
        if OS.name in ["macos", "linux"]:
            count_arg = "c"
            timeout_arg = "W"
        command = "ping " + domain + " -" + count_arg + " " + str(count) + \
                  " -" + timeout_arg + " " + str(timeout)
        ping_output = Console.get_output(command)
    except KeyboardInterrupt:
        sys.exit()
    except:  # any exception is not good ping
        ping_output = ""
    if ("TTL" in ping_output) or ("ttl" in ping_output):
        up = True
    else:
        up = False
    if logfile:
        if up:
            plog(logfile, domain + " is up!", quiet=True)
            cprint(up_message, "white", "on_green")
        else:
            plog(logfile, down_message, quiet=True)
            cprint(down_message, "white", "on_red")
    elif not quiet:
        if up:
            cprint(up_message, "white", "on_green")
        else:
            cprint(down_message, "white", "on_red")
        colorama.deinit()
    return up


def winRepair_UnicodeEncodeError(quiet=""):
    if quiet:
        quiet = " > null"
    os.system("chcp 65001" + quiet)
    os.system("set PYTHONIOENCODING = utf - 8")


def input_int(message="Введите число: ", minimum=None, maximum=None, default=None, quiet=False):
    output_int = "jabla fitta"
    if default:
        message = "(Enter = " + str(default) + ")"
    while output_int == "jabla fitta":  # цикл, пока не получит итоговое число
        integer = input(message)
        if integer != "":
            try:
                integer = Str.get_integers(integer)[0]
            except TypeError:
                print("Это не число")
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
    if not quiet:
        print("Итоговое число:", output_int)
    return output_int




def warning(message):

    pyautogui.alert(message)

def substring(string, before, after=None):
    warning(message="substring now in Str.substring!!!!!")
    return Str.substring(string, before, after=after)


def getDomainOfUrl(url):
    url_output = Str.substring(url, "://", "/")
    if url_output == "":
        url_output = Str.substring(url, "://")
    return url_output


class Bench:
    time_start = datetime.datetime.now()
    time_end = None
    previous = None

    @classmethod
    def start(cls):
        cls.time_start = datetime.datetime.now()

    @classmethod
    def get(cls):
        cls.time_end = datetime.datetime.now()
        delta = cls.time_end - cls.time_start
        delta_combined = delta.seconds + delta.microseconds / 1E6
        return delta_combined

    @classmethod
    def end(cls, quiet=False):
        delta_combined = cls.get()
        cls.previous = delta_combined
        if not quiet:
            cprint("Bench runned in " + str(delta_combined) + " seconds", "grey", "on_white")
        else:
            return delta_combined


class Tkinter():

    def color(red, green, blue):
        my_color = str('#%02x%02x%02x' % (red, green, blue))
        return my_color

    @staticmethod
    def warn():
        root = Tk()
        # root.after(300, lambda: root.focus_force())  # try to grab focus after 300ms

        root.wm_attributes("-topmost", 1)
        root.focus_force()

        def close_window():
            btn_close.name = None
            root.destroy()
        btn_close = Button(root, bg="red", text="...", padx=1000, pady=1000, command=close_window)
        btn_close.grid(row=0, column=0)
        mainloop()


class Windows:
    @staticmethod
    def lock():
        ctypes.windll.LockWorkStation()  # todo fix Windows 10


class Random:
    @staticmethod
    def integer(min=0, max=100):
        return random.randrange(min, max+1)


class Wget:
    @staticmethod
    def download(url, output):
        url = url.replace("&", backslash + "&")
        # onestring = "wget " + url + " -O " + output
        arguments = '--header="Accept: text/html" ' + \
                    '--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) ' + \
                    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3167.0 Safari/537.36"'
        Process.start("wget", url, "-O", output, arguments, pureshell=True)

        # Another way to fix blocks by creating ~/.wgetrc file https://stackoverflow.com/a/34166756

class Int:
    @staticmethod
    def from_to(start, end, to_str=False):
        roots = range(start, end + 1)
        if to_str:
            output = []
            max_len = max(len(str(start)), len(str(end)))
            for root in roots:
                output.append(Str.leftpad(root, max_len, 0))
            return output
        else:
            return roots


class Learning():
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


class Repl:
    def loop(safe=False):
        def main():
            while True:
                try:
                    command = input(">>")
                    exec (command)
                    exec("print(" + Str.substring(command, before = '', after=' ') + ")", globals())
                except KeyboardInterrupt:
                    break
                except SyntaxError as err:
                    print(err)
        if safe:
            try:
                main()
            except:
                pass
        else:
            main()


def screenblink(width = None, height = None, symbol = "#", sleep = 0.5):
    if width != None and height != None:
        os.system("mode con cols=" + str(width) + " lines=" + str(height))
    if width == None:
        width = Console.width()
    if height == None:
        height = Console.height()
    colorama.reinit()
    while True:
        colors = ["grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
        highlights = ["on_grey", "on_red", "on_green", "on_yellow", "on_blue", "on_magenta", "on_cyan", "on_white"]
        string = symbol * width
        color = random.choice(colors)
        colors.pop(colors.index(color))
        highlight = random.choice(highlights)
        try: # New version with one long line. Works perfect, as I see.
            string = string * height
            print(termcolor.colored(string, color, highlight))
            time.sleep(sleep)
        except KeyboardInterrupt as err:
            if get_os() == "windows":
                print (termcolor.colored("OK", "white", "on_grey"))
            colorama.deinit()
            Console.clean()
            break


if __name__ == "__main__":
    how_to_import_this_useless_stuff()
    Repl.loop()
    #File.backup(r"\\192.168.99.91\shares\scripts\utilsupdate\utils_dev.py")
    #print(rustime(1487646452.7141206))
    #ping(ip="192.168.99.91")
    #ping(ip="192.168.99.777")
    #screenblink()
    #print(checkWidthOfConsole())
    #print(checkHeightOfConsole())
    #import UtilsUpdate


colorama.reinit()
Bench.time_start = start_bench_no_bench
time_loading = Bench.end(quiet=True)
cprint("commands7 v" + __version__ + " loaded in " + str(time_loading) + " seconds", "grey", "on_white")

# Есть словарь: my_list = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]
# Сортировка словаря по одному ключу:
# my_list = sorted(my_list, key=lambda k: k['name'])
# Сортировка словаря по нескольким ключам:
# my_list = sorted(my_list, key=lambda x,y : cmp(x['name'], y['name']))
# или
# my_list.sort(lambda x,y : cmp(x['name'], y['name']))
