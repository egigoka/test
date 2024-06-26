import time
import os
import pickle
import sys
import datetime
from collections import deque
from commands import Time, Str, Print

CACHE_FOLDER = "cache"

CACHE_FILE = None
CLEAR = False
TIMER = 0
MAX_PERCENT = None
REVERSED = False
PRINT_USAGE = False

if __name__ == "__main__":
    for arg in sys.argv:
        if arg == "--clear" or arg == "--reset" or arg == "--clean":
            CLEAR = True
        elif arg == "--reversed":
            REVERSED = True
        elif arg.startswith("--timer="):
            TIMER = Str.get_integers(arg)[0]
        elif arg.startswith("--max-percent="):
            MAX_PERCENT = Str.get_integers(arg)[0]
        elif arg.startswith("--file="):
            CACHE_FILE = Str.substring(arg, "=") + ".pkl"

    if CACHE_FILE is None:
        print("Save file not specified. Provide with --file={filename}")
        PRINT_USAGE = True
    if MAX_PERCENT is None:
        print("Max percent not specified. Provide with --max-percent={max percent}")
        PRINT_USAGE = True

    if PRINT_USAGE:
        print(f"usage: python3 {__file__} --file={{filename}} "
              f"--max-percent={{max percent}} [--clear] [--reversed] [--timer={{timer}}]")
        sys.exit(1)


class TaskProgress:
    def __init__(self, max_percent=MAX_PERCENT, window_size=5):
        self.max_percent = max_percent
        self.history = deque(maxlen=window_size)
        self.start_time = time.time()
        self.last_time = self.start_time
        self.prev_time = self.start_time

    def get_diff(self):
        return self.last_time - self.prev_time

    def add_progress(self, percent):
        current_time = time.time()
        self.history.append((current_time, percent))
        self.prev_time = self.last_time
        self.last_time = current_time

    def get_avg_speed(self):
        if len(self.history) < 2:
            return None

        delta_time = self.history[-1][0] - self.history[0][0]
        delta_percent = self.history[-1][1] - self.history[0][1]

        if delta_time == 0:
            return None
        
        return delta_percent / delta_time

    def estimate_completion(self):
        speed = self.get_avg_speed()
        if speed is None:
            return None
        
        remaining_percent = self.max_percent - self.history[-1][1]
        try:
            estimate = self.last_time + (remaining_percent / speed)
        except ZeroDivisionError:
            day = 3600*24
            estimate = self.last_time + day*360*101 + day*30*4 + day*7*3
        return estimate

    def save(self, filename):
        try:
            file = open(filename, "wb")
        except FileNotFoundError:
            if not os.path.exists("cache"):
                os.makedirs("cache")
            file = open(filename, "wb")
        try:
            pickle.dump(self, file)
            file.close()
        finally:
            file.close()
        
    @classmethod
    def load(cls, filename):
        with open(filename, "rb") as file:
            return pickle.load(file)


def str_datetime():
    return str(datetime.datetime.now())[:19]


def print_progress(progress_tracker):
    estimated_completion = progress_tracker.estimate_completion()

    if not estimated_completion:
        output = "Not enough data to estimate completion time."
        print(str_datetime(), output, end="")
        return 

    estimated_time_left = estimated_completion - time.time()
    estimated_time_left = int(estimated_time_left)
    percent_left = ""
    if progress_tracker.max_percent != 100:
        percent_left = progress_tracker.max_percent - progress_tracker.history[-1][1]
        percent_left = percent_left / (progress_tracker.max_percent / 100)

        percent_left = f"({percent_left:.0f}%) "

    diff = progress_tracker.get_diff()

    output = (f"| Left {percent_left}: {Time.human_readable(estimated_time_left)}"
              f" | Completion: {time.ctime(estimated_completion)}"
              f" | Speed: {progress_tracker.get_avg_speed()*60:.2f} %/m,"
              f" | Diff: {Time.human_readable(int(diff))}")

    print(str_datetime(), output, end="")


def main():
    
    if CLEAR and os.path.exists(CACHE_PATH):
        os.remove(CACHE_PATH)
    
    try:
        progress_tracker = TaskProgress.load(CACHE_PATH)
        progress_tracker.max_percent = MAX_PERCENT
        progress_tracker.save(CACHE_PATH)
    except (FileNotFoundError, EOFError):
        progress_tracker = TaskProgress(max_percent=MAX_PERCENT)  # Example: custom max percent

    print_progress(progress_tracker)
    print()
    while True:
        percent_input = None
        try:
            Print.colored("Enter the percentage of task completed: ", "green", end="", flush=True)
            percent_input = input()
            percent = float(percent_input)

            if REVERSED:
                percent = progress_tracker.max_percent - percent

            progress_tracker.add_progress(percent)

            print_progress(progress_tracker)

            if percent >= progress_tracker.max_percent:
                print(f" | Task completed!")
                break
            else:
                print()

            progress_tracker.save(CACHE_PATH)
            Time.sleep(TIMER, verbose=True)

        except ValueError:
            if percent_input.strip() == "q":
                print("Exiting.")
                sys.exit(0)
            elif percent_input.strip() == "r":
                print("Resetting progress.")
                progress_tracker = TaskProgress(max_percent=MAX_PERCENT)
                progress_tracker.save(CACHE_PATH)
                continue
                
            print("Please enter a valid percentage.")
        except KeyboardInterrupt:
            print("Exiting.")
            break


if __name__ == "__main__":
    CACHE_PATH = CACHE_FOLDER + os.sep + CACHE_FILE
    main()
