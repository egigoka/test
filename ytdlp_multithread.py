from commands import *

ytdlp_format = "%(upload_date>%Y-%m-%d)s - %(title).197B [%(id)s].%(ext)s"


def regen_cache(channel, cookies_exist, cookies_path, debug):
    Print.colored("Getting links, please, be patient...")
    command = ["python3", "-m", "yt_dlp", "--flat-playlist", "--print", "id", channel]

    if cookies_exist:
        command.insert(3, cookies_path)
        command.insert(3, "--cookies")

    links = Console.get_output(*command, print_std=debug).strip()
    return links


def download(youtube_video_id, cnt, total, directory, ytdlp_format, no_meta, no_subs, cookies_exist, cookies_path, wait, debug):
    yt_id_with_cnt = f"{youtube_video_id} {cnt+1}/{total}"
    print(f"Started downloading {yt_id_with_cnt}")
    b = Bench(f"Downloaded {yt_id_with_cnt}", verbose=True)
    command = ["python3", "-m", "yt_dlp",
               "-f", "bv[ext=mp4] +ba[ext=m4a]/best[ext=mp4]/best",
               "--prefer-ffmpeg",
               "--merge-output-format", "mkv",
               "--newline",  # Output progress bar as new lines
               "-o", directory
               + Path.separator() + "Videos"
               + Path.separator() + ytdlp_format,
               # "--retries", "infinite",
               "--retries", "100000",
               "--fragment-retries", "100000",
               "--file-access-retries", "100000",
               "--extractor-retries", "100000",
               "--limit-rate", "40M",
               "--retry-sleep", "fragment:exp=1:8",
               "--sponsorblock-mark", "default",
               "--download-archive", directory + Path.separator() + "archive.ytdlp",
               f"https://youtube.com/watch?v={youtube_video_id}"]
    if not no_subs:
        subs_args = ["--embed-subs",
                     "--sub-langs", "all",
                     "--ppa", "EmbedSubtitle:-disposition:s:0 0"]
        for arg in reversed(subs_args):
            command.insert(3, arg)
    if not no_meta:
        meta_args = ["--write-info-json",
                     "--write-comments",
                     "--add-metadata",
                     "--parse-metadata", "%(title)s:%(meta_title)s",
                     "--parse-metadata", "%(uploader)s:%(meta_artist)s",
                     "--write-description",
                     "--write-thumbnail",
                     "--embed-thumbnail",
                     "--write-annotations",
                     "--write-playlist-metafiles",
                     "--write-all-thumbnails",
                     "--write-url-link"]

        for arg in reversed(meta_args):
            command.insert(3, arg)
    if cookies_exist:
        command.insert(3, cookies_path)
        command.insert(3, "--cookies")

    if wait:
        command.insert(-1, "--live-from-start")
        command.insert(-1, "--wait-for-video")
        command.insert(-1, "10")

    if debug:
        Print.colored(*command, "green")
    Console.get_output(*command,
                       print_std=debug)

    b.end()


def free_space_watchdog(minimum_space, directory):
    e = None

    free = 0

    while True:
        output = Console.get_output("df", "-k", directory)

        try:
            usage = (Str.nl(output))[1]
        except Exception as e:
            break

        try:
            free = int(Str.get_words(usage)[3]) * KiB
        except Exception as e:
            break

        try:
            if free < minimum_space:
                break
        except Exception as e:
            break

        Print.colored(f"Free space: {free / GiB:.2f}GiB, limit: {minimum_space / GiB:.2f}GiB", "blue")

        Time.sleep(60 * 5)

    if e is not None:
        Print.colroed(f"Exception: {e}", "red")
    try:
        Print.colored(
            f"free space ({free / GiB:.2f}GiB) is lower, that defined ({minimum_space / GiB:.2f}GiB), closing",
            "red")
    except Exception:
        pass

    print("OS exit started")
    OS.exit(1)
    print("OS exit ended")


def progress(directory):
    import subprocess
    subprocess.Popen(["python3", "/home/egigoka/py/test/ytdlp_progress_tracking.py",
                      directory + Path.separator() + "Videos", "whiletrue"])


