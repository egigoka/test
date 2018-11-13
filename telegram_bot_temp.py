#! python3
# -*- coding: utf-8 -*-
try:
    from commands import *
except ImportError:
    import os
    os.system("pip install git+https://github.com/egigoka/commands")
    from commands import *
try:
    import telebot
except ImportError:
    from commands.pip8 import Pip
    Pip.install("pytelegrambotapi")
    import telebot
from todoist_temp import *
import requests


class Arguments:
    pass


class State:
    def __init__(self, excluded_projects=[], excluded_items=[]):
        self.first_message = True
        self.getting_project_name = False
        self.getting_item_name = False

        self.excluded_projects = excluded_projects
        self.excluded_items = excluded_items

        self.counter_for_left_items = False
        self.counter_for_left_items_int = 0

        self.all_todo_str = ""

        self.sended_messages = 1


State = State()


def get_random_todo():
    Print.rewrite("Getting random todo")
    bench = Bench(prefix="Get random item in")
    bench.start()
    incomplete_items = todo.all_incomplete_items_in_account()
    bench.end()

    State.counter_for_left_items_int = 0

    State.all_todo_str = ""
    for project_name, project_items in Dict.iterable(incomplete_items.copy()):  # removing excluded
        if project_name.strip() in State.excluded_projects:
            incomplete_items[project_name] = []
            continue
        if project_items:
            print(f'"{project_name}"')
            State.all_todo_str += project_name + newline
        for item in project_items.copy():

            if item["content"].strip() in State.excluded_items:
                incomplete_items[project_name].remove(item)
                print(f'    "{item["content"]}" deleted')
            else:
                State.counter_for_left_items_int += 1
                print(f'    "{item["content"]}"')
                State.all_todo_str += "    " + item["content"] + newline

    for project_name, project_items in Dict.iterable(incomplete_items.copy()):  # removing empty projects
        if not project_items:
            incomplete_items.pop(project_name)

    try:
        random_project_name, random_project_items = Random.item(incomplete_items)
    except IndexError:
        return "All done!"
    random_item = Random.item(random_project_items)

    time_string = ""
    if random_item["due_date_utc"]:
        if not random_item["due_date_utc"].endswith("20:59:59 +0000"):
            time_string = random_item["date_string"]

    counter_for_left_items_str = ""
    if State.counter_for_left_items:
        counter_for_left_items_str = f"({State.counter_for_left_items_int} left)"

    return f"{random_item['content']} <{random_project_name}> {time_string} {counter_for_left_items_str}".replace(">  (", "> (")


encrypted = [-15, -21, -49, -16, -63, -52, -46, 6, -20, -13, -40, -6, -39, -33, 22, 0, 1, 51, 9, -26, -41, -24, 13,
                 4, 49, 44, -25, 18, 9, -18, -19, 72, -12, -26, -3, 3, -62, 3, 17, 4, 7, -3, -33, -3, -12]


telegram_token = Str.decrypt(encrypted, Str.input_pass("Enter password:"))

todoist_api = Todoist(todoist_api_key)

telegram_api = telebot.TeleBot(telegram_token, threaded=False)
# https://github.com/eternnoir/pyTelegramBotAPI/issues/273


