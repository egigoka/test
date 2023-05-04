from commands import *
from pyfiglet import Figlet
from datetime import timedelta

fterm = f = Figlet(font="term", justify="center", width=Console.width())

# fonts = Str.nl(File.read("pyfiglet_fonts.txt").strip())

def now():
	return Time.datetime()


ends = []

for arg in OS.args[1:]:
	ends.append(arg)

if not ends:
	print("No times given, exit")

endtimes = []

last_endtime = Time.datetime(year=1970)

for end in ends:

	end = Str.get_integers(end)
	
	new_endtime = Time.datetime(hour = end[0], minute = end[1], second = 0)

	if new_endtime < last_endtime:
		new_endtime = new_endtime.replace(day=last_endtime.day + 1)
	
	endtimes.append(new_endtime)

	last_endtime = new_endtime

endtimes.sort()

# cnt = Json("time_until_cnt.json")
# if not isinstance(cnt.string, int):
	# cnt.string = 0

for endtime in endtimes:
	while True:
	
		Print.rewrite()
		seconds = (endtime-now()).seconds
		human_readable = Time.human_readable(seconds)

		# font = Random.item(fonts)
		# try:
			# font = fonts[cnt.string]
		# except IndexError:
			# cnt.string = 0
			# font = fonts[cnt.string]
		font = "minecraft"

		# cnt.string += 1
		# cnt.save()
		
		# print(fterm.renderText(f"{font} {cnt.string}/{len(fonts)}"))
		# print(fterm.renderText(f"{font}"))

		Console.clean()
		
		f = Figlet(font=font, justify="center", width=Console.width())
		
		print(f.renderText(human_readable))
		print(f.renderText(f"until {endtime.hour}:{endtime.minute}"))

		if seconds <= 0:
			Console.blink()
			break

		Time.sleep(1)
	
