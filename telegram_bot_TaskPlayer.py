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
import time
import telegrame

__version__ = "0.7.0"

my_chat_id = 5328715
ola_chat_id = 550959211
tgx_chat_id = 619037205

encrypted_telegram_token_taskplayer = [-14, -18, -50, -16, -61, -56, -42, 1, -21, -13, -40, -6, -40, -27, -26, 39, -16,
                                       50, 12, 50, -21, -58, -17, 36, 29, -14, -60, 41, -27, -56, -7, 58, 41, 31, -56,
                                       33, -12, 12, -19, 48, 42, 4, 8, 47, -34]


telegram_token_taskplayer = Str.decrypt(encrypted_telegram_token_taskplayer, Str.input_pass())

telegram_api_taskplayer = telebot.TeleBot(telegram_token_taskplayer, threaded=False)


class State:
    def __init__(self):
        self.task_dict = {'Work': 1800, 'Home': 1800}
        self.current_task_name = None
        self.current_task_timer = Bench(quiet=True)
        self.current_task_time = 0
        self.current_task_id = ID()
        self.current_task_started = False
        self.current_task_message_id = 0
        self.current_task_halted = True
        self.current_task_halted_hello_message = False

        self.last_sent_mins = 0
        self.last_sent_secs = 0


    def set_task_by_int(self, integer):
        try:
            task = list(self.task_dict.items())[integer]
        except IndexError:
            return False
        self.current_task_name = task[0]
        self.current_task_time = task[1]
        self.current_task_timer.start()
        return True

    def reset_timer(self):
        self.current_task_timer.start()

    def set_first_task(self):
        self.current_task_id.__init__()
        assert self.current_task_id.get() == 0
        self.set_task_by_int(0)

    def set_next_task(self):
        next_task_int = self.current_task_id.get()
        if not self.set_task_by_int(next_task_int):
            self.set_first_task()

    def start_task(self):
        self.current_task_halted = False
        self.reset_timer()

    def set_dict(self, dict_):
        self.task_dict = dict_
        self.set_first_task()


State = State()


def _start_taskplayer_bot_reciever():
    @telegram_api_taskplayer.message_handler(content_types=["text", 'sticker'])
    def reply_all_messages_ola(message):

        if message.chat.id == my_chat_id:
            if message.text:
                print(fr"input: {message.text}")
                if message.text.lower().startswith("help"):
                    reply = "To set todos enter python dict with format like 'dict {'task1': 1800, 'task2': 3600}'" \
                            + newline
                    reply += "To skip task, enter 'skip'" + newline
                    reply += "To start next task enter 'start'" + newline

                elif message.text.lower().startswith("dict "):
                    message.text = message.text[5:]
                    temp_dict = {}
                    try:
                        temp_dict = Dict.from_str(message.text)
                    except (SyntaxError, TypeError, ValueError) as e:
                        print(e)
                        reply = f"Cannot change dict: {str(e)}"
                        telegram_api_taskplayer.send_message(message.chat.id, reply, disable_notification=True)
                    if temp_dict:
                        if not Dict.isinstance_keys(temp_dict, str):
                            temp_dict = Dict.all_keys_lambda(temp_dict, str)
                        State.set_dict(temp_dict)
                    else:
                        reply = f"Cannot set empty {temp_dict} list, return to {State.task_dict}"
                        telegram_api_taskplayer.send_message(message.chat.id, reply, disable_notification=True)
                elif message.text.lower() == "skip":
                    reply = "Trying to skip task"
                    State.set_next_task()
                    message_obj = telegram_api_taskplayer.send_message(message.chat.id, reply, disable_notification=True)
                    State.current_task_message_id = message_obj.message_id
                elif message.text.lower() == "start":
                    reply = "Trying to start task"
                    State.start_task()
                    message_obj = telegram_api_taskplayer.send_message(message.chat.id, reply, disable_notification=True)
                    State.current_task_message_id = message_obj.message_id
                else:
                    reply = "Unknown command, enter 'help'"
                    telegram_api_taskplayer.send_message(message.chat.id, reply, disable_notification=True)
            else:
                reply = "Stickers doesn't supported"
                telegram_api_taskplayer.send_message(message.chat.id, reply, disable_notification=True)

        else:
            telegram_api_taskplayer.forward_message(my_chat_id, message.chat.id, message.message_id,
                                                    disable_notification=True)
            Print.rewrite()
            print(f"from {message.chat.id}: {message.text}")
    telegram_api_taskplayer.polling(none_stop=True)


def _start_taskplayer_bot_sender():
    while True:
        time.sleep(0.2)

        # if State.current_task_halted:
        #     if not State.current_task_halted_hello_message:
        #         message_text = f"Waiting to 'start' task {State.current_task_name}"
        #         message_obj = telegram_api_taskplayer.send_message(my_chat_id, message_text)
        #         State.current_task_message_id = message_obj.message_id
        #         State.current_task_halted_hello_message = True
        #     continue

        time_passed = State.current_task_timer.get()
        seconds_passed = int(time_passed / 1)
        minutes_passed = int(time_passed / 60)
        seconds_all = int(State.current_task_time / 1)
        minutes_all = int(State.current_task_time / 60)
        seconds_left = seconds_all - seconds_passed
        minutes_left = minutes_all - minutes_passed

        if time_passed > State.current_task_time:
            if State.current_task_message_id:
                telegram_api_taskplayer.delete_message(my_chat_id, State.current_task_message_id)
            State.set_next_task()
            State.current_task_started = False
            State.current_task_halted = True
            continue
        if State.current_task_time >= 60:  # minutes mode
            if not State.current_task_started:
                message_text = f"Task {State.current_task_name} started - {minutes_left} minutes"
                message_obj = telegram_api_taskplayer.send_message(my_chat_id, message_text)
                State.current_task_message_id = message_obj.message_id
                State.current_task_started = True
            if minutes_passed != State.last_sent_mins:
                message_text = f"Current task is {State.current_task_name} {minutes_left} minutes left"
                telegram_api_taskplayer.edit_message_text(chat_id=my_chat_id, message_id=State.current_task_message_id,
                                               text=message_text)
                State.last_sent_mins = minutes_passed

        else:  # seconds mode
            if not State.current_task_started:
                message_text = f"Task {State.current_task_name} started - {seconds_left} seconds"
                message_obj = telegram_api_taskplayer.send_message(my_chat_id, message_text)
                State.current_task_message_id = message_obj.message_id
                State.current_task_started = True
            if seconds_passed != State.last_sent_secs:
                message_text = f"Current task is {State.current_task_name} {seconds_left} seconds left"
                telegram_api_taskplayer.edit_message_text(chat_id=my_chat_id, message_id=State.current_task_message_id,
                                               text=message_text)
                State.last_sent_secs = seconds_passed


def safe_threads_run():
    # https://www.tutorialspoint.com/python/python_multithreading.htm  # you can expand current implementation

    print(f"Main thread v{__version__} started")

    threads = Threading()

    threads.add(telegrame.very_safe_start_bot, args=(_start_taskplayer_bot_reciever,), name="Reciever")
    threads.add(telegrame.very_safe_start_bot, args=(_start_taskplayer_bot_sender,), name="Sender")

    threads.start(wait_for_keyboard_interrupt=True)

    Print.rewrite()
    print("Main thread quited")


if __name__ == '__main__':
    safe_threads_run()
