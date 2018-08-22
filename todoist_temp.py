#! python3
# -*- coding: utf-8 -*-
import string
import sys
import time
from commands import *
try:
    import todoist
except ImportError:
    from commands.pip8 import Pip
    Pip.install("todoist-python")
    import todoist


class Arguments:
    apikey = False
    if "apikey" in sys.argv:
        apikey = True

    cleanup = False
    if "cleanup" in sys.argv:
        cleanup = True

    test = False
    if "test" in sys.argv:
        test = True

    work = False
    if "work" in sys.argv:
        work = True

    list = False
    if "list" in sys.argv:
        list = True

    name = False
    if "name" in sys.argv:
        name = True


class Priority:
    USUAL = 1
    HIGH = 2
    VERY_HIGH = 3
    EXTREMELY = 4


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


class Todoist:

    #api here
    def __init__(self, api_key):
        Print.rewrite("Loading cache...")
        self.api = todoist.TodoistAPI(api_key)
        Print.rewrite("Syncing...")
        self.api.sync()
        Print.rewrite("Synced")

    def projects_all_names(self):
        names = {}
        for project in self.api.projects.all():
            names[project["name"]] = project["id"]
        return names

    def project_exists(self, name):
        all_projects = self.projects_all_names()
        if name in all_projects:
            return all_projects[name]
        return False

    def get_temp_project(self, prefix="Temp"):
        project_name = None
        cnt = 0
        while not project_name:
            cnt += 1
            temp_name = f"{prefix}_{cnt}"
            if not todo.project_exists(temp_name):
                project_name = temp_name
        new_project = self.api.projects.add(project_name)
        return new_project

    def project_raw_items(self, name):
        # Print.debug(self.api.projects.get_data(self.project_exists(name)))
        if self.project_exists(name):
            return self.api.projects.get_data(self.project_exists(name))["items"]
        else:
            raise KeyError(f"Project {name} doesn't exist!")

    def project_items_names(self, name):
        raw = self.project_raw_items(name)
        items = {}
        for item in raw:
            items[item["content"]] = item["id"]
        return items

    def create_project(self, name):
        project_id = self.project_exists(name)
        if not project_id:
            print(f"Creating project {name}")
            project = todo.api.projects.add(name)
            todo.api.commit()
            todo.api.sync()
            project_id = self.project_exists(name)
        return project_id

    def add_item(self, name, project_name, item_order, day_order, priority=Priority.USUAL, date_string=None, due_date_utc=None, auto_create_project=False):
        project_id = self.project_exists(project_name)
        if auto_create_project:
            project_id = self.create_project(project_name)
        else:
            raise KeyError(f"Project {project_name} doesn't exists")
        if date_string and due_date_utc:
            raise KeyError(f"only date_string {date_string} or due_date_utc {due_date_utc}")
        elif date_string:
            item = todo.api.items.add(name, project_id, item_order=item_order, date_string=date_string,
                                      day_order=day_order, priority=priority)
        elif due_date_utc:
            item = todo.api.items.add(name, project_id, item_order=item_order, due_date_utc=due_date_utc,
                                      day_order=day_order, priority=priority)
        else:
            item = todo.api.items.add(name, project_id, item_order=item_order, day_order=day_order, priority=priority)
        return item

    def date_string_today(self):
        return datetime.datetime.now().strftime("%d %b %Y")

    def __del__(self):
        print("try to commit changes")
        self.api.commit()
        print("api commited")


encoded = [-20, -20, -50, -14, -61, -54, 2, 0, 32, 27, -51, -21, -54, -53, 4, 3, 29, -14, -51, 29, -10, -6, 1, 4, 28,
           29, -55, -17, -59, -9, 2, 50, -13, -14, -52, -15, -56, -59, -44, 5]  # yes, that shitty

decoded = decrypt(encoded, Str.input_pass("Input password: "))

if Arguments.apikey:
    print(f"API key: {decoded}")

todo = Todoist(decoded)

if Arguments.name:
    print(todo.api.state["user"]["full_name"])

if Arguments.cleanup:
    if CLI.get_y_n(f'Do you really want to remove all data in account {todo.api.state["user"]["full_name"]}'):
        for task in todo.api.items.all():
            task.delete()
            Print.colored("    Task", task["content"], "deleted", "red")
        for project_id in todo.api.projects.all():
            project_id.delete()
            Print.colored("Project", project_id["name"], "deleted", "red")
        todo.api.commit()

if Arguments.list:
    for task in todo.api.items.all():
        Print.colored(">=>", task["content"])
    for project_id in todo.api.projects.all():
        Print.colored("Project", project_id["name"])

