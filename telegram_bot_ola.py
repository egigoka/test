#! python3
# -*- coding: utf-8 -*-
import datetime
try:
    from commands import *
except ImportError:
    import os
    os.system("pip install git+https://github.com/egigoka/commands")
    from commands import *
try:
    import telebot
except ImportError:
    from commands.pip9 import Pip
    Pip.install("pytelegrambotapi")
    import telebot
import requests

__version__ = "1.4.1"

my_chat_id = 5328715
ola_chat_id = 550959211
tgx_chat_id = 619037205

encrypted_telegram_token_olacushatc = [-14, -22, -51, -21, -57, -55, -42, 6, -20, -13, -40, -6, -42, -3, 1, 20, -3, -15,
                                       -16, 47, -45, 0, -24, 62, 7, -17, -55, -14, -39, 2, -15, 58, 16, -17, -16, 46,
                                       -11, -31, -47, 49, 46, 45, -60, 30, -26]


telegram_token_olacushatc = Str.decrypt(encrypted_telegram_token_olacushatc, Str.input_pass())
# telegram_token = Str.decrypt(encrypted, Str.input_pass("Enter password:"))

telegram_api_olacushatcs = telebot.TeleBot(telegram_token_olacushatc, threaded=False)

class State:
    last_sent = ""


def _start_ola_bot_reciever():
    @telegram_api_olacushatcs.message_handler(content_types=["text", 'sticker'])
    def reply_all_messages_ola(message):
        if message.chat.id == my_chat_id:
            if message.text:
                if message.text.startswith("help"):
                    reply = "Commands not implemented now :("
                else:
                    telegram_api_olacushatcs.forward_message(ola_chat_id, message.chat.id, message.message_id,
                                                             disable_notification=True)
                    reply = f"Forwarded to Ola: {message.text}"
            else:
                telegram_api_olacushatcs.forward_message(ola_chat_id, message.chat.id, message.message_id,
                                                         disable_notification=True)
                reply = f"Forwarded to Ola: [sticker]"
            Print.rewrite()
            print(reply)
            telegram_api_olacushatcs.send_message(message.chat.id, reply, disable_notification=True)
        else:
            telegram_api_olacushatcs.forward_message(my_chat_id, message.chat.id, message.message_id,
                                                     disable_notification=True)
            Print.rewrite()
            print(f"from {message.chat.id}: {message.text}")
    telegram_api_olacushatcs.polling(none_stop=True)


def _start_ola_bot_sender():
    while True:
        nowdt = datetime.datetime.now()
        now = nowdt.strftime("%H:%M")
        Time.sleep(20)
        if now == "08:00" and State.last_sent != now:
            State.last_sent = now
            message_text = "Позавтрокой, ну шо тебе стоит?"
            telegram_api_olacushatcs.send_message(ola_chat_id, message_text)
            telegram_api_olacushatcs.send_message(my_chat_id, message_text)
        elif now == "14:00" and State.last_sent != now:
            State.last_sent = now
            message_text = f"Ну шо, поедим? Я пространство в твоём телефоне, а ты _{'_'.join('еды нормальной')}_ !!!"
            telegram_api_olacushatcs.send_message(ola_chat_id, message_text)
            telegram_api_olacushatcs.send_message(my_chat_id, message_text)
        elif now == "20:00" and State.last_sent != now:
            State.last_sent = now
            message_text = "БОтелло: Наелась ли ты на ночь, Демолишон?"
            telegram_api_olacushatcs.send_message(ola_chat_id, message_text)
            telegram_api_olacushatcs.send_message(my_chat_id, message_text)


def _start_ola_bot_sender_mine():
    while True:
        nowdt = datetime.datetime.now()
        now = nowdt.strftime("%H:%M")
        weekday = nowdt.strftime("%w")
        Time.sleep(20)
        if now in ["10:50", "16:50"] and State.last_sent != now:
            State.last_sent = now
            message_text = "Печеньки! Ура!"
            if weekday == 3:
                message_text = "Фруктики! Возьми, а?"
            telegram_api_olacushatcs.send_message(my_chat_id, message_text)
        elif now == "16:00" and State.last_sent != now:
            State.last_sent = now
            message_text = "Сходи, покушой, зоебал сидеть!"
            telegram_api_olacushatcs.send_message(my_chat_id, message_text)


def safe_start_bot(bot_func):
    ended = False
    while not ended:
        try:
            bot_func()
            Print.colored("Bot quited", "red")
            ended = True
        except requests.exceptions.ReadTimeout:
            print(f"{Time.dotted()} requests.exceptions.ReadTimeout...")
            Time.sleep(5)
        except requests.exceptions.ConnectionError:
            print(f"{Time.dotted()} requests.exceptions.ConnectionError...")
            Time.sleep(5)


def safe_threads_run():
    # https://www.tutorialspoint.com/python/python_multithreading.htm  # you can expand current implementation

    print(f"Main thread v{__version__} started")

    threads = Threading()

    threads.add(safe_start_bot, args=(_start_ola_bot_reciever,))
    threads.add(safe_start_bot, args=(_start_ola_bot_sender,))
    threads.add(safe_start_bot, args=(_start_ola_bot_sender_mine,))

    threads.start(wait_for_keyboard_interrupt=True)

    threads.wait_for_keyboard_interrupt()

    Print.rewrite()
    print("Main thread quited")



if __name__ == '__main__':
    safe_threads_run()
