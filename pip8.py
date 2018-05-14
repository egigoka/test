#! python3
# -*- coding: utf-8 -*-
# http://python.su/forum/topic/15531/?page=1#post-93316
from os8 import OS
from str8 import Str
from list8 import List
__version__ = "0.0.5"
class Pip:

    @staticmethod
    def main(list_of_args):
        try:
            from pip import main as pip_main
        except ImportError:
            from pip._internal import main as pip_main
        return pip_main(list_of_args)

    @classmethod
    def install(Pip, *module_names, upgrade=False, uninstall=False):
        commands = ["install"]
        if uninstall: commands = ["uninstall", "-y"]
        elif upgrade: commands.append("--upgrade")
        commands.append(module_names)
        Pip.main(List.flatterize(commands))
        time.sleep(0.5)
        Pip.update_list_of_modules()

    @classmethod
    def uninstall(Pip, *module_names):
        Pip.install(*module_names, uninstall=True)

    @classmethod
    def check_pip_installation(Pip):
        if "pip" not in Pip.list_of_modules:
            if OS.name == "linux":
                os.system("sudo apt-get install python" + OS.python_commandline_version + "-pip")

    @classmethod
    def update_all_packages(Pip):
        packages = Str.nl(Console.get_output("pip list"))
        packages_names = []
        for package in packages[3:]:
            if ("Package" not in package) and ("---" not in package) and package != "":
                packages_names.append(Str.get_words(package)[0])
        Print.debug(packages_names)
        Pip.install(*packages_names, upgrade=True)

    list_of_modules = []

    @classmethod
    def update_list_of_modules(Pip):
        import pkgutil
        Pip.list_of_modules = []
        for item in pkgutil.iter_modules():
            Pip.list_of_modules.append(item[1])
Pip.update_list_of_modules()
