#! python3
# -*- coding: utf-8 -*-
import string
import sys
from commands import *
try:
    import todoist
except ImportError:
    from commands.pip8 import Pip
    Pip.install("todoist-python")
    import todoist


class Arguments:
    cleanup = False
    if "cleanup" in sys.argv:
        cleanup = True

    test = False
    if "test" in sys.argv:
        test = True


def encrypt(string, password):
    int_list = []
    password_len = len(password)
    for cnt, sym in enumerate(string):
        password_sym = password[cnt % password_len]
        int_list.append(ord(sym)-ord(password_sym))
    return int_list


def decrypt(int_list, password):
    output_string = ""
    password_len = len(password)
    for cnt, numb in enumerate(int_list):
        password_sym = password[cnt % password_len]
        output_string += chr(numb+ord(password_sym))
    return output_string


# 137925c1eb6296e4b96deeb5ad264bcc89587056
encoded = [-20, -20, -50, -14, -61, -54, 2, 0, 32, 27, -51, -21, -54, -53, 4, 3, 29, -14, -51, 29, -10, -6, 1, 4, 28,
           29, -55, -17, -59, -9, 2, 50, -13, -14, -52, -15, -56, -59, -44, 5]  # yes, that shitty

decoded = decrypt(encoded, Str.input_pass("Input password: "))

print(f"API key: {decoded}")

api = todoist.TodoistAPI(decoded)

api.sync()

print(api.state["user"]["full_name"])

for project in api.state['projects']:
    print("    " + project["name"])


if Arguments.cleanup:
    if CLI.get_y_n(f'Do you really want to remove all data in account {api.state["user"]["full_name"]}'):
        for task in api.items.all():
            task_id = task["id"]
            task_obj = api.items.get_by_id(task_id)
            task_obj.delete()
            Print.colored("    Task", task_obj["content"], "deleted", "red")
        for project in api.projects.all():
            project.delete()
            Print.colored("Project", project["name"], "deleted", "red")



if Arguments.test:
    new_project = api.projects.add(f"Test+{Time.dotted()}")
    task1 = api.items.add("Task1", new_project["id"])
    task2 = api.items.add("Task2", new_project["id"])


api.commit()

"""
Xiaomi Piston наушники хорошие внутриканальные
Антидепрессанты (Тенатен?)
Olloclip (прикольные линзы для телефона)
Snail w3d (смартфон игровая приставка с 3д экраном за дёшево)
Download master скачивает подписки утюг
Весы кухонные
В smartwatch есть джипиэс и они работают с слипэсэндроид
Lifx лампочка умная
Настоящий фотоаппарат"""