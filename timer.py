from commands import *

try:
	end = int(OS.args[1])
except ValueError:
    end = eval(OS.args[1])

start = Time.stamp()

def seconds_human_readable(seconds):

	if seconds is None:
		return ""

	mins = str(int(seconds / 60)).zfill(2)
	secs = str(int(seconds - int(mins) * 60)).zfill(2)
	return f"{mins}m {secs}s"

while True:
	Time.sleep(0.5)
	delta = Time.stamp() - start
	passed = seconds_human_readable(delta)

	endtime = ""
	if end is not None:
		endtime = " / " + seconds_human_readable(end)
	
	Print.rewrite(f"{passed}{endtime}")

	if delta >= end:
		Console.blink()
		OS.exit(0) 
