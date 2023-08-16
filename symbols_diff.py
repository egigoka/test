from commands import *

qq = q

for sym in "qwertyuiopasdfghjklzxcvbnm":
	exec(f"{sym} = ord('{sym}')")


def sleep(minutes):
	try:
		Time.sleep(60*minutes, verbose=True)
	except KeyboardInterrupt:
		Print.rewrite()


def diff(sym, symb):
	number = int((sym+symb) / 2)
	char = chr(number)
	if number == sym:
		return(f"same as first({char})")
	return(char)

dd = diff
