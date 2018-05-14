#! python3
# -*- coding: utf-8 -*-
# http://python.su/forum/topic/15531/?page=1#post-93316
import pkgutil
import sys
from pip8 import Pip
from bench8 import get_Bench
from os8 import OS

FRACKING_Internal_mine_import_speed_tweaking = True

def mine_import(module_name, objects=None, justdownload=False, az=None):  # import
  # d module, if module not found, trying to install it by pip
    #return
    if FRACKING_Internal_mine_import_speed_tweaking: debug_Bench = get_Bench()
    if FRACKING_Internal_mine_import_speed_tweaking: debug_Bench.start()
    Pip.check_pip_installation()
    if module_name not in Pip.list_of_modules:
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
                    Pip.install(package)
                if OS.python_implementation == "pypy":
                    Print.debug("Yep, PyPy doesn't support pyobjc")
        if module_name in ["win32api","win32con"]:
            Pip.install("pypiwin32")
        else:
        ###########RARE###########
            Pip.install(module_name)
    if not justdownload:
        def import_error():
            import_fail_arg = "--import-fail"
            if import_fail_arg in sys.argv:
                print('<<<<<<<<<<Some errors occured with importing "' + str(module_name) + '", re-run script doesnt help, sorry about that>>>>>>>>>>')
                print('<<<<<<<<<<Trying to work without "' + str(module_name) + '">>>>>>>>>>')
            else:
                commands = ""
                sys.argv.append(import_fail_arg)
                for arg in sys.argv:
                    commands += arg + " "
                commands = commands.rstrip(" ")
                print('<<<<<<<<<<Some errors occured with importing "' + str(module_name) + '", trying to re-run script with parameters "' + commands + '">>>>>>>>>>')
                os.system(commands)
                sys.exit()
        try:
            if az and objects:
                if len(objects.split(",")) == 1:
                    globals()[az] = importlib.import_module(objects[0], package=module_name)
                print("mine_import doesn't support both attributes use 'az' and 'objects', so only 'objects' will apply.")
                az = None
            if az:
                import importlib
                try:
                    globals()[az] = importlib.import_module(module_name)
                except ImportError as err:  # support for py3.4
                    print(err)
                    print("trying to import " + module_name + " in another way")
                    exec ("import " + module_name + " as " + az, globals())
                except ModuleNotFoundError as err:
                    print(err)
                    print("trying to import " + module_name + " in another way")
                    exec ("import " + module_name + " as " + az, globals())
            elif objects:
                # import importlib  # todo better code
                # for object in objects.split(",")
                #     globals()[object] = importlib.import_module(name, package=module_name):
                #### if " as " in object поделить и применить правильно, то есть имя назначить второе, а импортировать из первого
                exec("from " + module_name + " import " + objects, globals())
            else:
                import importlib
                try:
                    globals()[module_name] = importlib.import_module(module_name)
                except ImportError as err:  # support for py3.4
                    print(err)
                    print("trying to import " + module_name + " in another way")
                    exec ("import " + module_name, globals())
                except ModuleNotFoundError as err:
                    print(err)
                    print("trying to import " + module_name + " in another way")
                    exec ("import " + module_name, globals())
        except ImportError as err:  # support for py3.4
            import_error()
        except ModuleNotFoundError:
            import_error()


mine_import("termcolor", objects="colored, cprint")  # print_green_on_cyan = lambda x: cprint(x, 'green', 'on_cyan')
if OS.name == "windows":
    mine_import("pyperclip", az="copypaste")
else:
    mine_import("copypaste")
if OS.display:
    if OS.python_implementation != "pypy":
        if OS.name != "macos:":
            mine_import("pyautogui", justdownload=True)
        mine_import("paramiko", justdownload=True)
    import tkinter
if OS.name == "windows":
    if sys.version_info < (3,6):
        mine_import("win_unicode_console")
    mine_import("win32api")
    mine_import("win32con")
    mine_import("termcolor")
mine_import("colorama")
