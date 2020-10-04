from commands import *
from commands.mouse9 import Mouse

__version__ = "2.8.3"

PRINT_START_FINISH = False
PRINT_DIMENSIONAL_SACRIFICE = False

SLEEP_BETWEEN_MOUSE_CLICKS = 0.1

DISABLE_DS_AM_AT_INFINITY_PERCENT = 100  # this is managed automatically since 2.5.0
DISABLE_DS_AM_BEFORE_THIS_SECONDS_BEFORE_INFINITY = 240

print(f"antimatter v{__version__}")


class Logger:
	def __init__(self, prefix, verbose=True):
		self.check_every = 3
		self.previous_value = None
		self.value_change_time = Time.stamp()
		self.prefix = prefix
		self.verbose = verbose

	def _set_new_value(self, new_value):
		self.previous_value = new_value
		self.value_change_time = Time.stamp()

	def check(self, new_value):
		single_change_time = 0
		# first run
		if self.previous_value is None:
			self._set_new_value(new_value)
			Print.rewrite()
			if self.verbose:
				print(f"{self.prefix} started as {self.previous_value}")
		# usual case
		elif new_value > self.previous_value:
			changed_by = new_value - self.previous_value
			time_passed = Time.delta(self.value_change_time, Time.stamp())
			single_change_time = time_passed/changed_by
			Print.rewrite()
			if self.verbose:
				for i in range(changed_by):
					print(f"{self.prefix} {self.previous_value + i + 1} in {single_change_time:.2f}s")
			self._set_new_value(new_value)
		# new value 50% lower than previous
		elif new_value <= self.previous_value*0.5:
			self._set_new_value(new_value)
			global LOGGER_LAST_RESET
			if Time.delta(LOGGER_LAST_RESET, Time.stamp()) > 5:
				if self.verbose:
					print()
				LOGGER_LAST_RESET = Time.stamp()
			if self.verbose:
				print(f"{self.prefix} reset to {self.previous_value}")
		return single_change_time


def get_info_from_screen():
	if PRINT_START_FINISH: print("start text capturing")
	with LOCK_TEXT_CAPTURING:
		Mouse.Click.left(position=(Random.integer(100,200), Random.integer(100,200)), quiet=True)
		Keyboard.hotkey("ctrl", "a")
		# Time.sleep(1)
		Keyboard.hotkey("ctrl", "c")
		# Time.sleep(1)
		stats = paste()
		stats = Str.nl(stats)
		Time.sleep(SLEEP_BETWEEN_MOUSE_CLICKS)
		Mouse.Click.left(position=(Random.integer(100,200), Random.integer(100,200)), quiet=True)
	if PRINT_START_FINISH: print("end text capturing")
	return stats


# добавить функционал выбора времени, а не количества запусков
get_info_from_screen = CachedFunction(get_info_from_screen, 1, quiet=True)


def logger_antimatter():
	while True:
		if PRINT_START_FINISH: print("start antimatter logger")
		with LOCK_KEYBOARD_MOUSE:
			info = get_info_from_screen()
		if "antimatter" in info[2]:
			am_string = info[2]
		elif "antimatter" in info[3]:
			am_string = info[3]
		else:
			print("cannot get antimatter string")
			continue

		try:
			am_string = Str.substring(am_string, "You are getting ", " antimatter per second.")
		except KeyError:
			print("cannot get antimatter power")
			continue

		try:
			am_float, am_power = Str.get_integers(am_string, float_support=True)
		except ValueError:
			try:
				am_int = Str.get_integers(am_string, float_support=True)[0]
			except IndexError:
				print("cannot get antimatter power simple")
				continue
			am_power = len(str(float(am_int)))-1

		LOGGER_ANTIMATTER.check(am_power)
		if PRINT_START_FINISH: print("end antimatter logger")
		Time.sleep(LOGGER_ANTIMATTER.check_every, verbose=False)


def get_infinity_int():
	if PRINT_START_FINISH: print("start getting infinity_int")
	infinity_int = None
	with LOCK_KEYBOARD_MOUSE:
		info = get_info_from_screen()
	try:
		if "%" in info[-1]:
			infinity_string = info[-1]
		elif "%" in info[-2]:
			infinity_string = info[-2]
		else:
			print("cannot get infinity string")
	except IndexError:
		print("cannot get text infinity")

	try:
		infinity_int = int(float(infinity_string[:-1]))
	except ValueError:
		pass
	except NameError:
		pass
	return infinity_int


def logger_infinity():
	while True:
		if PRINT_START_FINISH: print("start infinity logger")

		infinity_int = get_infinity_int()
		if infinity_int is not None:
			single_infinity_percent_time = LOGGER_INFINITY_PERCENTAGE.check(infinity_int)
			global DISABLE_DS_AM_AT_INFINITY_PERCENT
			try:
				DISABLE_DS_AM_AT_INFINITY_PERCENT = 100 - DISABLE_DS_AM_BEFORE_THIS_SECONDS_BEFORE_INFINITY/single_infinity_percent_time
			except ZeroDivisionError:
				pass

		if PRINT_START_FINISH: print("end infinity logger")

		Time.sleep(LOGGER_INFINITY_PERCENTAGE.check_every, verbose=False)


