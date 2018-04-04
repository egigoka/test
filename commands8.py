#! python3
# -*- coding: utf-8 -*-
import datetime
start_bench_no_bench = datetime.datetime.now()
__version__ = "8.0.18-alpha"
import os
import sys
import copy
import platform
import pkgutil

# todo version diff
#   todo export script as json?
#   todo compare jsons?
#   todo save changes as commit message?

# this shit for pycharm:
colorama = None; cprint = None; copypaste = None; pyautogui = None; Tk = None; Button = None; mainloop = None; paramiko = None

def get_Bench(start=False):  # return class with those functions:
    class Bench(object):  # dir ignore
        time_start = datetime.datetime.now()
        time_end = None
        quiet = False  # d argument for disable print to terminal               bnl1
        prefix = "Bench runned in"  # d what have been done, will print if      bnl1
        # d "quiet" variable of class is False

        @classmethod
        def start(cls):  # set time of begin to now
            cls.time_start = datetime.datetime.now()

        @classmethod
        def get(cls):  # dir ignore
            cls.time_end = datetime.datetime.now()
            delta = cls.time_end - cls.time_start
            delta_combined = delta.seconds + delta.microseconds / 1E6
            return delta_combined

        @classmethod
        def end(cls):  # return delta between start and end
            delta_combined = cls.get()
            if not cls.quiet:
                try:
                    cprint(cls.prefix + " " + str(round(delta_combined, 2)) + " seconds", "grey", "on_white")
                except TypeError:
                    print(cls.prefix + " " + str(round(delta_combined, 2)) + " seconds")
            return delta_combined
    return Bench

class OS:
    is_python3 = sys.version_info >= (3, 0)  # d boolean
    python_implementation = None # d string with name of python implementation: "cpython" or "pypy"
    python_version_major = sys.version_info.major # d int of major python version
    python_commandline_version = ""
    if is_python3:
        python_commandline_version = "3" # d string of addable "3" to commandline apps if python is 3rd version
    family = None  # d string with family of OS: "nt" or "unix"
    name = None  # d string with name of OS: "windows", "linux", or "macos"
    windows_version = None  # d only on Windows, integer of major version of Windows
    display = None  # d didn't work yet
    cyrrilic_support = None  # d boolean variable of cyrrilic output support
    if sys.platform == "linux" or sys.platform == "linux2":
        name = "linux"
    elif sys.platform == "win32" or sys.platform == "cygwin":
        name = "windows"
        windows_version = sys.getwindowsversion().major
    elif sys.platform == "darwin":
        name = "macos"

    if platform.python_implementation == "PyPy":
        python_implementation = "pypy"
    else:
        python_implementation = "cpython"

    if name == "windows":
        family = "nt"
    elif name in ["macos", "linux"]:
        family = "unix"

    try:  # todo make this work!
        if name == "linux":
            from Xlib.display import Display
        display = True
    except ImportError:
        display = False
        print("Your system haven't display -_-")

    try:
        cyrline = "йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
        for cyrsybol in cyrline:
            print(cyrsybol*2, end="\r")
        print("  ", end="\r")
        cyrrilic_support = True
    except UnicodeEncodeError as err:
        cyrrilic_support = False
        # print (err)
        print ("Your system doesn't properly work with cyrrilic -_-")




