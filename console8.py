#! python3
# -*- coding: utf-8 -*-
# http://python.su/forum/topic/15531/?page=1#post-93316
from os8 import OS
from str8 import Str
import os
__version__ = "0.0.2"

class Console():
    @staticmethod
    def clean():  # wipe terminal output. Not tested on linux
      # todo test on linux
        if OS.name == "windows":
            os.system("cls")
        elif OS.name == "linux":
            import shutil
            print(newline * shutil.get_terminal_size().lines)
        elif OS.name == "macos":
            os.system(r"clear && printf '\e[3J'")

    @staticmethod
    def width():  # return width of terminal window in characters
        if OS.name == "windows":
            import shutil
            width_ = shutil.get_terminal_size().columns
        elif OS.name in ["linux", "macos"]:
            io = Console.get_output("stty size")
            width_ = Str.get_integers(io)[1]
        return int(width_)

    @staticmethod
    def height():  # return height of terminal window in characters
        if OS.name == "windows":
            import shutil
            height = width_ = shutil.get_terminal_size().lines
        elif OS.name in ["linux", "macos"]:
            sttysize = Console.get_output("stty size")
            height = Str.get_integers(sttysize)[0]
        if height > 100:
            height = 100
        return int(height)

    @classmethod
    def blink(cls, width=None, height=None, symbol="#", sleep=0.5):
        import random
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
                import time
                import termcolor
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
        # TODO make ouptut even if exit status != 0
        import subprocess
        p = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        if OS.name == "windows":
            output = p.decode("cp866")
        elif OS.family == "unix":
            output = p.decode("utf8")
        if split_lines:
            output = Str.nl(output)
        return output
