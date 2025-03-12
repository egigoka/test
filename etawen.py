import time
import os
import pickle
import sys
import datetime
import argparse
from collections import deque
from commands import Time, Str, Print

CACHE_FOLDER = "cache"
DEFAULT_TIMER = 0

def parse_arguments():
    parser = argparse.ArgumentParser(description="Task Progress Tracker")
    parser.add_argument("--file", required=True, help="Filename for saving progress")
    parser.add_argument("--max-percent", type=int, required=True, help="Maximum percentage for the task")
    parser.add_argument("--reversed", action="store_true", help="Reverse progress calculation")
    parser.add_argument("--timer", type=int, default=DEFAULT_TIMER, help="Timer duration between inputs")
    parser.add_argument("--no-powerline", action="store_true", help="Don't use powerline fonts")
    
    args = parser.parse_args()
    
    args.cache_file = args.file + ".pkl"
    args.cache_path = os.path.join(CACHE_FOLDER, args.cache_file)
    
    return args

if __name__ == "__main__":
    args = parse_arguments()


class TaskProgress:
    WINDOW_SIZE = 5
    SECONDS_PER_DAY = 86400
    DAYS_IN_YEAR = 365
    DAYS_IN_MONTH = 30
    DAYS_IN_WEEK = 7

    def __init__(self, max_percent):
        self.max_percent = max_percent
        self.history = deque(maxlen=self.WINDOW_SIZE)
        self.start_time = time.time()
        self.last_time = self.start_time
        self.prev_time = self.start_time

    def get_diff(self):
        return self.last_time - self.prev_time

    def add_progress(self, percent):
        current_time = time.time()
        self.history.append((current_time, percent))
        self.prev_time, self.last_time = self.last_time, current_time

    def get_avg_speed(self):
        if len(self.history) < 2:
            return None

        delta_time = self.history[-1][0] - self.history[0][0]
        delta_percent = self.history[-1][1] - self.history[0][1]

        return delta_percent / delta_time if delta_time != 0 else None

    def estimate_completion(self):
        speed = self.get_avg_speed()
        if speed is None:
            return None
        
        remaining_percent = self.max_percent - self.history[-1][1]
        try:
            estimate = self.last_time + (remaining_percent / speed)
        except ZeroDivisionError:
            estimate = self.last_time + self.SECONDS_PER_DAY * self.DAYS_IN_YEAR * 100
        return estimate

    def save(self, filename):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "wb") as file:
            pickle.dump(self, file)
        
    @classmethod
    def load(cls, filename):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return None


def str_datetime():
    return datetime.datetime.now().strftime("%d %H:%M:%S")
    


def print_progress(progress_tracker):
    estimated_completion = progress_tracker.estimate_completion()

    if not estimated_completion:
        print(f"{str_datetime()} Not enough data to estimate completion time.", end="")
        return 

    estimated_time_left = int(estimated_completion - time.time())
    current_percent = progress_tracker.history[-1][1]
    percent_left = progress_tracker.max_percent - current_percent
    percent_left_formatted = f"({percent_left / (progress_tracker.max_percent / 100):.0f}%) " if progress_tracker.max_percent != 100 else ""

    diff = progress_tracker.get_diff()
    
    speed = progress_tracker.get_avg_speed() * 60

    if speed >= 1:
        speed_suffix = " %/m"
        speed_value = f"{speed:.2f}"
    elif speed == 0:
        speed_suffix = ""
        speed_value = 0
    else:
        speed_suffix = "/%"
        speed = 1/speed
        speed_value = f"{int(speed)}m {str(int(speed*60%60)).zfill(2)}s"


    completed = datetime.datetime.fromtimestamp(estimated_completion)
    now = Time.timestamp_to_datetime(progress_tracker.last_time)
    if completed.day != now.day:
        completed_formatted = completed.strftime('%d %H:%M:%S')
    elif completed.hour != now.hour:
        completed_formatted = completed.strftime('%H:%M:%S')
    else:
        completed_formatted = completed.strftime('%M:%S')
    
    speed_formatted = f"{speed_value}{speed_suffix}"

    if args.no_powerline:
        output = (f"{str_datetime()} "
                  f"| Lft {percent_left_formatted}{Time.human_readable(estimated_time_left)}"
                  f" | Cmp: {completed_formatted}"
                  f" | Spd: {speed_formatted}"
                  f" | Dif: {Time.human_readable(int(diff))}")
    else:
        start = chr(57522)
        end = chr(57520)
        
        output = start
        output += Print.colored(str_datetime(), "white", "on_black", verbose=False)
        output += end
        output += f"Lft {percent_left_formatted}{Time.human_readable(estimated_time_left)}".rstrip()
        output += start
        output += Print.colored(f"Cmp {completed_formatted}", "white", "on_black", verbose=False)
        output += end
        output += f"Spd {speed_formatted}"
        output += start
        output += Print.colored(f"Dif {Time.human_readable(int(diff))}", "white", "on_black", verbose=False)
        output += end

    print(output, end="")


def main(args):
    
    progress_tracker = TaskProgress.load(args.cache_path)
    if progress_tracker is None:
        progress_tracker = TaskProgress(max_percent=args.max_percent)
    else:
        progress_tracker.max_percent = args.max_percent
    
    progress_tracker.save(args.cache_path)

    print_progress(progress_tracker)
    print()

    while True:
        try:
            Print.colored("Enter the percentage of task completed: ", "green", end="", flush=True)
            percent_input = input().strip().lower()

            if percent_input == 'q':
                print("Exiting.")
                break
            elif percent_input == 'r':
                print("Resetting progress.")
                progress_tracker = TaskProgress(max_percent=args.max_percent)
                progress_tracker.save(args.cache_path)
                continue

            percent = float(percent_input)
            if args.reversed:
                percent = args.max_percent - percent

            progress_tracker.add_progress(percent)
            print_progress(progress_tracker)

            if percent >= args.max_percent:
                print(" | Task completed!")
                break
            else:
                print()

            progress_tracker.save(args.cache_path)
            Time.sleep(args.timer, verbose=True)

        except ValueError:
            print("Please enter a valid percentage.")
        except KeyboardInterrupt:
            print("\nExiting.")
            break

if __name__ == "__main__":
    args = parse_arguments()
    main(args)