class Internal:

    @staticmethod
    def mine_import(module_name, objects=None, justdownload=False, az=None):  # import
      # d module, if module not found, trying to install it by pip
        # check for pip module
        debug_Bench = get_Bench()
        debug_Bench.start()
        def just_install(module_name):
            import pip
            pip.main(['install', module_name])
        modules_list = []
        for item in pkgutil.iter_modules():
            modules_list.append(item[1])
        if "pip" not in modules_list:
            if OS.name == "linux":
                os.system("sudo apt-get install python" + OS.python_commandline_version + "-pip")
        if module_name not in modules_list:
            ###########RARE###########
            if module_name == "pyautogui":
                if OS.name == "linux":
                    if OS.is_python3:
                        os.system("apt-get install python-xlib")
                    else:
                        os.system("apt-get install python3-Xlib")
                if OS.name == "macos":
                    for package in ["python" + OS.python_commandline_version + "-xlib",
                                    "pyobjc-core", "pyobjc"]:
                        just_install(package)
                    if OS.python_implementation == "pypy":
                        Print.debug("Yep, PyPy doesn't support pyobjc")
            if module_name in ["win32api","win32con"]:
                just_install("pypiwin32")
            else:
            ###########RARE###########
                just_install(module_name)
        if not justdownload:
            if az and objects:
                if len(objects.split(",")) == 1:
                    globals()[az] = importlib.import_module(objects[0], package=module_name)
                print("Internal.mine_import doesn't support both attributes use 'az' and 'objects', so only 'objects' will apply.")
                az = None
            if az:
                import importlib
                globals()[az] = importlib.import_module(module_name)
            elif objects:
                # import importlib  # todo better code
                # for object in objects.split(",")
                #     globals()[object] = importlib.import_module(name, package=module_name):
                #### if " as " in object поделить и применить правильно, то есть имя назначить второе, а импортировать из первого
                exec("from " + module_name + " import " + objects, globals())
            else:
                import importlib
                globals()[module_name] = importlib.import_module(module_name)
        debug_Bench.prefix = module_name + " " + str(objects)
        debug_Bench.end()


    @staticmethod
    def dir_c():  # d print all functionality of commands8
        first_func_after_class = 1

        cnt_of_all_def = 0
        cnt_of_commented_def = 0

        for line in Str.nl(File.read(Path.extend(Path.current(), "commands8.py"))):  # dir ignore
            if "# dir ignore" not in line:  # dir ignore
                if "bnl" in line:  # dir ignore
                    print(newline*Str.get_integers(line)[-1], end="")  # dir ignore
                    line = line.replace("bnl"+str(Str.get_integers(line)[-1]),"")
                if "def " in line:  # dir ignore
                    print(newline*first_func_after_class + line)  # dir ignore
                    first_func_after_class = 1

                    cnt_of_all_def += 1
                    if "  # " in line: cnt_of_commented_def += 1

                elif ("class " in line) and (line[0:4] != "    "):  # dir ignore
                    first_func_after_class = 0
                    print(newline + line)  # dir ignore
                elif "# d " in line:  # dir ignore
                    print(line.replace("# d ", "# ", 1))  # dir ignore
        Print.debug(cnt_of_all_def, cnt_of_commented_def)



    @staticmethod
    def rel(quiet=False):  # d reload commands8, if you use it not in REPL, activate quiet argument
      # d require additional line of code after reload if you import not entrie commands8
      # d you need manually add "from commands8 import *" to script/REPL
      # d if you import like "import commands8", additional line of code not needed
        import commands8, importlib
        commands8 = importlib.reload(commands8)
        del commands8
        string = "from commands8 import *"  # you need to manually add this string to code :(
        if not quiet:
            print('"'+string+'" copied to clipboard')
            import copypaste
            copypaste.copy(string)
            pass


if OS.display:
    if OS.python_implementation != "pypy":
        if OS.name != "macos:":
            Internal.mine_import("pyautogui", justdownload=True)
        Internal.mine_import("paramiko", justdownload=True)
    Internal.mine_import("tkinter")  # from tkinter import *


import json, \
       shutil, \
       time, \
       random, \
       subprocess, \
       datetime, \
       re, \
       ctypes, \
       getpass





if OS.name == "windows":
    Internal.mine_import("win_unicode_console")
    Internal.mine_import("win32api")
    Internal.mine_import("win32con")
    Internal.mine_import("termcolor")
Internal.mine_import("colorama")
colorama.init()
colorama.deinit()
Internal.mine_import("termcolor", objects="colored, cprint")  # print_green_on_cyan = lambda x: cprint(x, 'green', 'on_cyan')
if OS.name == "windows":
    Internal.mine_import("pyperclip", az="copypaste")
else:
    Internal.mine_import("copypaste")


newline = '\n'  # d string with newline bnl3
ruble = u"\u20bd"  # d string with ₽ symbol
backslash = "\ "[:1]  # d string with backslash
newline2 = "\r\n"  # d string with other newline





