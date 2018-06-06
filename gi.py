#! python3
# -*- coding: utf-8 -*-
"""Internal module to simplify work with git
"""
# pylint: disable=unused-wildcard-import, wildcard-import
import sys
sys.path.append("..")
try:
    from commands8 import *
except ModuleNotFoundError:
    from commands.path8 import Path
    from commands.process8 import Process
    from commands.bash8 import Bash
__version__ = "1.1.3"

# for setup.py
# try:
#     from commands.dir8 import Dir
#     from commands.file8 import File
#     from commands.print8 import Print
# except ModuleNotFoundError:
#     print("using commands8? 0_o")
#
# import os
# if not os.path.isdir(Path.extend(Path.working(), "commands")):
#     Dir.create(Path.extend(Path.working(), "commands"))
#
# for file_or_dir in Dir.list_of_files(Path.commands8()):
#     if file_or_dir not in ["commands", ".git", ".idea", ".gitignore", "venv", "__pycache__"]:
#         file_to_copy = Path.extend(Path.working(), file_or_dir)
#         new_file = Path.extend(Path.working(), "commands", file_or_dir)
#         File.copy(file_to_copy, new_file)
# end support for setup.py

def get_name_of_repo():
    """Return mine name of repo
    :return: string, name of repo
    """
    import os
    if Path.working().split(os.sep)[-1] in ["t", "term"]:
        return "test"
    return Path.working().split(os.sep)[-1]


class Git:
    """Class to simplify work with git, wrapper for cli git
    """
    @classmethod
    def add(cls, what):
        """Adds files to next commit
        :param what: string, adding files
        :return: None
        """
        Process.start("git", "add", what)

    @classmethod
    def commit(cls, message=None):
        """Commit all added changes
        :param message: string, message of commit
        :return: None
        """
        commands = ["git", "commit"]
        if message:
            commands.append("-m")
            commands.append(Bash.argument_escape(message))
        Process.start(commands)

    @classmethod
    def push(cls, path, upstream=False):
        """Push commits to 'path' repo
        :param path: string, path of repo
        :param upstream: boolean, if True, adding argument '-u' to git
        :return: None
        """
        commands = ["git", "push"]
        if upstream:
            commands.append("-u")
        commands.append(path)
        Process.start(commands)

    @classmethod
    def update(cls, message, path="https://github.com/egigoka/" + get_name_of_repo() + ".git"):
        """Automatization to mine git upload
        :param message: string, commit message
        :param path: string, path to repo
        :return: None
        """
        cls.add(".")
        cls.commit(message)
        cls.push(path, upstream=True)



if __name__ == "__main__":
    ARGUMENTS = list(sys.argv)
    ARGUMENTS.pop(0)
    STRING = "small update (default message)"
    try:
        ARGUMENTS[0]  # pylint: disable=pointless-statement
        STRING = ""
        for arg in ARGUMENTS:
            STRING += arg + " "
        STRING = STRING.rstrip(" ")
    except IndexError:
        INPUT_STRING = input("Enter a description or press Enter to default message: ")
        if INPUT_STRING:
            STRING = INPUT_STRING
    Git.update(STRING)

