#! python3
# -*- coding: utf-8 -*-
from commands8 import *
__version__ = "1.0.0"

def get_name_of_repo():
    if Path.working().split(os.sep)[-1] in ["t", "term"]:
        return "test"
    else:
        return Path.working().split(os.sep)[-1]


class Git:
    @classmethod
    def add(cls, what):
        Process.start("git", "add", what)

    @classmethod
    def commit(cls, message=None):
        commands = ["git", "commit"]
        if message:
            commands.append("-m")
            commands.append(Bash.argument_escape(message))
        Process.start(commands)

    @classmethod
    def push(cls, path, upstream=False):
        commands = ["git", "push"]
        if upstream:
            commands.append("-u")
        commands.append(path)
        Process.start(commands)

    @classmethod
    def update(cls, message, path="https://github.com/egigoka/" + get_name_of_repo() + ".git"):
        cls.add(".")
        cls.commit(message)
        cls.push(path, upstream=True)



if __name__ == "__main__":
    arguments = list(sys.argv)
    arguments.pop(0)
    string = "small update (default message)"
    try:
        arguments[0]
        string = ""
        for arg in arguments:
            string += arg + " "
        string = string.rstrip(" ")
    except IndexError:
        input_string = input("Enter a description or press Enter to default message: ")
        if input_string:
            string = input_string
    Git.update(string)
