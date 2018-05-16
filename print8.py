#! python3
# -*- coding: utf-8 -*-
# http://python.su/forum/topic/15531/?page=1#post-93316
from os8 import OS
from console8 import Console
from const8 import *
__version__ = "0.1.3"
class Print():
    @staticmethod
    def debug(*strings, raw=False):  # d just more notable print, only for
      # d debugging
        line = "-" * Console.width()
        print("<<<Debug sheet:>>>")
        for str_ in strings:
            print(line, end="")
            if raw:
                print(repr(str_))
            else:
                print(str_)
            print(line)
        print("<<<End of debug sheet>>>")

    @staticmethod
    def rewrite(*strings, sep=" ", raw=False):  # d string, that can be rewritable
      # d note, that you need to rewrite string to remove characters
        # clean
        line = " " * Console.width()
        if OS.name == "windows":
            line = line[:-1]
        print(line, end="\r")
        # print or output

        print(*strings, sep=sep, end="\r")

    @staticmethod
    def prettify(object, indent=4, quiet=False):
        import pprint
        pp = pprint.PrettyPrinter(indent=indent)
        if not quiet:
            pp.pprint(object)
        else:
            return pp.pformat(object=object)

    colorama_inited = False

    @classmethod
    def colored(Print, *strings, attrs=None, end=newline, sep=" "):  # usage: Print.colored("text", "red") or Print.colored("text", "red", "on_white")
      # d you can pick colors from termcolor.COLORS, highlights from termcolor.HIGHLIGHTS
        import termcolor
        if OS.name == "windows":
            import colorama
            colorama.init()
        # check for colors in input
        highlight = None
        color = None
        color_args = 0
        if len(strings) >= 3:
            if strings[-1] in termcolor.HIGHLIGHTS:
                highlight = strings[-1]
                color_args += 1
                if strings[-2] in termcolor.COLORS:
                    color = strings[-2]
                color_args += 1
        elif len(strings) >= 2:
            if strings[-1] in termcolor.COLORS:
                color = strings[-1]
                color_args += 1
            elif strings[-1] in termcolor.HIGHLIGHTS:
                highlight = strings[-1]
                color_args += 1
        # create single string to pass it into termcolor
        string = ""
        strings = strings[:-color_args]
        for substring in strings[:-1]:  # все строки добавляются в основную строку с сепаратором
            string += substring + sep
        string += strings[-1]  # последняя без сепаратора
        # run termcolor
        termcolor.cprrint(string, color=color, on_color=highlight, attrs=attrs, end=end)