@telegram_api.message_handler(content_types=["text"])
def reply_all_messages(message):
    def main_message(sended_messages_before=0):
        last_message = message.message_id + State.sended_messages + sended_messages_before
        State.sended_messages = 1

        if State.first_message:
            markup = telebot.types.ReplyKeyboardMarkup()
            main_button = telebot.types.KeyboardButton('MOAR!')
            settings_button = telebot.types.KeyboardButton('Settings')
            list_button = telebot.types.KeyboardButton('List')
            markup.row(main_button)
            markup.row(settings_button, list_button)

            telegram_api.send_message(message.chat.id, "init keyboard", reply_markup=markup)

            last_message += 1
            State.first_message = False

        if State.excluded_projects:
            excluded_str = f"Excluded projects: {State.excluded_projects}."
        else:
            excluded_str = "No excluded projects."
        if State.excluded_items:
            excluded_str += f"{newline}Excluded items: {State.excluded_items}."
        else:
            excluded_str += f"{newline}No excluded items."

        telegram_api.send_message(message.chat.id, f"{excluded_str}{newline}wait")

        telegram_api.edit_message_text(chat_id=message.chat.id, message_id=last_message,
                                       text=f"{excluded_str}{newline}{get_random_todo()}")  # , reply_markup=markup)

    if message.chat.id != 5328715:
        telegram_api.send_message(message.chat.id, "ACCESS DENY!")
        return

    if State.getting_project_name:
        message_text = message.text.strip()
        if message_text in State.excluded_projects:
            State.excluded_projects.remove(message_text)
        else:
            State.excluded_projects.append(message_text)
        State.getting_project_name = False
        State.getting_item_name = False
        State.first_message = True
        main_message()

    elif State.getting_item_name:
        message_text = message.text.strip()
        if message_text in State.excluded_items:
            State.excluded_items.remove(message_text)
        else:
            State.excluded_items.append(message_text)
        State.getting_item_name = False
        State.first_message = True
        main_message()

    elif message.text == "MOAR!" or State.first_message:  # MAIN MESSAGE
        main_message()

    elif message.text == "List":
        if State.first_message:
            get_random_todo()
        if State.all_todo_str:
            telegram_api.send_message(message.chat.id, State.all_todo_str)
        else:
            telegram_api.send_message(message.chat.id, "Todo list for today is empty!")
        main_message(1)

    elif message.text == "Settings":
        State.first_message = False

        markup = telebot.types.ReplyKeyboardMarkup()
        project_exclude_button = telebot.types.KeyboardButton("Exclude project")
        project_include_button = telebot.types.KeyboardButton("Include project")

        items_exclude_button = telebot.types.KeyboardButton("Exclude items")
        items_include_button = telebot.types.KeyboardButton("Include items")

        clean_black_list_button = telebot.types.KeyboardButton("Clean black list")

        counter_for_left_items_button = telebot.types.KeyboardButton("Toggle left items counter")

        markup.row(project_exclude_button, project_include_button)
        markup.row(items_exclude_button, items_include_button)
        markup.row(clean_black_list_button)
        markup.row(counter_for_left_items_button)

        telegram_api.send_message(message.chat.id, "Settings:", reply_markup=markup)

    elif message.text == "Exclude project":
        markup = telebot.types.ReplyKeyboardMarkup()
        for project_name, project_id in Dict.iterable(todoist_api.projects_all_names()):
            if project_name not in State.excluded_projects:
                project_button = telebot.types.KeyboardButton(project_name)
                markup.row(project_button)

        telegram_api.send_message(message.chat.id, "Send me project name to exclude:", reply_markup=markup)

        State.getting_project_name = True

    elif message.text == "Include project":
        if State.excluded_projects:
            markup = telebot.types.ReplyKeyboardMarkup()
            for project_name in State.excluded_projects:
                project_button = telebot.types.KeyboardButton(project_name)
                markup.row(project_button)

            telegram_api.send_message(message.chat.id, "Send me project name to include:", reply_markup=markup)

            State.getting_project_name = True
        else:
            telegram_api.send_message(message.chat.id, "No excluded projects, skip...")
            State.first_message = True
            main_message(1)

    elif message.text == "Exclude items":
        # markup = telebot.types.ForceReply(selective=False) it doesn't show up default keyboard :(

        markup = telebot.types.ReplyKeyboardMarkup()
        default_items = False
        for item_name in [r"Vacuum/sweep", "Wash the floor"]:
            if item_name not in State.excluded_items:
                project_button = telebot.types.KeyboardButton(item_name)
                markup.row(project_button)
                default_items = True

        if not default_items:
            project_button = telebot.types.KeyboardButton("Enter item manually")
            markup.row(project_button)

        telegram_api.send_message(message.chat.id, "Send me item name:", reply_markup=markup)

        State.getting_item_name = True

    elif message.text == "Include items":
        if State.excluded_items:
            markup = telebot.types.ReplyKeyboardMarkup()
            for item_name in State.excluded_items:
                project_button = telebot.types.KeyboardButton(item_name)
                markup.row(project_button)

            telegram_api.send_message(message.chat.id, "Send me item name:", reply_markup=markup)

            State.getting_item_name = True
        else:
            telegram_api.send_message(message.chat.id, "No excluded items, skip...")
            State.first_message = True
            main_message(1)

    elif message.text == "Clean black list":
        State.excluded_items = []
        State.excluded_projects = []
        State.first_message = True
        main_message()

    elif message.text == "Toggle left items counter":
        if State.counter_for_left_items:
            State.counter_for_left_items = False
        else:
            State.counter_for_left_items = True
        State.first_message = True
        main_message()

    else:
        telegram_api.send_message(message.chat.id, f"ERROR! <{message.text}>")
        State.first_message = True
        State.sended_messages += 1
        main_message()


def main():
    try:
        Print.colored("Bot started", "green")
        telegram_api.polling(none_stop=True)
        Print.colored("Bot ended", "green")
    except KeyboardInterrupt:
        print("Ctrl+C")
    except requests.exceptions.ReadTimeout:
        print(f"requests.exceptions.ReadTimeout... {Time.dotted()}")
        main()
    except requests.exceptions.ConnectionError:
        print(f"requests.exceptions.ConnectionError... {Time.dotted()}")
        main()


if __name__ == '__main__':
    main()



#if __name__ == '__main__':
#        main()