class Print():
    @staticmethod
    def debug(*arguments, raw=False):  # d just more notable print, only for
      # d debugging
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
    def rewrite(*arguments, sep=" ", raw=False):  # d string, that can be rewritable
      # d note, that you need to rewrite string to remove characters

        line = " " * Console.width()
        if OS.name == "windows":
            line = line[:-1]
        print(line, end="\r")
        print(*arguments, sep=sep, end="\r")


class Str:
    @staticmethod
    def to_quotes(some_string):  # d just place input string inside "" quotes
        return '"' + str(some_string) + '"'

    @staticmethod
    def to_quotes_2(some_string):  # d place input string inside '' quotes
        return "'" + str(some_string) + "'"

    @staticmethod
    def get_integers(string):  # d return list of integers from string, !!!floating not supported!!!
      # todo add support for floating numbers, it will be cool!
        integer_found = False
        integers = []
        current_integer = 0
        negative = False
        for symbol in str(string) + " ":  # in exception some processing, meh :(
            try:
                if symbol in ['-', '—']:
                    negative = True
                    continue
                int(symbol)
                current_integer = current_integer*10 + int(symbol)
                integer_found = True
            except ValueError:
                if integer_found:
                    if negative:
                        current_integer = -current_integer
                    integers = integers + [current_integer]
                    current_integer = 0
                    integer_found = False
                negative = False
        return integers

    @staticmethod
    def newlines_to_strings(string, quiet=False):  # split long string with line
      # d breaks to separate strings in list
        if string:
            string = str(string)
            if OS.name == "windows":
                strings = string.split(newline2)
                if len(strings) == 1:
                    strings = strings[0].split(newline)
            elif OS.name in ["macos", "linux"]:
                strings = string.split(newline)
            return strings
        else:
            if not quiet:
                print("None can't be splitted")

    @classmethod
    def nl(cls, string):  # alias to newline
        return cls.newlines_to_strings(string=string)

    @staticmethod
    def split_every(string, chars):  # split string every
        chars = int(chars)
        output_lines = []
        char_exists = "."
        char_can_be_exists = ".?"
        regexp = char_exists + char_can_be_exists*(chars-1)
        for line in re.findall(regexp, str(string)):  # todo can I just return this list?
            output_lines += [line]
        return output_lines

    @staticmethod
    def leftpad(string, leng, ch="0", rightpad=False):  # d return string with
      # d added characters to left side. If string longer — return original string
        string = str(string)
        if len(string) >= leng:
            return string
        strOfCh = str(ch) * leng
        string_output = strOfCh[len(string):leng] + string
        if rightpad:
            string_output = string + strOfCh[len(string):leng]
        return string_output

    @classmethod
    def rightpad(cls, string, leng, ch="0"):  # return string with added
      # d characters to right side. If string longer — return original string
        return cls.leftpad(string, leng, ch=ch, rightpad=True)

    @staticmethod
    def substring(string, before, after=None):  # return string that between
      # d "before", and "after" strings, not including those.
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
    def diff_simple(string_a, string_b):  # d print all symbol differents.
      # d Not all mine code, must rewrite.
      # todo rewrite this shit.
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

    @staticmethod
    def input_pass(string="Password:"):  # d return string from user, securely
      # d inputed by getpass library
        return getpass.getpass(string)

    @staticmethod
    def input_int(message="Input integer: ", minimum=None, maximum=None, default=None, quiet=False):
      # d return integer from user with multible parameters.
        output_int = "jabla fitta"
        if default:
            message = "(Enter = " + str(default) + ")"
        while output_int == "jabla fitta":  # цикл, пока не получит итоговое число
            integer = input(message)
            if integer != "":
                try:
                    integer = Str.get_integers(integer)[0]
                except IndexError:
                    print("Это не число")
                    continue
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



