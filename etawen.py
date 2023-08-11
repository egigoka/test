import time
import os
import pickle
from collections import deque
from commands import Time


class TaskProgress:
    def __init__(self, max_percent=100, window_size=5):
        self.max_percent = max_percent
        self.history = deque(maxlen=window_size)
        self.start_time = time.time()
        self.last_time = self.start_time

    def add_progress(self, percent):
        current_time = time.time()
        self.history.append((current_time, percent))
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
            estimate = self.last_time + 3600*24*360*100
        return estimate

    def save(self, filename="cache" + os.sep + "etawen.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def load(cls, filename="cache" + os.sep + "etawen.pkl"):
        with open(filename, "rb") as file:
            return pickle.load(file)


def print_progress(progress_tracker):
    estimated_completion = progress_tracker.estimate_completion()
    if estimated_completion:
        estimated_time_left = estimated_completion - time.time()
        print(f"Estimated time left: {Time.human_readable(estimated_time_left)}")
        print(f"Estimated completion time: {time.ctime(estimated_completion)}")
    else:
        print("Not enough data to estimate completion time.")


def main():
    try:
        progress_tracker = TaskProgress.load()
    except (FileNotFoundError, EOFError):
        progress_tracker = TaskProgress(max_percent=100)  # Example: custom max percent

    print_progress(progress_tracker)
    while True:
        try:
            percent = float(input("Enter the percentage of task completed: "))
            if percent >= progress_tracker.max_percent:
                print("Task completed!")
                break

            progress_tracker.add_progress(percent)

            print_progress(progress_tracker)

            progress_tracker.save()
            time.sleep(60)  # Wait for a minute

        except ValueError:
            print("Please enter a valid percentage.")
        except KeyboardInterrupt:
            print("Exiting.")
            break


main()
