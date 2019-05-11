import requests
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

__version__ = "0.0.2"


def safe_start_bot(bot_func, skipped_exceptions=(requests.exceptions.ReadTimeout,
                                                 requests.exceptions.ConnectionError,
                                                 requests.exceptions.ChunkedEncodingError)):
    ended = False
    while not ended:
        try:
            bot_func()
            ended = True
        except skipped_exceptions as e:
            print(f"{e} {e.args} {e.with_traceback(e.__traceback__)}... {Time.dotted()}")
            Time.sleep(5)


def very_safe_start_bot(bot_func):
    safe_start_bot(bot_func=bot_func, skipped_exceptions=(requests.exceptions.ReadTimeout,
                                                          requests.exceptions.ConnectionError,
                                                          requests.exceptions.ChunkedEncodingError,
                                                          telebot.apihelper.ApiException))
