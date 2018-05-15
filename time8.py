#! python3
# -*- coding: utf-8 -*-
# http://python.su/forum/topic/15531/?page=1#post-93316
from os8 import OS
from str8 import Str
__version__ = "0.0.5"
class Time:

    @staticmethod
    def stamp():
        import time
        return time.time()


    @staticmethod
    def get(size, zfill=0):
        return Str.leftpad(eval("str(datetime.datetime.now()." + size + ")"), leng=zfill, ch=0)


    @classmethod
    def dotted(Time):
        dateandtime = Time.get("year") + "." + Time.get("month", 2) + "." + \
                      Time.get("day", 2) + "_at_" + Time.get("hour", 2) + "." + \
                      Time.get("minute", 2) + "." + Time.get("second", 2) + "." + \
                      Time.get("microsecond", 6)
        return dateandtime


    @staticmethod
    def timestamp_to_datetime(timestamp):
        if isinstance(timestamp, datetime.datetime):
            return timestamp
        return datetime.datetime.fromtimestamp(timestamp)


    @staticmethod
    def datetime_to_timestamp(datetime_object):
        import time
        return time.mktime(datetime_object.timetuple())


    @classmethod
    def rustime(Time, customtime=None):
        if customtime:
            time = Time.timestamp_to_datetime(customtime)
        else:
            time = datetime.datetime.now()
        def lp(string): return Str.leftpad(string, 2, 0)
        rustime = lp(time.day) + " числа " \
        + lp(time.month) + " месяца " \
        + lp(time.year) + " года в " \
        + lp(time.hour) + ":" + lp(time.minute) + ":" + lp(time.second)
        if not OS.cyrillic_support:
            rustime = Time.dotted()
        return rustime

    @staticmethod
    def timer(seconds, check_per_sec=10):
        Countdown = get_Bench()
        Countdown.start()
        secs_second_var = int(seconds)
        while Countdown.get() < seconds:
            import time
            time.sleep(1/check_per_sec)
            secs_left_int = int(seconds - Countdown.get())
            if secs_left_int != secs_second_var:
                secs_second_var = secs_left_int
                Print.rewrite("Timer for " + str(seconds) + " seconds. " + str(secs_left_int) + " left")
        Print.rewrite("")

    @classmethod
    def sleep(Time, seconds, quiet=False):
        if seconds < 0:
            raise ValueError("sleep length must be non-negative")
        elif seconds >= 1:
            Time.timer(seconds)
        else:
            if not quiet:
                print("sleeping", seconds)
            import time
            time.sleep(seconds)

    @classmethod
    def delta(Time, time_a, time_b):  # return difference between two timestamps
        if time_a > time_b: time_a, time_b = time_b, time_a
        time_a = Time.timestamp_to_datetime(time_a)
        time_b = Time.timestamp_to_datetime(time_b)
        delta = time_b - time_a
        delta_combined = delta.seconds + delta.microseconds / 1E6
        return delta_combined
