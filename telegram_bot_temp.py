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


State = State()


def get_random_todo():
    Print.rewrite("Getting random todo")
    bench = Bench(prefix="Get random item in")
    bench.start()
    incomplete_items = todo.all_incomplete_items_in_account()
    bench.end()

    for project_name, project_items in Dict.iterable(incomplete_items.copy()):
        if not project_items:
            incomplete_items.pop(project_name)

    random_project_name, random_project_items = Random.item(incomplete_items)
    random_item = Random.item(random_project_items)

    time_string = ""
    if random_item["due_date_utc"]:
        if not random_item["due_date_utc"].endswith("20:59:59 +0000"):
            time_string = random_item["date_string"]

    return f"{random_item['content']} <{random_project_name}> {time_string}"


encrypted = [-15, -21, -49, -16, -63, -52, -46, 6, -20, -13, -40, -6, -39, -33, 22, 0, 1, 51, 9, -26, -41, -24, 13,
                 4, 49, 44, -25, 18, 9, -18, -19, 72, -12, -26, -3, 3, -62, 3, 17, 4, 7, -3, -33, -3, -12]


telegram_token = Str.decrypt(encrypted, Str.input_pass("Enter password:"))

todoist_api = Todoist(todoist_api_key)

telegram_api = telebot.TeleBot(telegram_token)

@telegram_api.message_handler(content_types=["text"])
def reply_all_messages(message): # Название функции не играет никакой роли, в принципе
    if message.chat.id != 5328715:
        telegram_api.send_message(message.chat.id, "ACCESS DENY!")
        return

    if State.getting_project_name:
        State.excluded_projects.append(message.text)
        State.__init__(excluded_projects=State.excluded_projects, excluded_items=State.excluded_items)

    elif State.getting_item_name:
        State.excluded_items.append(message.text)
        State.__init__(excluded_projects=State.excluded_projects, excluded_items=State.excluded_items)

    elif message.text == "MOAR!" or State.first_message:  # main button

        last_message = message.message_id + 3

        if State.first_message:
            markup = telebot.types.ReplyKeyboardMarkup()
            main_button = telebot.types.KeyboardButton('MOAR!')
            settings_button = telebot.types.KeyboardButton('Settings')
            markup.row(main_button)
            markup.row(settings_button)

            telegram_api.send_message(message.chat.id, "init keyboard", reply_markup=markup)

            last_message += 1
            State.first_message = False

        telegram_api.send_message(message.chat.id, f"Excluded projects: {State.excluded_projects}")
        telegram_api.send_message(message.chat.id, f"Excluded items: {State.excluded_items}")

        telegram_api.send_message(message.chat.id, "wait")

        telegram_api.edit_message_text(chat_id=message.chat.id, message_id=last_message, text=get_random_todo())#, reply_markup=markup)

    elif message.text == "Settings":
        State.first_message = False

        markup = telebot.types.ReplyKeyboardMarkup()
        project_exclude_button = telebot.types.KeyboardButton("Exclude project")
        items_exclude_button = telebot.types.KeyboardButton("Exclude items by name")
        clean_black_list_button = telebot.types.KeyboardButton("Clean black list")
        markup.row(project_exclude_button)
        markup.row(items_exclude_button)
        markup.row(clean_black_list_button)

        telegram_api.send_message(message.chat.id, "Settings:", reply_markup=markup)

    elif message.text == "Exclude project":
        markup = telebot.types.ForceReply(selective=False)

        telegram_api.send_message(message.chat.id, "Send me project name:", reply_markup=markup)

        State.getting_project_name = True

    elif message.text == "Exclude items by name":
        markup = telebot.types.ForceReply(selective=False)

        telegram_api.send_message(message.chat.id, "Send me item name:", reply_markup=markup)

        State.getting_item_name = True

    elif message.text == "Clean black list":
        State.__init__()

    else:
        telegram_api.send_message(message.chat.id, f"ERROR! <{message.text}>")
        State.__init__(excluded_projects=State.excluded_projects, excluded_items=State.excluded_items)



def main():
    try:
        Print.colored("Bot started", "green")
        telegram_api.polling(none_stop=True)
        Print.colored("Bot ended", "green")
    except KeyboardInterrupt:
        print("Ctrl+C")
    except requests.exceptions.ReadTimeout:
        Print("Timeout...")
        main()


if __name__ == '__main__':
    main()



#if __name__ == '__main__':
#        main()