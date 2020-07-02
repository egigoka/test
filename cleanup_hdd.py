from commands import *
import os


def file_move(file, root, path1, path2, State):
    filepath = Path.combine(root, file)
    filepath2 = filepath.replace(path1, path2, 1)

    State.last_file = filepath
    State.last_file2 = filepath2

    try:
        Dir.create(Path.get_parent(filepath2))
    except PermissionError as e:
        Print.colored(f"Dir '{Path.get_parent(filepath2)}' cannot be created: {e}", "red")
    File.move(filepath, filepath2)

    State.count_of_scanned_files += 1
    State.previous_size = 0


series_names = """Tekst.WEB-DL.1080p.HD.m4v
Orphan Black (Season 05) BaibaKo
Gisaengchung (Parasite).2019.720p.mkv
Ford_V_Ferrari.2019.Scr.1080p.mkv
Hellboy (2019).720p.mkv
Sobache.serdce.1988.х264.BDRip.720р.HDClub.mkv
Evangelion 2.22 You Can (Not) Advance (720p)"""
series_names = Str.nl(series_names)

for series_cnt, series_name in enumerate(series_names):
    path1 = Path.combine("Volumes", "HDD 2", "Series", series_name)
    path2 = Path.combine("Volumes", "HDD3", "Series", series_name)

    if not Dir.exist(path1) and not File.exist(path1):
        path1 = Path.combine("Volumes", "HDD 2", "Films", series_name)
        path2 = Path.combine("Volumes", "HDD3", "Films", series_name)
        if not Dir.exist(path1) and not File.exist(path1):
            continue

    class State:
        last_file = None
        last_file2 = None
        try:
            count_of_all_files = Dir.number_of_files(path1)
        except FileNotFoundError:
            count_of_all_files = 1
        count_of_scanned_files = 0

        previous_size = 0
        speed_bench = Bench()


    def printer():
        while True:
            try:
                current_size = File.get_size(State.last_file2)
            except (TypeError, FileNotFoundError):
                current_size = 0
            try:
                percent_file = round((current_size/File.get_size(State.last_file))*100, 2)
            except (TypeError, FileNotFoundError):
                percent_file = 0.0
            percent_all = round(((State.count_of_scanned_files/State.count_of_all_files)*100) + percent_file/State.count_of_all_files, 2)
            # "%.2f" % 1.1 == 1.10

            time_delta = State.speed_bench.end()
            size_diff = 0
            if current_size > State.previous_size:
                size_diff = round((current_size - State.previous_size), 4)
            if float(size_diff) < 0.0001:
                size_diff = 0
            speed = round(size_diff / time_delta, 2)

            # # debug
            # if float(speed/MiB) > 100:
            #     Print.rewrite()
            #     Print.colored("time_delta", time_delta,
            #                   "current_size", current_size/MiB,
            #                   "State.previous_size", State.previous_size/MiB,
            #                   "current_size > State.previous.size", current_size > State.previous_size,
            #                   "size_diff", size_diff,
            #                   "speed", speed/MiB,
            #                   "current_size - State.previous_size", (current_size - State.previous_size)/MiB,
            #                   "red")

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

            Print.rewrite(f"{CLI.wait_update(quiet=True)} [{series_cnt}/{len(series_names)}] {percent_all}% ({State.count_of_scanned_files}/"
                          f"{State.count_of_all_files}). Speed: {round(speed/MiB, 2)}MB/s. Remaining: {remaining_time_str}", State.last_file)

            State.previous_size = current_size
            import time
            time.sleep(1)


    t = MyThread(printer, quiet=True, daemon=True)
    t.start()

    if File.exist(path1):
        root, file = os.path.split(path1)
        file_move(file, root, path1, path2, State)

        if File.exist(path1):
            Print.rewrite()
            raise FileExistsError(f"File {path1} is not moved")
        else:
            Print.rewrite()
            Print.colored(f"File {path1} moved", "green")

    if Dir.exist(path1):
        for root, dirs, files in OS.walk(path1):
            for file in files:
                file_move(file, root, path1, path2, State)

        if Dir.number_of_files(path1):
            Print.rewrite()
            raise FileExistsError(f"{path1} is not empty")
        else:
            Dir.delete(path1)
            Print.rewrite()
            Print.colored(f"Dir {path1} moved and deleted", "green")
