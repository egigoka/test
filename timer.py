from commands import *

end = None
try:
    end = int(OS.args[1])
except ValueError:
    pass

if end is None:
    try:
        end = eval(OS.args[1])
    except SyntaxError:
        pass

if end is None:
    end = OS.args[1]
    if end.endswith("h"):
        end = end.replace("h", "")
        end = int(end) * 3600
    elif end.endswith("m"):
        end = end.replace("m", "")
        end = int(end) * 60

start = Time.stamp()

def seconds_human_readable(seconds):

    if seconds is None:
        return ""

    mins = str(int(seconds / 60)).zfill(2)
    secs = str(int(seconds - int(mins) * 60)).zfill(2)
    return f"{mins}m {secs}s"

try:
    sleep = end / Console.width() / 8 / 3
    sleep = max(sleep, 0.001)
    sleep = min(sleep, 1)
    while True:
        Time.sleep(sleep)
        delta = Time.stamp() - start
        passed = seconds_human_readable(delta)

        endtime = ""
        if end is not None:
            endtime = seconds_human_readable(end)

        print("\r" + CLI.progressbar(delta, end, passed, endtime), end="")

        if delta >= end:
            Console.blink()
            OS.exit(0) 
except KeyboardInterrupt:
    pass
