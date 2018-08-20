#! python3
# -*- coding: utf-8 -*-
from commands import *
try:
    import todoist
except ImportError:
    from commands.pip8 import Pip
    Pip.install("todoist-python")
    import todoist


def encode(string, password):  # some kind of Gronsfeld Cipher
    output = []
    password_len = len(password)
    for cnt, sym in enumerate(string):
        password_sym = password[cnt % password_len]
        output.append(ord(sym)-ord(password_sym))
    return output


def decode(list, password):
    output = ""
    password_len = len(password)
    for cnt, numb in enumerate(list):
        password_sym = password[cnt % password_len]
        output += chr(numb+ord(password_sym))
    return output


encoded = [-20, -20, -50, -14, -61, -54, 2, 0, 32, 27, -51, -21, -54, -53, 4, 3, 29, -14, -51, 29, -10, -6, 1, 4, 28,
           29, -55, -17, -59, -9, 2, 50, -13, -14, -52, -15, -56, -59, -44, 5]  # yes, that shitty

decoded = decode(encoded, Str.input_pass("Input password: "))

print(decoded)

api = todoist.TodoistAPI(decoded)

api.sync()

print(api.state["user"]["full_name"])

for project in api.state['projects']:
    print("    " + project["name"])