class Console():
    @staticmethod
    def clean():  # wipe terminal output. Not tested on linux
      # todo test on linux
        if OS.name == "windows":
            os.system("cls")
        elif OS.name == "linux":
            print(newline * shutil.get_terminal_size().lines)
        elif OS.name == "macos":
            os.system(r"clear && printf '\e[3J'")

    @staticmethod
    def width():  # return width of terminal window in characters
        if OS.name == "windows":
            io = Console.get_output("mode con")
            width_ = Str.get_integers(io)[1]
        elif OS.name in ["linux", "macos"]:
            io = Console.get_output("stty size")
            width_ = Str.get_integers(io)[1]
        return int(width_)

    @staticmethod
    def height():  # return height of terminal window in characters
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
      # d fastly print to terminal characters with random color. Completely shit.
      # d arguments width and height changing size of terminal, works only in
      # d Windows.
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
                print(termcolor.colored("OK", "white", "on_grey"))
                colorama.deinit()
                cls.clean()
                break


    @staticmethod
    def get_output(command, quiet=True, split_lines=False):  # d return output
      # d of executing command. Doesn't output it to terminal in realtime.
      # d can be output after done if "quiet" argument activated.
        p = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        if OS.name == "windows":
            output = p.decode("cp866")
        elif OS.family == "unix":
            output = p.decode("utf8")
        if split_lines:
            output = Str.nl(output)
        return output



class Ssh:
    @staticmethod
    def get_output(host, username, password, command, safe=False):  # return
      # d output from command, runned on SSH server. Support only
      # d username:password autorisation.
      # todo autorisation by key.
        if OS.python_implementation != "pypy":
            Internal.mine_import("paramiko")
        else:
            raise OSError("paramiko doesn't supported by PyPy")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # automatically add unknown hosts
        ssh.connect(host, username=username, password=password)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("uptime")
        if (ssh_stderr.read() != b'') and not safe:
            raise IOError("ssh_stderr = " + str(ssh_stderr))
        ssh.close()
        return str(ssh_stdout.read(), 'utf8')

    @classmethod
    def get_avg_load_lin(cls, host, username, password, safe=False):  # return
      # d list of average loads from SSH linux server. Shit, I know
        output = cls.get_output(host=host, username=username, password=password, command="uprime", safe=safe)
        output = Str.substring(output, before="load average: ", after=newline)
        output = output.split(", ")
        return output

    @classmethod
    def get_uptime_lin(cls, host, username, password, safe=False):  # return
      # d string with uptime of SSH linux server. As I said before... :(
        output = cls.get_output(host=host, username=username, password=password, command="uprime", safe=safe)
        output = Str.substring(output, before=" up ", after=", ")
        return output





class Path:
    @staticmethod
    def full(path):
        return os.path.abspath(path)

    @staticmethod
    def current():
        return os.path.dirname(os.path.realpath(__file__))

    @classmethod
    def extend(cls, *paths):  # paths input strings of path pieces, return
      # d string with path, good for OS
        for path_ in paths:
            try:
                path = os.path.join(str(path), str(path_))
            except NameError:  # first path piece is very important
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
    def home():  # return path of home directory of current user. Not tested in
      # d linux.
      # todo test in lunux!
        if OS.name == "windows":
            path = Console.get_output(r"echo %userprofile%")
            path = path.rstrip(newline2)
        else:
            path = Console.get_output("echo $HOME", split_lines=True)[0]
            path = path.rstrip(newline)
        return path

    @staticmethod
    def set_current(path, quiet=True):  # changes current working directory.
      # d If quiet is disabled, prints directory.
        os.chdir(path)
        if not quiet:
            Print.debug("os.getcwd()  # current directory is", os.getcwd())


class Locations:
    if OS.name == "windows":  # d ...
        texteditor = "notepad"  # d notepad is in every version of Windows, yea?
        py = "py"
        pyw = "pyw"
    elif OS.name == "macos":  # d ...
        texteditor = "open"  # d just open default program for file
        py = "python3"
        pyw = "python3"
    elif OS.name == "linux":  # d ...
        texteditor = "nano"  # d nano is everywhere, I suppose? ]-:
        py = "python3"
        pyw = "python3"

