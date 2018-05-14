#! python3
# -*- coding: utf-8 -*-
# http://python.su/forum/topic/15531/?page=1#post-93316
from os8 import OS
__version__ = "0.0.2"
class Print():
    @staticmethod
    def debug(*arguments, raw=False):  # d just more notable print, only for
      # d debugging
        line = "-" * Console.width()
        print("<<<Debug sheet:>>>")
        for arg in arguments:
            print(line, end="")
            if raw:
                print(repr(arg))
            else:
                print(arg)
            print(line)
        print("<<<End of debug sheet>>>")

    @staticmethod
    def rewrite(*arguments, sep=" ", raw=False):  # d string, that can be rewritable
      # d note, that you need to rewrite string to remove characters

        line = " " * Console.width()
        if OS.name == "windows":
            line = line[:-1]
        print(line, end="\r")
        print(*arguments, sep=sep, end="\r")

    @staticmethod
    def prettify(object, indent=4, quiet=False):
        import pprint
        pp = pprint.PrettyPrinter(indent=indent)
        if not quiet:
            pp.pprint(object)
        else:
            return pp.pformat(object=object)
