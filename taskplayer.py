from commands import *
try:
    import win10toast
except ModuleNotFoundError:
    pass
import datetime
import math


tasks = [
    "",  #0 skip
    "",  #0 skip
    "",  #1 skip
    "",  #1 skip
    "",  #2 skip
    "",  #2 skip
    "",  #3 skip
    "",  #3 skip
    "",  #4 skip
    "",  #4 skip
    "",  #5 skip
    "",  #5 skip
    "",  #6 skip
    "",  #6 skip
    "",  #7 skip
    "wo",  #7
    "pl",  #8
    "wo",  #8
    "io",  #9
    "wo",  #9
    "pl",  #10
    "wo",  #10
    "wo",  #11 skip
    "io",  #11
    "wo",  #12
    "pl",  #12
    "",  #13 skip
    "",  #13 skip
    "wo",  #14 skip
    "wo",  #14
    "io",  #15
    "wo",  #15
    "wo",  #16 skip
    "",  #16 skip
    "",  #17 skip
    "",  #17 skip
    "",  #18 skip
    "",  #18 skip
    "",  #19 skip
    "",  #19 skip
    "",  #20 skip
    "",  #20 skip
    "",  #21 skip
    "",  #21 skip
    "",  #22 skip
    "",  #22 skip
    "",  #23 skip
    "",  #23 skip
]

try:
    n = win10toast.ToastNotifier()
except NameError:
    pass

def notify(text):
    try:
        n.show_toast(
            "test", 
            text, 
            duration = 3, 
            icon_path = None
        )
    except NameError:
        print("\n")
        print(text)
        print()



last_task = None

while True:
    switch_every = 30
    switch_every_seconds = switch_every * 60
    
    now = datetime.datetime.now()
    nearest_minute = (math.floor(now.minute / switch_every) + 1) * switch_every
    nearest_minute = 0 if nearest_minute == 60 else nearest_minute
    nearest_hour = now.hour if nearest_minute != 0 else now.hour + 1

    nearest = now.replace(
        hour = nearest_hour,
        minute = nearest_minute,
        second = 0,
        microsecond = 0
    )
    
    current_task = int((nearest_hour * (60/switch_every) + nearest_minute / switch_every - 1) % len(tasks))
    current_task_name = tasks[current_task]
    
    diff = Time.delta(now, nearest)
    progress = CLI.progressbar(
        switch_every_seconds - diff, 
        switch_every_seconds, 
        f"{current_task_name} {current_task+1}", 
        len(tasks)
    )
    print(progress, end = "", flush=True)
    Time.sleep(5)
    print("\r", end = "")
    
    if last_task != current_task:
        if last_task is not None:
            last_task = current_task
            notify(f"{current_task_name}")
        else:
            last_task = current_task