def logger_infinity_points():
	while True:
		if PRINT_START_FINISH: print("start infinity points logger")
		with LOCK_KEYBOARD_MOUSE:
			info = get_info_from_screen()
		if "Infinity points" in info[0]:
			infinity_string = info[0]
		elif "Infinity points" in info[1]:
			infinity_string = info[1]
		else:
			print("cannot get infinity points string")
			continue

		try:
			infinity_string = Str.substring(infinity_string, "You have ", " Infinity points.")
		except KeyError:
			print("cannot get infinity points power")
			continue

		try:
			ip_float, ip_power = Str.get_integers(infinity_string, float_support=True)
			ip_int = int(ip_float * (10 ** ip_power))
		except ValueError:
			try:
				ip_int = Str.get_integers(infinity_string, float_support=True)[0]
			except IndexError:
				print("cannot get infinity points power simple")
				continue

		LOGGER_INFINITY_POINTS.check(ip_int)
		if PRINT_START_FINISH: print("end infinity points logger")
		Time.sleep(LOGGER_INFINITY_POINTS.check_every, verbose=False)


def buyer():
	while True:
		if PRINT_START_FINISH: print("start buying")
		infinity_int = get_infinity_int()
		with LOCK_KEYBOARD_MOUSE:
			Keyboard.hotkey("c", verbose=False)  # big crunch
			Keyboard.hotkey("t", verbose=False)  # tickspeed
			Keyboard.hotkey("t", verbose=False)  # tickspeed
			Keyboard.hotkey("t", verbose=False)  # tickspeed
			Keyboard.hotkey("t", verbose=False)  # tickspeed
			Keyboard.hotkey("t", verbose=False)  # tickspeed
			if infinity_int is not None:
				if infinity_int < DISABLE_DS_AM_AT_INFINITY_PERCENT:
					Keyboard.hotkey("g", verbose=False)  # antimatter galaxy
					Keyboard.hotkey("d", verbose=False)  # dimension shift
			keys = Int.from_to(1, 8, to_str=True)
			keys.reverse()
			for i in keys:  # buy dimensions (from bigger to smaller) todo: determine max dimension and buy it
				Keyboard.hotkey(i)
				Keyboard.hotkey("shift", i)
			Keyboard.hotkey("m", verbose=False)  # max all
		if PRINT_START_FINISH: print("end buying")
		Time.sleep(1)


def dimensional_sacrifice():
	while True:
		if PRINT_START_FINISH: print("start check for sacrificing")
		with LOCK_KEYBOARD_MOUSE:
			stats = get_info_from_screen()
		try:
			dimensional_sacrifice_multiplier = stats[9]
		except IndexError:
			print("cannot find dimensional sacrifice multiplier")
			continue
		try:
			dimensional_sacrifice_multiplier = Str.substring(dimensional_sacrifice_multiplier, "(", "x)")
			dimensional_sacrifice_multiplier = float(dimensional_sacrifice_multiplier)
			Print.rewrite(f"{Time.dotted()[:-10]} DS x{dimensional_sacrifice_multiplier}")
			if dimensional_sacrifice_multiplier >= 2:
				with LOCK_KEYBOARD_MOUSE:
					Keyboard.hotkey("s")
				Print.rewrite()
				if PRINT_DIMENSIONAL_SACRIFICE:
					print(f"used dimensional sacrifice x{dimensional_sacrifice_multiplier}")
		except KeyError:
			print("cannot find dimensional sacrifice multiplier precisely")
		if PRINT_START_FINISH: print("end checking for sacrificing")
		Time.sleep(10, verbose=False)


LOGGER_ANTIMATTER = Logger("am power")
LOGGER_INFINITY_PERCENTAGE = Logger("% of infinity", verbose=False)
LOGGER_INFINITY_POINTS = Logger("infinity points")

LOGGER_LAST_RESET = Time.stamp()

LOCK_KEYBOARD_MOUSE = Lock()
LOCK_TEXT_CAPTURING = Lock()


t = Threading()
t.add(buyer)
t.add(dimensional_sacrifice)
# t.add(logger_antimatter)
t.add(logger_infinity)
t.add(logger_infinity_points)

t.start(wait_for_keyboard_interrupt = True)


example = '''You have 0 Infinity points.
You have 7.54e12 antimatter.

You are getting 9.91e11 antimatter per second.
Reduce the tick interval by 14%.
Cost: 1e14 Buy Max
Tickspeed: 190
Dimensions Options Statistics Achievements Challenges Infinity
DimensionsProduction
Dimensional Sacrifice (1.00x) Max all (M)
First Dimension x110.4	
1.71e9 (0) (+2.46%/s)
Cost: 1e13	Until 10, Cost: 1e14
Second Dimension x26.3	
3.04e6 (0) (+1.10%/s)
Cost: 1e14	Until 10, Cost: 1e15
Third Dimension x6.6	
9.67e3 (0) (+5.21%/s)
Cost: 1e14	Until 10, Cost: 1e15
Fourth Dimension x6.6	
147 (0) (+11.76%/s)
Cost: 1e18	Until 10, Cost: 1e19
Fifth Dimension x3.3	
10 (0) (+0.00%/s)
Cost: 1e17	Until 10, Cost: 1e18
Sixth Dimension x1.6	
0 (0) (+0.00%/s)
Cost: 1e13	Until 10, Cost: 1e14
Dimension Shift (2): requires 20 Sixth Dimensions	Reset the game for a new Dimension
Antimatter Galaxies (2): requires 200 Eighth Dimensions	Lose all your previous progress, but get a tickspeed boost
How to play | Donate | Changelog | Discord | Subreddit | Savefixer
4.18%
Game saved'''