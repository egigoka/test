#! python3
# -*- coding: utf-8 -*-
import datetime
start_bench_no_bench = datetime.datetime.now()
__version__ = "8.3.6.21-alpha"
# TODO for 9.0.0 release:
    # todo OS class vars not strings, but booleans
    # todo lazy load for all modules
    # todo docstrings everywhere
import os  # widely used
import sys  # used for check version of python for init or not win_unicode_console
sys.path.append(".")

FRACKING_classes_speed_tweaking = True

bench_no_bench_import_time = datetime.datetime.now()

# todo version diff
#   todo export script as json?
#   todo compare jsons?
#   todo save changes as commit message?

try:

    from bench8 import get_Bench

    if FRACKING_classes_speed_tweaking:
        LoadTimeBenchMark = get_Bench()
        LoadTimeBenchMark.time_start = start_bench_no_bench
        LoadTimeBenchMark.end("python libs imported in", quiet_if_zero=True)
        LoadTimeBenchMark.start()
        LoadTimeBenchMark.time_start = bench_no_bench_import_time
        LoadTimeBenchMark.end("func get_Bench loaded in", quiet_if_zero=True)
        LoadTimeBenchMark.start()

    from str8 import Str

    if FRACKING_classes_speed_tweaking:
        LoadTimeBenchMark.end("class Str loaded in", quiet_if_zero=True)  # python searching for that module in PATH
        LoadTimeBenchMark.start()

    from os8 import OS

    if FRACKING_classes_speed_tweaking:
        LoadTimeBenchMark.end("class OS loaded in", quiet_if_zero=True)
        LoadTimeBenchMark.start()

    from print8 import Print

    if FRACKING_classes_speed_tweaking:
        LoadTimeBenchMark.end("class Print loaded in", quiet_if_zero=True)
        LoadTimeBenchMark.start()

    class Internal:
        @staticmethod
        def dir_c(debug=False):  # d print all functionality of commands8
            first_func_after_class = 1

            cnt_of_all_def = 0
            cnt_of_commented_def = 0

            file_path = Path.extend(Path.commands8(), "commands8.py")
            file_pipe = File.read(file_path)
            file_lines = Str.nl(file_pipe)
            for line in file_lines:  # dir ignore
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
            if debug: Print.debug(cnt_of_all_def, cnt_of_commented_def)



        @staticmethod
        def rel(quiet=False):  # d reload commands8, if you use it not in REPL, activate quiet argument
          # d require additional line of code after reload if you import not entrie commands8
          # d you need manually add "from commands8 import *" to script/REPL
          # d if you import like "import commands8", additional line of code not needed
            import commands8, importlib
            commands8 = importlib.reload(commands8)
            del commands8
            string = "from commands8 import *"  # d you need to manually add this <<< string to code :(
            if not quiet:
                print('"'+string+'" copied to clipboard')
                import copypaste
                copypaste.copy(string)
                pass

    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.end("class Internal loaded in", quiet_if_zero=True)
    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.start()

    if OS.name == "windows":  # init some modules to proper work with windows console
        if sys.version_info < (3,6):
            import win_unicode_console
            win_unicode_console.init()
    import colorama
    colorama.init()

    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.end("imported all dependencies in", quiet_if_zero=True)
    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.start()

    from const8 import *

    from console8 import Console

    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.end("class Console loaded in", quiet_if_zero=True)
    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.start()

    class Ssh:
        @staticmethod
        def get_output(host, username, password, command, safe=False):  # return
          # d output from command, runned on SSH server. Support only
          # d username:password autorisation.
          # todo autorisation by key.
            if OS.python_implementation != "pypy":
                import paramiko
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


    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.end("class Ssh loaded in", quiet_if_zero=True)
    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.start()


    class Path:
        @staticmethod
        def full(path):
            return os.path.abspath(path)

        @staticmethod
        def commands8():
            return os.path.dirname(os.path.realpath(__file__))

        @staticmethod
        def working():
            return os.getcwd()

        @classmethod
        def extend(cls, *paths, debug=False):  # paths input strings of path pieces, return
          # d string with path, good for OS
            for path_part in paths:
                try:
                    path = os.path.join(str(path), str(path_part))
                except NameError:  # first path piece is very important
                    if OS.family == "": pass # fix
                    if (OS.name == "windows") and path_part == backslash:  # support for smb windows paths like \\ip_or_pc\dir\
                        path = backslash * 2
                    elif (OS.name == "windows") and (len(path_part) <= 3):
                        path = os.path.join(path_part, os.sep)
                    elif OS.name == "windows":
                        path = path_part
                        if debug: Print.debug("path", path, "path_part", path_part)
                    elif OS.family == "unix":
                        if path_part == "..":
                            path = path_part
                        elif path_part == ".":
                            path = path_part
                        elif path_part == "~":
                            path = cls.home()
                        else:
                            path = os.path.join(os.sep, path_part)
                    else:
                        raise FileNotFoundError("path_part" + str(path_part) + "is not expected")

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
        def commands8(): return Path.commands8()  # alias to Path.commands8

        @staticmethod
        def working(): return Path.working()  # alias to Path.working

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

    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.end("class Path loaded in", quiet_if_zero=True)
    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.start()

    class File:
        @staticmethod
        def create(filename):
            filename = Path.full(filename)
            if os.path.split(filename)[0] != "":
                Dir.create(os.path.split(filename)[0])
            if not File.exists(filename):
                with open(filename, 'a'):  # open file and close after
                    os.utime(filename, None)  # change time of file modification
            else:
                raise FileExistsError("file" + str(filename) + "exists")
            if not File.exists(filename):
                raise FileNotFoundError("error while creating file " + filename +
                                        "try to repair script at " + Path.full(sys.argv[0]))

        @staticmethod
        def delete(path, quiet=False):  # ...
            import time
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
            if File.exists(path):
                raise FileExistsError(path + " is not deleted")

        @staticmethod
        def move(input_file, output_file):  # ...
            import shutil
            shutil.move(input_file, output_file)

        @staticmethod
        def copy(input_file, output_file):  # ...
            import shutil
            shutil.copy2(input_file, output_file)

        @staticmethod
        def rename(input_file, output_file):  # ...
            File.move(input_file, output_file)

        @staticmethod
        def hide(filename, quiet=True):  # adding dot to filename and set attribute
          # d FILE_ATTRIBUTE_HIDDEN to file, if running on Windows
            filename = Path.full(filename)
            if OS.name == "windows":
                import win32api, win32con
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
            import shutil
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
        # import locale
        # locale.getpreferredencoding(False) # what is that?
        # locale.getpreferredencoding(False)
            with open(path, "r", encoding='utf-8') as f:
                return f.read()

        @staticmethod
        def write(filename, what_to_write, mode="ab"):  # write to end of file with default mode, you can change it to any
          # g that supported by python open() func
            with open(filename, mode=mode) as file:  # open file then closes it
                file.write(what_to_write.encode("utf-8"))

        @staticmethod
        def get_size(filename):  # return size in bytes
            return os.stat(filename).st_size

        @staticmethod
        def exists(filename):
            return os.path.exists(filename)

    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.end("class File loaded in", quiet_if_zero=True)
    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.start()

    from time8 import Time

    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.end("class Time loaded in", quiet_if_zero=True)
    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.start()

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
            import json
            try:
                File.wipe(filename)
                settingsJsonTextIO = open(filename, "w")
                json.dump(jsonstring, settingsJsonTextIO)
                settingsJsonTextIO.close()
                if not quiet:
                    print("JSON succesfull saved")
                if debug:
                    print("sys.argv[0] =",sys.argv[0])
                    print(jsonstring)
            except:
                raise IOError("error while saving JSON, try to repair script at path " +
                              Path.full(sys.argv[0]))
            json_test_string = cls.load(filename, quiet=True)
            if jsonstring != json_test_string:
                Print.debug("jsonstring_to_save", jsonstring, "json_test_string_from_file", json_test_string)
                raise IOError("error while saving JSON, try to repair script at path " +
                              Path.full(sys.argv[0]))  # exception

        @classmethod
        def load(cls, filename, quiet = False, debug=False):
            import json
            try:
                if not os.path.isfile(filename):
                    File.create(filename)
                    cleanjson = {}
                    cls.save(filename, cleanjson)
                settingsJsonTextIO = open(filename)
                jsonStringInMemory = json.load(settingsJsonTextIO)
                settingsJsonTextIO.close()
                if not quiet:
                    print("JSON succesfull loaded")
                if debug:
                    print(jsonStringInMemory)
                return jsonStringInMemory
            except:
                raise IOError("error while loading JSON, try to repair script at path " +
                              Path.full(sys.argv[0]))

    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.end("class Json loaded in", quiet_if_zero=True)
    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.start()

    from list8 import List

    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.end("class List loaded in", quiet_if_zero=True)
    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.start()

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
                    import subprocess
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

    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.end("class Process loaded in", quiet_if_zero=True)
    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.start()

    class Dict:
        @staticmethod
        def iterable(dict_):
            if not isinstance(dict_, dict):
                raise TypeError("There must be dict in input")
            return dict_.items()

        @staticmethod
        def sorted_by_key(dict, case_insensitive=False):
            if case_insensitive == True:
                output = {}
                for i in sorted(dict, key=str.lower):
                    output[i] = dict[i]
                return output
            else:
                import collections
                return collections.OrderedDict(sorted(dict.items()))

    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.end("class Dict loaded in", quiet_if_zero=True)
    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.start()

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

    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.end("class Codegen loaded in", quiet_if_zero=True)
    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.start()

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

    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.end("func plog loaded in", quiet_if_zero=True)
    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.start()

    class Network:
        @staticmethod
        def getDomainOfUrl(url):
            url_output = Str.substring(url, "://", "/")
            if url_output == "":
                url_output = Str.substring(url, "://")
            return url_output

        @staticmethod
        def dnslookup(domain):
            import socket
            try:
                return socket.gethostbyname(domain)  # I don't how it work todo check code of 'socket'
            except socket.gaierror:
                return "not found"

        @classmethod
        def ping(Network, domain ="127.0.0.1", count=1, quiet=False, logfile=None, timeout=10000, return_ip=False):
            # с таким эксепшном можно сделать куда проще это всё
            domain = Network.getDomainOfUrl(domain)
            backup_ping_output = ""
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
                try:
                    backup_ping_output = ping_output
                except UnboundLocalError:
                    backup_ping_output = ""
                ping_output = ""
            if ("TTL" in ping_output) or ("ttl" in ping_output):
                up = True
            else:
                up = False

            if logfile or (not quiet): import termcolor
            if logfile:
                if up:
                    plog(logfile, domain + " is up!", quiet=True)
                    termcolor.cprint(up_message, "white", "on_green")
                else:
                    plog(logfile, down_message, quiet=True)
                    termcolor.cprint(down_message, "white", "on_red")

            elif not quiet:
                Print.rewrite("")
                if up:
                    termcolor.cprint(up_message, "white", "on_green")
                else:
                    termcolor.cprint(down_message, "white", "on_red")
                colorama.deinit()
            ip = None
            if return_ip:
                try:
                    for line in Str.nl(ping_output+backup_ping_output):
                        if len(Str.get_integers(line)) >= 4:
                            octaves = Str.get_integers(line)
                            ip = str(octaves[0]) + "." + str(octaves[1]) + "." + str(octaves[2]) + "." + str(octaves[3])
                            break
                except TypeError:
                    pass
                if not ip:
                    ip = Network.dnslookup(domain)
                return up, ip, ping_output
            return up

    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.end("class Network loaded in", quiet_if_zero=True)
    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.start()

    class Fix:

        def winRepair_UnicodeEncodeError(quiet=""):
            if quiet:
                quiet = " > null"
            os.system("chcp 65001" + quiet)
            os.system("set PYTHONIOENCODING = utf - 8")


    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.end("class Fix loaded in", quiet_if_zero=True)
    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.start()

    class Bash:
        escapable_chars = [backslash]
        @classmethod
        def argument_escape(cls, argument):
            for char in cls.escapable_chars:
                argument = argument.replace(char, backslash+char)
            return Str.to_quotes(argument)

    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.end("class Bash loaded in", quiet_if_zero=True)
    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.start()

    if OS.name == "macos":
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

    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.end("class macOS loaded in", quiet_if_zero=True)
    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.start()

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

    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.end("class Gui loaded in", quiet_if_zero=True)
    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.start()

    class Tkinter():
        @staticmethod
        def color(red, green, blue):  # return string of color matching for use in
          # d Tkinter
            return str('#%02x%02x%02x' % (red, green, blue))

    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.end("class Tkinter loaded in", quiet_if_zero=True)
    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.start()

    if OS.name == "windows":
        class Windows:
            @staticmethod
            def lock():  # locking screen, work only on Windows < 10
                if OS.windows_version and (OS.windows_version != 10):
                    import ctypes
                    ctypes.windll.LockWorkStation()  # todo fix Windows 10
                else:
                    raise OSError("Locking work only on Windows < 10")

    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.end("class Windows loaded in", quiet_if_zero=True)
    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.start()



    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.end("class Random loaded in", quiet_if_zero=True)
    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.start()

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

    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.end("class Wget loaded in", quiet_if_zero=True)
    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.start()

    class Int:
        @staticmethod
        def from_to(start, end, to_str=False, list=False):  # return list of integers, if argument
          # g "to_str" activated, return list of strings with equal length
          # g if "list" arg activated, list will be returned, otherwise, it will be iterable obj
            if list: roots = range(start, end + 1)
            else: roots = xrange(start, end + 1)
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

    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.end("class Int loaded in", quiet_if_zero=True)
    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.start()

    class CLI():
        @staticmethod
        def get_y_n(question="", answer=None):
            def check_answer(string):
                if inputtt == "y":
                    return True
                if inputtt == "n":
                    return False
            if answer: check_answer(answer)
            while True:
                inputtt = input(str(question) + " (y/n)?")
                inputtt = inputtt.strip(" ")
                check_answer(inputtt)

        wait_update_pos = 0

        @classmethod
        def wait_update(CLI, quiet=False):
            if CLI.wait_update_pos == 0:
                stick = "|"
            elif CLI.wait_update_pos == 1:
                stick = "/"
            elif CLI.wait_update_pos == 2:
                stick = "-"
            elif CLI.wait_update_pos == 3:
                stick = "\ "[:1]
            elif CLI.wait_update_pos == 4:
                stick = "|"
            elif CLI.wait_update_pos == 5:
                stick = "/"
            elif CLI.wait_update_pos == 6:
                stick = "-"
            elif CLI.wait_update_pos == 7:
                stick = "\ "[:1]
                CLI.wait_update_pos = -1
            CLI.wait_update_pos += 1
            if not quiet:
                Print.rewrite(stick)
            else:
                return stick

        @staticmethod
        def progressbar(count, of):
            Console.width()

    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.end("class CLI loaded in", quiet_if_zero=True)
    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.start()

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

    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.end("class Repl loaded in", quiet_if_zero=True)
    if FRACKING_classes_speed_tweaking: LoadTimeBenchMark.start()

    try:
        colorama.reinit()
    except AttributeError:
        print("failed to init colorama, maybe problem with importing")
    LoadTimeBenchMark = get_Bench()
    LoadTimeBenchMark.time_start = start_bench_no_bench
    LoadTimeBenchMark.end("commands8 v" + __version__ + " loaded in")
except ModuleNotFoundError:
    import installreq8
    from print8 import Print
    Print.debug("I tried my best to install dependencies, try to restart script, everything must be okay")
