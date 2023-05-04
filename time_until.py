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

	while True:
		if new_endtime < last_endtime:
			new_endtime = new_endtime + timedelta(days=1)
		else:
			break
	
	endtimes.append(new_endtime)

	last_endtime = new_endtime

#debug
# for endtime in endtimes:
	# print(endtime)
#debug END

endtimes.sort()

#debug
# print()
# for endtime in endtimes:
	# print(endtime)
#debug END

# cnt = Json("time_until_cnt.json")
# if not isinstance(cnt.string, int):
	# cnt.string = 0

while True:
	Console.clean()
	for endtime in endtimes:
		time = now()

		# Print.debug(f"{endtime=}")
		# Print.debug(f"{time=}")
		
		if endtime < time:
			continue
		
		seconds = int((endtime-time).total_seconds())
		# Print.debug(f"{seconds=}")
		human_readable = Time.human_readable(seconds)
		# Print.debug(f"{human_readable=}")

		# font = Random.item(fonts)
		# try:
			# font = fonts[cnt.string]
		# except IndexError:
			# cnt.string = 0
			# font = fonts[cnt.string]
		# font = "minecraft"
		font = "minecraft_condenced"
		
		# cnt.string += 1
		# cnt.save()
		
		# print(fterm.renderText(f"{font} {cnt.string}/{len(fonts)}"))
		# print(fterm.renderText(f"{font}"))

		f = Figlet(font=font, justify="center", width=Console.width())

		until = f"{endtime.hour}:{endtime.minute}"
		
		if endtime.day != time.day:
			until = f"{endtime.day:02}.{endtime.month:02} {until}"
		
		print(f.renderText(f"{human_readable} until {until}").rstrip())

		# if seconds <= 0:
			# Console.blink()
			# break
	# OS.exit(1)
	Time.sleep(1)
	
