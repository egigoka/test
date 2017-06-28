#! python3
# -*- coding: utf-8 -*-
__version__ = "1.0.0"
from utils import file_wipe, file_create, newline
from os import path

def start_gen(file_path):
    global file
    file = open(file_path, "wb")


def add_line(code, nonl = False):
    global file
    file.write(code.encode('utf8'))
    # if True:
    #     print(code)
    if not nonl:
        file.write(newline.encode('utf8'))


def end_gen(quiet = False):
    global file
    file.close()


shebang = "#! python3" + newline + \
            "# -*- coding: utf-8 -*-"