if Arguments.test:
    new_project = todo.get_temp_project("Test")
    Print.colored(f"Project {new_project} created")
    task1 = todo.api.items.add("Task1_io0", new_project["id"], item_order=0)
    task2 = todo.api.items.add("Task2_io1", new_project["id"], priority=Priority.HIGH, item_order=1)
    task3 = todo.api.items.add("Task3_io999", new_project["id"], item_order=999)
    task4 = todo.api.items.add("Task4_io4", new_project["id"], item_order=4)
    task5 = todo.api.items.add("Task5_io3", new_project["id"], item_order=3)
    task6 = todo.api.items.add("Task6_io999", new_project["id"], item_order=999)
    task7 = todo.api.items.add("Task7_io-1", new_project["id"], item_order=-1)
    task8 = todo.api.items.add("Task8_io-2", new_project["id"], item_order=-2)

    # test time
    now = time.time()
    tomorrow = time.gmtime(now + 24 * 3600)
    due_date_utc = time.strftime("%Y-%m-%dT%H:%M", tomorrow)
    task9 = todo.api.items.add("Task9+io-10+due_date_utc", new_project["id"], item_order=-10, due_date_utc=due_date_utc)
    task10 = todo.api.items.add("Task10+io-10+due_date_utc", new_project["id"], item_order=-10, due_date_utc=due_date_utc, all_day=True)
    atestitem = todo.api.items.add("succ", new_project["id"], item_order=-1, date_string="17 Jan 2018 every 3 days")

    #
    # due_date_utc
    # String
    # 	The date of the task in the format Mon 07 Aug 2006 12:34:56 +0000 (or null if not set). For all day task (i.e. task due “Today”), the time part will be set as xx:xx:59.

if Arguments.work:
    # items = ['Wash the clothes - Shower room - 1 week', 'Clean out the tables - Kitchen - 2 days',
    #          'Wash dishes - Kitchen - 1 day', 'Take out the trash - Kitchen - 1 day',
    #          'Wash the stove - Kitchen - 1 day',
    #          'Vacuum/sweep - Kitchen - 1 day', 'Wash the floor - Kitchen - 3 days', 'Clean out - Balcony - 3 days',
    #          'Wash the floor - Balcony - 3 days', 'Clean up on the table - My room - 2 days',
    #          'Clean out - My room - 2 days', 'Wipe dust - My room - 1 week','Fill the bed - My room - 1 day',
    #          'Vacuum/sweep - My room - 1 day', 'Wash the floor - My room - 3 days',
    #          'Wash shower - Shower room - 1 day', 'Wash the sink - Shower room - 1 day',
    #          'Vacuum/sweep - Shower room - 1 day', 'Vacuum/sweep - Toilet - 1 day',
    #          'Wash the floor - Shower room - 3 days', 'Wash the floor - Toilet - 3 days',
    #          'Wash toilet - Toilet - 1 week', 'Wash and place shoes - Hallway - 2 days',
    #          'Vacuum/sweep - Corridor - 1 day', 'Vacuum/sweep - Hallway - 1 day','Wash the floor - Corridor - 3 days',
    #          'Wash the floor - Hallway - 3 days', 'Wash the sink - Kitchen - 3 days',
    #          'Clothes to gather - Balcony - 1 week','Wipe in the wardrobe - Wardrobe - 3 days']
    # items = [
    #     "Brush teeth in morning - Hygiene - 1 day",
    #     "Brush teeth in evening - Hygiene - 1 day",
    #     "Shower - Hygiene - 1 day",
    #     "Deodorant - Hygiene - 1 day",
    #     "Shaving - Hygiene - 1 day",
    #     "Cut nails on toes - Hygiene - 2 weeks",
    #     "Cut nails on fingers - Hygiene - 2 weeks"
    # ]
    items = Str.nl("""Упражнения против синдрома кистей
Diary
Memrise English
-1 subscription Twitter
Offload one app
Разобрать 100 фоток на айфоне
Change something to English
Memrise Finish
Разобрать почту""")
    cnt_order = 1000
    for item in items:
        # try:
        #     properties = item.split(" - ")
        #     name = properties[0]
        #     where = properties[1]
        #     repeat_time = properties[2]
        # except IndexError:
        #     print(item)
        #     sys.exit(1)
        name = item
        where = "Everyday"
        repeat_time = "1 day"

        cnt_order += 1
        item_order = day_order = cnt_order

        todo.add_item(name, where, item_order, day_order, priority=Priority.USUAL,
                      date_string=f"{todo.date_string_today()} every {repeat_time}", auto_create_project=True)
        Print.debug(f'''todo.add_item({name}, {where}, {item_order}, {day_order}, priority={Priority.USUAL},
                      date_string=f"{todo.date_string_today()} every {repeat_time}", auto_create_project={True})''')

    todo.api.commit()

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

