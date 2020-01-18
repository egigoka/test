import os
import time
from commands import *

dct = {}
create_logstring = "Init check"
Print.colored("Init...", "grey", "on_white")

while True:
    for root, dirs, files in os.walk(Path.extend("Users", "mac", "Library", "Application Support", "Disk-O")):
        time9.sleep(0.001)
        for file in files:
                path = Path.extend(root, file)
                #print(path1)
                #print(dct)
                try:
                    if dct[path] != File.get_size(path):
                        dct[path] = File.get_size(path)
                        Print.colored(Time.dotted(), "Changed", os.path.split(path)[1], "yellow")
                except FileNotFoundError:
                    Print.colored(Time.dotted(), "Removed", os.path.split(path)[1], "red")
                    dct.pop(path, None)
                except KeyError as err:
                    try:
                        dct[path] = File.get_size(path)
                        Print.colored(Time.dotted(), create_logstring, os.path.split(path)[1], "green")
                    except FileNotFoundError:
                        #Print.colored("file not found", path1)
                        Print.rewrite(Time.dotted(), "Skip non-file", path)
                        pass
    create_logstring = "Created"

    for path, size in Dict.iterable(dct, copy_dict=True):
        time9.sleep(0.001)
        try:
            #Print.debug("dct[path1]", dct[path1],
            #            "File.get_size(path1)", File.get_size(path1),
            #            "dct[path1] != File.get_size(path1)", dct[path1] != File.get_size(path1))

            if dct[path] != File.get_size(path):
                dct[path] = File.get_size(path)
                Print.colored(Time.dotted(), "Changed", os.path.split(path)[1], "yellow")
        except FileNotFoundError:
            Print.colored(Time.dotted(), "Removed", os.path.split(path)[1], "red")
            dct.pop(path, None)
        except KeyError as err:
            Print.colored(Time.dotted(), "Created", os.path.split(path)[1], "green")
            dct[path] = File.get_size(path)

    CLI.wait_update()
    time9.sleep(2)
