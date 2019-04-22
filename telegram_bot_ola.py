#! python3
# -*- coding: utf-8 -*-
import sys
import os
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

__version__ = "1.0.0"

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
        now = datetime.datetime.now()
        now = now.strftime("%H:%M")
        Time.sleep(20)
        if now == "08:00" and State.last_sent != now:
            State.last_sent = now
            telegram_api_olacushatcs.send_message(ola_chat_id, "Позавтрокой, пожалуйсто")
            telegram_api_olacushatcs.send_message(my_chat_id, "Позавтрокой, пожалуйсто")
        elif now == "14:00" and State.last_sent != now:
            State.last_sent = now
            telegram_api_olacushatcs.send_message(ola_chat_id, "Не зобудь про обед")
            telegram_api_olacushatcs.send_message(my_chat_id, "Не зобудь про обед")
        elif now == "20:00" and State.last_sent != now:
            State.last_sent = now
            telegram_api_olacushatcs.send_message(ola_chat_id, "Поужинать тоже немножечко надо")
            telegram_api_olacushatcs.send_message(my_chat_id, "Поужинать тоже немножечко надо")


def safe_start_bot(bot_func):
    ended = False
    while not ended:
        try:
            Print.colored("Bot ola started", "green")
            bot_func()
            Print.colored("Bot ola ended", "green")
            ended = True
        except requests.exceptions.ReadTimeout:
            print(f"requests.exceptions.ReadTimeout... {Time.dotted()}")
            Time.sleep(5)
        except requests.exceptions.ConnectionError:
            print(f"requests.exceptions.ConnectionError... {Time.dotted()}")
            Time.sleep(5)


def main():
    # https://www.tutorialspoint.com/python/python_multithreading.htm
    import threading
    import time

    exitFlag = 0

    class myThread(threading.Thread):
        def __init__(self, threadID, name, counter):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.counter = counter

        def setup(self, func, args=(), kwargs={}):
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

    threads = []

    # Create new threads
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)

    # config new threads
    thread1.setup(safe_start_bot, args=(_start_ola_bot_reciever,))
    thread2.setup(safe_start_bot, args=(_start_ola_bot_sender,))

    # Start new Threads
    thread1.start()
    thread2.start()

    # Add threads to thread list
    threads.append(thread1)
    threads.append(thread2)

    # Wait for all threads to complete
    try:
        while 1:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        Print.colored("\nKilling script", "red")
        Process.kill(os.getpid())


if __name__ == '__main__':
    main()



#if __name__ == '__main__':
#        main()
