from commands import *
import os
import time  # debug
import shutil  # debug


def file_move(file, root, path1, path2, state):
    filepath = Path.combine(root, file)
    filepath2 = filepath.replace(path1, path2, 1)

    try:
        Dir.create(Path.get_parent(filepath2))
    except PermissionError as e:
        Print.colored(f"Dir '{Path.get_parent(filepath2)}' cannot be created: {e}", "red")
    
    filesize = File.get_size(filepath)
    free_space = Dir.get_free_space(Path.get_parent(filepath2))
    if filesize > free_space:
        raise OSError(f"Not enough free space to move '{filepath}' to '{filepath2}'")

    state.last_file = filepath
    state.last_file2 = filepath2

    try:
        shutil.move(filepath, filepath2)
    except OSError as e:
        if e.errno == 28:
            File.delete(e.filename2)
        else:
            raise
    state.count_of_scanned_files += 1
    state.previous_size = 0


class State:
    def __init__(self, path):
        self.last_file = None
        self.last_file2 = None
        try:
            self.count_of_all_files = Dir.number_of_files(path)
        except FileNotFoundError:
            self.count_of_all_files = 1
        self.count_of_scanned_files = 0

        self.previous_size = 0
        self.speed_bench = Bench()


def printer(state):
    while True:
        try:
            current_size = File.get_size(state.last_file2)
        except (TypeError, FileNotFoundError):
            current_size = 0
        try:
            percent_file = round((current_size/File.get_size(state.last_file))*100, 2)
        except (TypeError, FileNotFoundError):
            percent_file = 0.0
        percent_all = round(((state.count_of_scanned_files/state.count_of_all_files)*100) + percent_file/state.count_of_all_files, 2)
        # "%.2f" % 1.1 == 1.10

        time_delta = state.speed_bench.end()
        size_diff = 0
        if current_size > state.previous_size:
            size_diff = round((current_size - state.previous_size), 4)
        if float(size_diff) < 0.0001:
            size_diff = 0
        speed = round(size_diff / time_delta, 2)

        # # debug
        if float(speed/MiB) > 200:
            Print.rewrite()
            Print.colored(f"""{time_delta=}
{current_size=}
{state.previous_size=}
{current_size > state.previous_size=}
{float(size_diff) < 0.0001=}
{size_diff/MiB=}
{speed/MiB=}
{(current_size - state.previous_size)/MiB=}
""", "red")

        try:
            size_left = Dir.get_size(path1) - current_size
        except FileNotFoundError:
            try:
                size_left = File.get_size(path1) - current_size
            except FileNotFoundError:
                size_left = 0
        try:
            remaining_time = size_left/float(speed)
            remaining_seconds = int(remaining_time % 60)
            remaining_minutes = int(remaining_time // 60)

            # # debug
            # Print.rewrite()
            # Print("remaining_time", remaining_time,
            #       "remaining_seconds", remaining_seconds,
            #       "remaining_minutes", remaining_minutes)

            remaining_time_str = f"{remaining_minutes}:{str(remaining_seconds).zfill(2)}"
        except ZeroDivisionError:
            remaining_time_str = "Unknown"

        Print.rewrite(f"{CLI.wait_update(quiet=True)} [{series_cnt}/{len(series_names)}] {percent_all}% ({state.count_of_scanned_files}/"
                      f"{state.count_of_all_files}). Speed: {round(speed/MiB, 2)}MB/s. Remaining: {remaining_time_str}", state.last_file)

        state.previous_size = current_size
        time.sleep(2)

from_folder = Path.combine("Volumes", "HDD2")
to_folder = Path.combine("Users", "mac", "HDD2")

#series_names = """One Punch Man"""
#series_names = Str.nl(series_names)
series_names = []
for root, dirs, files in OS.walk(from_folder):
	series_names += dirs+files

#series_names = Dir.list_of_entries(Path.combine(from_folder, "Series"))
#series_names += Dir.list_of_entries(Path.combine(from_folder, "Films"))

# from_folder, to_folder = to_folder, from_folder

#subfolders = ["Series", "Films"]
subfolders = Dir.list_of_dirs(from_folder)

if __name__ == '__main__':
    for series_cnt, series_name in enumerate(series_names):
        Print.colored(series_name, "yellow")
        found = False
        for subfolder in subfolders:
            path1 = Path.combine(from_folder, subfolder, series_name)
            path2 = Path.combine(to_folder, subfolder, series_name)
            if Dir.exist(path1) or File.exist(path1):
                found = True
                break

        if not found:
            Print.colored(f"{series_name} not found", "red")
            continue

        state = State(path1)

        t = MyThread(printer, args=[state], quiet=True, daemon=True)
        t.start(wait_for_keyboard_interrupt=False)

        if File.exist(path1):
            root, file = os.path.split(path1)
            file_move(file, root, path1, path2, state)

            if File.exist(path1):
                Print.rewrite()
                raise FileExistsError(f"File {path1} is not moved")
            else:
                Print.rewrite()
                Print.colored(f"File {path1} moved", "green")
        elif Dir.exist(path1):
            for root, dirs, files in OS.walk(path1):
                for file in files:
                    file_move(file, root, path1, path2, state)

            if Dir.number_of_files(path1):
                Print.rewrite()
                raise FileExistsError(f"{path1} is not empty")
            else:
                Dir.delete(path1)
                Print.rewrite()
                Print.colored(f"Dir {path1} moved and deleted", "green")
        else:
            # this shouldn't happen
            print("we're fucked up")
            print(path1)
        t.raise_exception()