class Dir:
    @staticmethod
    def create(filename):  # create dir if didn't exist
        if not os.path.exists(filename):
            os.makedirs(filename)

    @staticmethod
    def current(self):  # alias to Path.current
        return Path.current()

    @staticmethod
    def list_of_files(path):  # return list of files in folder
        return os.listdir(path)

    @staticmethod
    def number_of_files(path, quiet=False):  # return integer of number of files
      # d in directory
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
        if os.path.split(filename)[0] != "":
            Dir.create(os.path.split(filename)[0])
        if not os.path.exists(filename):
            with open(filename, 'a'):  # open file and close after
                os.utime(filename, None)  # changes time of file modification
        if not os.path.exists(filename):
            raise FileNotFoundError("error while creating file " + filename +
                                    "try to repair script at " + Path.full(sys.argv[0]))

    @staticmethod
    def delete(path, quiet=False):  # ...
        if os.path.isdir(path):
            raise IsADirectoryError(path + " is directory, use Dir.delete to delete")
        try:
            os.remove(path)
        except FileNotFoundError:
            if not quiet:
                print("file", path, "is not exist")
        if not quiet:
            print("file", path, "is deleted")
        time.sleep(0.05)
        if os.path.exists(path):
            raise FileExistsError(path + " is not deleted")

    @staticmethod
    def move(input_file, output_file):  # ...
        shutil.move(input_file, output_file)

    @staticmethod
    def copy(input_file, output_file):  # ...
        shutil.copy2(input_file, output_file)

    @staticmethod
    def rename(input_file, output_file):  # ...
        File.move(input_file, output_file)

    @staticmethod
    def hide(filename, quiet=True):  # adding dot to filename and set attribute
      # d FILE_ATTRIBUTE_HIDDEN to file, if running on Windows
        filename = Path.full(filename)
        if OS.name == "windows":
            win32api.SetFileAttributes(filename, win32con.FILE_ATTRIBUTE_HIDDEN)  # hiding file like windows do
        dotted_file = Path.extend(os.path.split(filename)[0], "." + os.path.split(filename)[1])  # adding dot
        File.rename(filename, dotted_file)
        if not quiet:
            print ("file", filename, "is hidden now")
        return dotted_file

    @classmethod
    def backup(cls, filename, subfolder="bak", hide=True, quiet = False):
      # d move file to subfolder, adds sort of timestamp to filename and hide
      # d file if necessary
        filename = Path.full(filename) # normalize filename
        backupfilename = str(filename) + "." + Time.dotted() + ".bak"  # add dottedtime to backup filename
        backupfilename = os.path.split(backupfilename)  # splitting filename to folder and file
        try:  # if subfolder has no len
            if len(subfolder) < 1:  # if subfolder has zero len
                raise TypeError("subfolder must have non-zero len")
        except TypeError:  # if subfolder has no len
            subfolder = "bak"  # set subfolder to default
            print("len(subfolder) < 1, so subfolder = 'bak'")  # print error
        subfolder = Path.extend(backupfilename[0], subfolder)  # append subfolder name
        Dir.create(subfolder)  # create subfolder
        backupfilename = Path.extend(subfolder, backupfilename[1])  # backup file name full path
        shutil.copy2(filename, backupfilename)  # finally backup file
        if hide:
            backupfilename = cls.hide(backupfilename)  # hiding file
        if not os.path.isfile(backupfilename):  # if file is not created
            raise FileNotFoundError(backupfilename + " isn't created while backup")
        if not quiet:  # if finction is not shutted up
            print("backup of file", filename, "created as", backupfilename) # all is ok, print that
        return backupfilename

    @staticmethod
    def wipe(path):  # clean content of file
        file = open(path, 'w')
        file.close()

    @staticmethod
    def read(path):  # return pipe to file content
        with open(path, "r") as f:
            return f.read()


class Time:

    rnd = str(random.randint(1,100))

    @classmethod
    def fuck(cls):
        print("fuck it all "+cls.rnd)

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
        if not OS.cyrrilic_support:
            rustime = str(day) + "." + str(month) + "." + str(year) + "y at " \
        + str(hour) + ":" + str(minute) + ":" + str(second)
        return rustime

    @staticmethod
    def timer(seconds, check_per_sec=10):
        Countdown = get_Bench()
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
            File.create(filename)
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



