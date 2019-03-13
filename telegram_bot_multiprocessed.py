import multiprocessing
import telegram_bot_temp

pool_bots = multiprocessing.Pool(processes=2)

pool_entries = [
    pool_bots.apply_async(telegram_bot_temp.start_ola_bot, args=(), kwds={}),
    pool_bots.apply_async(telegram_bot_temp.start_todoist_bot, args=(), kwds={}),
]

output = [p.get() for p in pool_entries]