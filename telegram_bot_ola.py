#! python3
# -*- coding: utf-8 -*-
import sys
import os
import datetime
import threading
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

__version__ = "1.1.3"


class myThread(threading.Thread):
    def __init__(self, threadID, name, func, args=(), kwargs={}):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        print("Starting " + self.name)
        try:
            self.func(*self.args, **self.kwargs)
        except(KeyboardInterrupt, SystemExit):
            print("Control-C, exit")
            sys.exit(1)
        print("Exiting " + self.name)

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
            telegram_api_olacushatcs.send_message(ola_chat_id, message.text)
            telegram_api_olacushatcs.send_message(tgx_chat_id, message.text)
            Print.rewrite()
            print("to ola and tgx:", message.text)
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
            message_text = "Позавтрокой, умоляю"
            telegram_api_olacushatcs.send_message(ola_chat_id, message_text)
            telegram_api_olacushatcs.send_message(my_chat_id, message_text)
        elif now == "14:00" and State.last_sent != now:
            State.last_sent = now
            message_text = "Чтобы расти, нужно обедоть"
            telegram_api_olacushatcs.send_message(ola_chat_id, message_text)
            telegram_api_olacushatcs.send_message(my_chat_id, message_text)
        elif now == "20:00" and State.last_sent != now:
            State.last_sent = now
            message_text = "Добрейшего вечерочка, ужин это не впадлу"
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
            Print.colored("Bot ola quited", "red")
            ended = True
        except requests.exceptions.ReadTimeout:
            print(f"requests.exceptions.ReadTimeout... {Time.dotted()}")
            Time.sleep(5)
        except requests.exceptions.ConnectionError:
            print(f"requests.exceptions.ConnectionError... {Time.dotted()}")
            Time.sleep(5)

def main():
    # https://www.tutorialspoint.com/python/python_multithreading.htm  # you can expand current implementation

    exitFlag = 0

    print(f"Main thread v{__version__} started")

    threads = []
    thread_id = ID()

    # Create new threads
    thread1 = myThread(thread_id.get(), "Reciever", safe_start_bot, args=(_start_ola_bot_reciever,))
    thread2 = myThread(thread_id.get(), "Sender", safe_start_bot, args=(_start_ola_bot_sender,))
    thread3 = myThread(thread_id.get(), "Sender mine", safe_start_bot, args=(_start_ola_bot_sender_mine,))

    # Start new Threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Add threads to thread list
    threads.append(thread1)
    threads.append(thread2)
    threads.append(thread3)

    import time
    try:
        while 1:
            time.sleep(1)  # wait for KeyboardInterrupt
    except (KeyboardInterrupt, SystemExit):
        Print.colored("\nKilling script", "red")
        Process.kill(os.getpid())

    print("Main thread quited")



if __name__ == '__main__':
    main()
