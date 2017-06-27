#! python3
from utils_dev import *
import os
import sys
#init
__version__ = "1.1.0"
scriptsFolder = path_extend("S:", "scripts")
scriptsSubFolderName = "UtilsUpdate"
utils_devName = "utils_dev.py"
utils_devPath = path_extend(scriptsFolder, scriptsSubFolderName, utils_devName)
codegen_devName = "codegen_dev.py"
codegen_devPath = path_extend(scriptsFolder, scriptsSubFolderName, codegen_devName)

def check_version(utils_py_file):
    try:
        file = open(utils_py_file, encoding='utf-8')
    except PermissionError:
        print("utils_py_file =", utils_py_file)
        file_delete(path=utils_py_file, quiet=True)
        check_update(name=utils_py_file, path=path)
    for string in file:
        if "__version__" in string:
            version = substring(string, "=")
            if "\n" in version:
                version = version.rstrip("\n")
            version = substring(version, "'", "'")
            version = substring(version, '"', '"')
            isDevVersion = False
            if "d" in version:
               isDevVersion = True
            if "\n" in version:
                version = version.rstrip("\n")
    try:
        version
    except:
        version = "0.0.0"
        isDevVersion = False
    return version, isDevVersion


def check_update(user_path, dev_path, package_name, user_package_name): # todo add dev path, add name of package
    newest_version = check_version(dev_path)
    checking_version = check_version(user_path)
    print("Found", package_name, str(checking_version) + " in " + str(user_package_name) + ", actual is " + str(newest_version))
    if (newest_version[1] == False) & (newest_version != checking_version):
        file_backup(user_path, quiet=True)
        os.system("copy " + dev_path + " " + user_path)
    elif newest_version[1]: #isDevVersion == True
        os.system(utils_devPath)
        sys.exit()
    # todo WARNING UPPER VERSION
    #return

paths = {}
paths["UtilsUpdate"] = \
    {"user_path": path_extend("S:", "scripts", "UtilsUpdate", "utils_dev.py"),
    "dev_path": path_extend(home_path(), "Dropbox", "term", "utils_dev.py"),
    "package_name": "utils_dev.py"}
paths["SolvoUnload"] = \
    {"user_path": path_extend(scriptsFolder, "SolvoUnload", "utils.py"),
    "dev_path": utils_devPath,
    "package_name": "utils.py"}
paths["SolvoUnload_"] = \
    {"user_path": path_extend(scriptsFolder, "SolvoUnload", "codegen.py"),
    "dev_path": codegen_devPath,
    "package_name": "codegen.py"}
paths["BartenderPrint"] = \
    {"user_path": path_extend(scriptsFolder, "BartenderPrint", "utils.py"),
    "dev_path": utils_devPath,
    "package_name": "utils.py"}
paths["HomeDirctory"] = \
    {"user_path": path_extend(home_path(), "Dropbox", "term", "utils.py"),
    "dev_path": utils_devPath,
    "package_name": "utils.py"}
paths["Series"] = \
    {"user_path": path_extend(scriptsFolder, "Series", "utils.py"),
    "dev_path": utils_devPath,
    "package_name": "utils.py"}
paths["PyCharm project untitled"] = \
    {"user_path": path_extend("C:", "Users", "Sklad_solvo", "PycharmProjects", "untitled", "utils.py"),
    "dev_path": utils_devPath,
    "package_name": "utils.py"}
paths["autoshutdown"] = \
    {"user_path": path_extend(scriptsFolder, "autoshutdown", "utils.py"),
    "dev_path": utils_devPath,
    "package_name": "utils.py"}
paths["BarsPrint"] = \
    {"user_path": path_extend(scriptsFolder, "BarsPrint", "utils.py"),
    "dev_path": utils_devPath,
    "package_name": "utils.py"}
paths["EQueue"] = \
    {"user_path": path_extend(scriptsFolder, "EQueue", "utils.py"),
    "dev_path": utils_devPath,
    "package_name": "utils.py"}


#print(paths)
for name in paths:
    # command = "explorer " + in_quotes(os.path.split(paths[name])[0])
    # print(command)
    # os.system(command)
    user_path = paths[name]["user_path"]
    dev_path = paths[name]["dev_path"]
    package_name = paths[name]["package_name"]
    user_package_name = name
    file_create(user_path)
    check_update(user_path, dev_path, package_name, user_package_name)