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
    first_message = True


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

    last_message = message.message_id + 1

    if State.first_message:
        markup = telebot.types.ReplyKeyboardMarkup()
        button = telebot.types.KeyboardButton('MOAR!')
        markup.row(button)

        telegram_api.send_message(message.chat.id, "init keyboard", reply_markup=markup)

        last_message += 1
        State.first_message = False

    telegram_api.send_message(message.chat.id, "wait")

    telegram_api.edit_message_text(chat_id=message.chat.id, message_id=last_message, text=get_random_todo())#, reply_markup=markup)


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