class List:
    @staticmethod
    def flatterize(input_list):
        if not ((isinstance(input_list,list)) or (isinstance(input_list,tuple))):
            raise TypeError("object of type '"+str(type(input_list))+"' can't be flatterized")
        output_list = copy.deepcopy(list(input_list))
        cnt = 0
        for object in output_list:
            if not isinstance(object, (str,int)):
                output_list.pop(cnt)
                for item in reversed(object):
                    output_list.insert(cnt, item)
            cnt+=1
        return output_list



class Process():
    @staticmethod
    def kill(process):
        if OS.name == "windows":
            command_ = "taskkill /f /im " + str(process) + ".exe"
            try:
                int(process)
                command_ = "taskkill /f /pid " + str(process)
            except:
                pass
        elif OS.name == "macos":
            command_ = "killall " + str(process)
            try:
                int(process)
                command_ = "kill " + str(process)
            except:
                pass
        else:
            Gui.warning("OS " + str(OS.name) + " not supported")
        os.system(command_)
    @staticmethod
    def start(*arguments, new_window=False, debug=False, pureshell=False):
        arguments = List.flatterize(arguments)
        if debug:
            Print.debug("Process.start arguments", arguments)
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
                            Gui.warning("macOS doesn't support creating new window now")
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
                    commands += str(argument_) + " "
                # print(commands)
                os.system(commands)



class Dict:
    @staticmethod
    def iterable(dict):
        return dict.items()


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


class Network:
    @staticmethod
    def getDomainOfUrl(url):
        url_output = Str.substring(url, "://", "/")
        if url_output == "":
            url_output = Str.substring(url, "://")
        return url_output

    @classmethod
    def ping(Network, domain ="127.0.0.1", count=1, quiet=False, logfile=None, timeout=10000):
        # с таким эксепшном можно сделать куда проще это всё
        domain = Network.getDomainOfUrl(domain)
        if not quiet:
            colorama.reinit()
            Print.rewrite("Pinging", domain, count, "times...")
            up_message = domain + " is up!"
            down_message = domain + " is down."
        try:
            if OS.name == "windows":
                count_arg = "n"
                timeout_arg = "w"
            if OS.name in ["macos", "linux"]:
                count_arg = "c"
                timeout_arg = "W"
            if OS.name == "linux":
                timeout = int(timeout/1000)
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
            Print.rewrite("")
            if up:
                cprint(up_message, "white", "on_green")
            else:
                cprint(down_message, "white", "on_red")
            colorama.deinit()
        return up


class Fix:

    def winRepair_UnicodeEncodeError(quiet=""):
        if quiet:
            quiet = " > null"
        os.system("chcp 65001" + quiet)
        os.system("set PYTHONIOENCODING = utf - 8")





class Bash:
    escapable_chars = [backslash]
    @classmethod
    def argument_escape(cls, argument):
        for char in cls.escapable_chars:
            argument = argument.replace(char, backslash+char)
        return Str.to_quotes(argument)


class macOS:

    class osascript:
        @staticmethod
        def quotes_escape(string):
            quote_1 = '"'
            #quote_2 = "'"
            # if there any already escaped symbols:
            string = string.replace(backslash, backslash*3)  # if there any other escaped symbols except quotes
            string = string.replace(backslash*3+quote_1, backslash*2+quote_1)  # removing one backslash, because it will added furthurer
            #string = string.replace(backslash*3+quote_2, backslash*2+quote_2)

            # usual quotes escape
            escaped_1 = backslash + quote_1
            #escaped_2 = backslash + quote_2
            string = string.replace(quote_1,escaped_1)
            #string = string.replace(quote_2, escaped_2)
            return string

    @classmethod
    def notification(cls, message, title="python3", subtitle=None, sound=None, list_of_sounds=False):
        # https://apple.stackexchange.com/questions/57412/how-can-i-trigger-a-notification-center-notification-from-an-applescript-or-shel# - just applescript
        # better realizations:
        # advanced commandline tool - https://github.com/vjeantet/alerter
        # simpler commandline tool - https://github.com/vjeantet/alerter
        # commands = "display notification \"message\" with title \"title\" subtitle \"subtitle\" sound name \"Sosumi\""
        commands = "display notification " + Str.to_quotes(cls.osascript.quotes_escape(message))
        if title or subtitle:
            commands += " with "
            if title:
                commands += "title " + Str.to_quotes(cls.osascript.quotes_escape(title)) + " "
            if subtitle:
                commands += "subtitle " + Str.to_quotes(cls.osascript.quotes_escape(subtitle)) + " "
        if sound:
            commands += " sound name " + Str.to_quotes(cls.osascript.quotes_escape(sound))
        commands = cls.osascript.quotes_escape(commands)  # escaping quotes:
        commands = Str.to_quotes(commands)  # applescript to quotes
        Process.start("osascript", "-e", commands)  # f start(*arguments, new_window=False, debug=False, pureshell=False):
        if list_of_sounds:
            Print.debug("global sounds", Dir.list_of_files(Path.extend("System", "Library", "Sounds")), "local sounds", Dir.list_of_files(Path.extend("~", "Library", "Sounds")))

