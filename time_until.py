from commands import *

from pyfiglet import Figlet

fterm = f = Figlet(font="term", justify="center", width=Console.width())

# fonts = Str.nl(File.read("pyfiglet_fonts.txt").strip())

def now():
	return Time.datetime()


end = Str.get_integers(OS.args[1])

endtime = Time.datetime(hour = end[0], minute = end[1], second = 0)

# cnt = Json("time_until_cnt.json")
# if not isinstance(cnt.string, int):
	# cnt.string = 0

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

	if seconds <= 0:
		Console.blink()
		break

	Time.sleep(1)
	