def running_threads(tt, additional_threads):
    return
    Print.colored("COUNTING THREADS LOL", "black", "on_white")
    Print.colored("COUNTING THREADS LOL", "red", "on_white")
    Print.colored("COUNTING THREADS LOL", "black", "on_white")
    Print.colored("COUNTING THREADS LOL", "red", "on_white")
    Print.colored("COUNTING THREADS LOL", "black", "on_white")
    Print.colored("COUNTING THREADS LOL", "red", "on_white")
    Print.colored("COUNTING THREADS LOL", "black", "on_white")
    Print.colored("COUNTING THREADS LOL", "red", "on_white")
    Print.colored("COUNTING THREADS LOL", "black", "on_white")
    Print.colored("COUNTING THREADS LOL", "red", "on_white")
    Print.colored("COUNTING THREADS LOL", "black", "on_white")
    Print.colored("COUNTING THREADS LOL", "red", "on_white")
    Print.colored("COUNTING THREADS LOL", "black", "on_white")
    Print.colored("COUNTING THREADS LOL", "red", "on_white")
    Print.colored("COUNTING THREADS LOL", "black", "on_white")
    Print.colored("COUNTING THREADS LOL", "red", "on_white")
    Print.colored("COUNTING THREADS LOL", "black", "on_white")
    Print.colored("COUNTING THREADS LOL", "red", "on_white")
    Print.colored("COUNTING THREADS LOL", "black", "on_white")
    Print.colored("COUNTING THREADS LOL", "red", "on_white")
    Print.colored("COUNTING THREADS LOL", "black", "on_white")
    Print.colored("COUNTING THREADS LOL", "red", "on_white")
    Print.colored("COUNTING THREADS LOL", "black", "on_white")

    while True:
        running = 0
        for runner in tt.runner_threads:
            if runner.is_running():
                running += 1
                Print.colored("running", runner.thread.name, "magenta")
        running += len(tt.input_threads)
        for t in tt.input_threads:
            Print.colored("running", t.thread.name, "magenta")
        Print.colored(f"left {running - additional_threads} links to download", "magenta")
        Time.sleep(20)


def parse_arguments(args):
    dl = "dl" in OS.args
    ch = "ch" in OS.args
    chy = "chy" in OS.args
    debug = "debug" in OS.args
    wait = "wait" in OS.args
    no_meta = "no-meta" in OS.args
    no_subs = "no-subs" in OS.args

    count_of_threads = 2

    directory = None
    for arg in OS.args:
        if debug:
            print(f"{arg=} {Dir.exists(arg)=}")
        if Dir.exists(arg):
            directory = arg
        try:
            count_of_threads = int(arg)
        except ValueError:
            pass

    if (not dl and not ch) or directory is None:
        print(f"usage: py {args[0]} [dl] [ch] [chy] [no-meta] [no-subs] "
              f"[debug] [wait]"
              f"[count of threads] dir_with_config_and_files")
        if not dl and not ch:
            print("please, use at least argument 'dl' and/or 'ch'")
        if directory is None:
            print("please, specify working directory")
        OS.exit(1)

    channel_file_path = directory + Path.separator() + "channel_link.txt"

    return dl, ch, chy, debug, wait, no_meta, no_subs, directory, count_of_threads, channel_file_path


if __name__ == "__main__":

    dl, ch, chy, debug, wait, no_meta, no_subs, directory, count_of_threads, channel_file_path = parse_arguments(OS.args)

    if debug:
        print(f"Working dir is {directory}")
        print(f"{channel_file_path=}")

    channel = File.read(channel_file_path).strip()
    cache_file_path = directory + Path.separator() + "channel_videos_cache.txt"
    cookies_path = directory + Path.separator() + "cookies.txt"
    cookies_exist = File.exist(cookies_path)
    if not cookies_exist:
        Print.colored("Cookies file not found, download without them")

    if ch:
        regen = True
        try:
            if File.get_size(cache_file_path):
                if chy:
                    pass
                elif not CLI.get_y_n("Cache file already written. Do you wish to recreate it?"):
                    regen = False
        except OSError:
            pass
        if regen:
            links = regen_cache(channel=channel, cookies_path=cookies_path, debug=debug, cookies_exist=cookies_exist)
            File.wipe(cache_file_path)
            File.write(cache_file_path, links)

    if dl:
        additional_threads = 3
        tt = Threading(verbose=debug, max_threads=count_of_threads - 1 + additional_threads, start_from_first=True)

        tt.add(progress, kwargs=ImDict({"directory": directory}))
        tt.add(free_space_watchdog, kwargs=ImDict({"minimum_space": 20 * GiB,
                                                   "directory": directory}))
        tt.add(running_threads, args=(tt, additional_threads))

        yt_ids = Str.nl(File.read(cache_file_path).strip())

        for cnt, line in enumerate(yt_ids):
            tt.add(download, kwargs=ImDict({"youtube_video_id": line,
                                            "cnt": cnt,
                                            "total": len(yt_ids),
                                            "directory": directory,
                                            "ytdlp_format": ytdlp_format,
                                            "no_meta": no_meta,
                                            "no_subs": no_subs,
                                            "cookies_exist": cookies_exist,
                                            "cookies_path": cookies_path,
                                            "wait": wait,
                                            "debug": debug}))

        tt.start(wait_for_keyboard_interrupt=True)