class Gui:
    def warning(message):
        try:
            try:
                sys.ps1
                sys.ps2
                interactive_mode = True
            except:
                interactive_mode = False
            Print.debug("interactive_mode", interactive_mode)
            try:
                not_dot_py = sys.argv[0][-3] != ".py"  # todo check logic
            except:
                not_dot_py = True
            
            if (not_dot_py or (sys.argv[0] != "")) and (not interactive_mode):
                Print.debug("sys.argv", sys.argv)
                Print.debug("Something wrong with sys.argv. Tkinter doesn't like it.")
                input()
        except IndexError:
            Print.debug("sys.argv", sys.argv)
            raise RuntimeError ("Something wrong with sys.argv. Tkinter doesn't like it.")
        if OS.name == 'macos':
            macOS.notification(message)
        if OS.name != "macos" and OS.python_implementation != "pypy":
            Internal.mine_import("pyautogui")
            pyautogui.alert(message)
        else:
            Print.debug("PyPy doesn't support pyautogui, so warning is here:", warning)
            input("Press Enter to continue")









class Tkinter():
    @staticmethod
    def color(red, green, blue):  # return string of color matching for use in
      # d Tkinter
        return str('#%02x%02x%02x' % (red, green, blue))




class Windows:
    @staticmethod
    def lock():  # locking screen, work only on Windows < 10
        if OS.windows_version and (OS.windows_version != 10):
            ctypes.windll.LockWorkStation()  # todo fix Windows 10
        else:
            raise OSError("Locking work only on Windows < 10")


class Random:
    @staticmethod
    def integer(min, max):  # return random integer
        return random.randrange(min, max+1)

    @staticmethod
    def float(min, max):  # return random floating number
        return random.uniform(min, max)


class Wget:
    @staticmethod
    def download(url, output, quiet=False):  # just wrapper for commandline wget
        arguments = '--header="Accept: text/html" ' + \
                    '--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) ' + \
                    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3167.0 Safari/537.36"'
        if quiet:
            command = "wget '" + url + "' -O " + output + " " + arguments
            return Console.get_output(command)
        else:
            url = url.replace("&", backslash + "&")
            Process.start("wget", url, "-O", output, arguments, pureshell=True)


        # Another way to fix blocks by creating ~/.wgetrc file https://stackoverflow.com/a/34166756

class Int:
    @staticmethod
    def from_to(start, end, to_str=False):  # return list of integers, if argument
      # g "to_str" activated, return list of strings with equal length
        roots = range(start, end + 1)
        if to_str:
            output = []
            max_len = max(len(str(start)), len(str(end)))
            for root in roots:
                if root < 0:
                    output.append("-" + Str.leftpad(-root, max_len-1, 0))
                else:
                    output.append(Str.leftpad(root, max_len, 0))
            return output
        else:
            return roots




class Repl:
    @staticmethod
    def loop(safe=False):  # mine shitty implementation of REPL
        def main():  # dir ignore
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


colorama.reinit()
LoadTimeBenchMark = get_Bench()
LoadTimeBenchMark.time_start = start_bench_no_bench
LoadTimeBenchMark.prefix = "commands8 v" + __version__ + " loaded in"
LoadTimeBenchMark.end()

#if __name__ == "__main__":
#    Internal.dir_c()
#    Repl.loop()
