import multiprocessing
import telegram_bot_todoist

pool_bots = multiprocessing.Pool(processes=2)

pool_entries = [
    pool_bots.apply_async(telegram_bot_todoist.start_ola_bot, args=(), kwds={}),
    pool_bots.apply_async(telegram_bot_todoist.start_todoist_bot, args=(), kwds={}),
]

output = [p.get() for p in pool_entries]