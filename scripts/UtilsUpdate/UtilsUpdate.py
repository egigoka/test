#! python3
from utils_dev import *
import os
import sys
#init
__version__ = "1.1.0"
scriptsFolder = path_extend("T:", "scripts")
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
        if ("__version__" in string) and ("=" in string):
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
    # return

paths = {}
paths["UtilsUpdate"] = {
        "dev_path": path_extend(home_path(), "term", "commands7.py"),
        "user_path": path_extend("T:", "scripts", "UtilsUpdate", "commands7.py"),
        "package_name": "commands7.py"}

paths["LaTeX_DrBx"] = {
        "dev_path": path_extend(home_path(), "term", "commands7.py"),
        "user_path": path_extend(home_path(), "term", "LaTeX", "commands7.py"),
        "package_name": "commands7.py"}
paths["LaTeX_DrBx_pycharm"] = {
        "dev_path": path_extend(home_path(), "term", "pycharm.py"),
        "user_path": path_extend(home_path(), "term", "LaTeX", "pycharm.py"),
        "package_name": "pycharm.py"}
paths["LaTeX_DrBx_fck"] = {
        "dev_path": path_extend(home_path(), "term", "fuck.bat"),
        "user_path": path_extend(home_path(), "term", "LaTeX", "fuck.bat"),
        "package_name": "fuck.bat"}
paths["LaTeX_DrBx_utilsupdate"] = {
        "dev_path": path_extend(home_path(), "term", "utilsupdate.bat"),
        "user_path": path_extend(home_path(), "term", "LaTeX", "utilsupdate.bat"),
        "package_name": "utilsupdate.bat"}

paths["BartenderPrint_c7"] = {
        "dev_path": path_extend(home_path(), "term", "commands7.py"),
        "user_path": path_extend("T:", "scripts", "BartenderPrint", "commands7.py"),
        "package_name": "commands7.py"}
paths["BartenderPrint_pycharm"] = {
        "dev_path": path_extend(home_path(), "term", "pycharm.py"),
        "user_path": path_extend("T:", "scripts", "BartenderPrint", "pycharm.py"),
        "package_name": "pycharm.py"}
paths["BartenderPrint_fck"] = {
        "dev_path": path_extend(home_path(), "term", "fuck.bat"),
        "user_path": path_extend("T:", "scripts", "BartenderPrint", "fuck.bat"),
        "package_name": "fuck.bat"}
paths["BartenderPrint_utilsupdate"] = {
        "dev_path": path_extend(home_path(), "term", "utilsupdate.bat"),
        "user_path": path_extend("T:", "scripts", "BartenderPrint", "utilsupdate.bat"),
        "package_name": "utilsupdate.bat"}

paths["Scripts in share"] = {
        "dev_path": path_extend(home_path(), "term", "commands7.py"),
        "user_path": path_extend("T:", "scripts", "commands7.py"),
        "package_name": "commands7.py"}
paths["Scripts in share mouse check"] = {
        "dev_path": path_extend(home_path(), "term", "untitled", "test27hookmouseclicks.py"),
        "user_path": path_extend("T:", "scripts", "test27hookmouseclicks.py"),
        "package_name": "test27hookmouseclicks.py"}

paths["Untitled PyCharm Project"] = {
        "dev_path": path_extend(home_path(), "term", "commands7.py"),
        "user_path": path_extend(home_path(), "term", "untitled", "commands7.py"),
        "package_name": "commands7.py"}

paths["Latex drb"] = {
        "dev_path": path_extend("T:", "scripts", "BartenderPrint", "print_l.py"),
        "user_path": path_extend(home_path(), "term", "LaTeX", "print.py"),
        "package_name": "print_l.py"}


paths["tripleclick in scripts"] = {
        "dev_path": path_extend(home_path(), "term", "tripleclick.py"),
        "user_path": path_extend("T:", "scripts", "tripleclick", "tripleclick.py"),
        "package_name": "tripleclick.py"}
paths["tripleclick in scripts c7"] = {
        "dev_path": path_extend(home_path(), "term", "commands7.py"),
        "user_path": path_extend("T:", "scripts", "tripleclick", "commands7.py"),
        "package_name": "commands7.py"}







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
    {"user_path": path_extend(home_path(), "term", "utils.py"),
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