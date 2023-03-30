from commands import *

dl = "dl" in OS.args
ch = "ch" in OS.args
debug = "debug" in OS.args

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
    print("usage: py ytdlp_multithread.py [dl] [ch] dir_with_config_and_files")
    if not dl and not ch:
        print("please, use at least argument 'dl' and/or 'ch'")
    if directory is None:
        print("please, specify working directory")
    OS.exit(1)

if debug:
    print(f"Working dir is {directory}")

channel_file_path = directory + Path.separator() + "channel_link.txt"
if debug:
    print(f"{channel_file_path=}")
channel = File.read(channel_file_path).strip()
cache_file_path = directory + Path.separator() + "channel_videos_cache.txt"

def regen_cache():
    Print.colored("Getting links, please, be patient...")
    links = Console.get_output("python3", "-m", "yt_dlp", "--flat-playlist", "--print", "id", channel, print_std=debug).strip()
    File.wipe(cache_file_path)
    File.write(cache_file_path, links)

if ch:
    regen = True
    if File.get_size(cache_file_path):
        if not CLI.get_y_n("Cache file already written. Do you wish to recreate it?"):
            regen = False
    if regen:
        regen_cache()


def download(youtube_video_id, cnt, total):
    yt_id_with_cnt = f"{youtube_video_id} {cnt}/{total}"
    print(f"Started downloading {yt_id_with_cnt}")
    b = Bench(f"Downloaded {yt_id_with_cnt}", verbose=True)
    Console.get_output("python3", "-m", "yt_dlp",
                       "-f", "bv[ext=mp4] +ba[ext=m4a]/best[ext=mp4]/best",
                       "-o", directory + Path.separator() + "%(title)s [%(id)s].%(ext)s",
                       "--retries", "infinite",
                       "--fragment-retries", "infinite",
                       "--file-access-retries", "infinite",
                       "--extractor-retries", "infinite",
                       "--limit-rate", "40M",
                       "--retry-sleep", "exp=1:8",
                       "--write-info-json",
                       "--write-comments",
                       "--write-subs",
                       "--sub-langs", "all",
                       "--live-from-start",
                       "--wait-for-video",
                       # "--download-archive", directory + Path.separator() + "archive.ytdlp",
                       f"https://youtube.com/watch?v={youtube_video_id}", 
                       print_std=debug)
    b.end()

def free_space_watchdog(minimum_space):
    e = None

    free = 0
    
    while True:
        output = Console.get_output("df", "-k", directory)

        try:
            usage = (Str.nl(output))[1]
        except Exception as e:
            break

        try:
            free = int(Str.get_words(usage)[3])*KiB
        except Exception as e:
            break

        try:
            if free < minimum_space:
                break
        except Exception as e:
            break

        Print.colored(f"Free space: {free/GiB:.2f}GiB, limit: {minimum_space/GiB:.2f}GiB", "blue")

        Time.sleep(60*5)

    if e is not None:
        Print.colroed(f"Exception: {e}", "red")
    try:
        Print.colored(f"free space ({free/GiB:.2f}GiB) is lower, that defined ({minimum_space/GiB:.2f}GiB), closing",
                      "red")
    except Exception:
        pass

    print("OS exit started")
    OS.exit(1)
    print("OS exit ended")

def progress():
    import subprocess
    subprocess.Popen(["python3", "/home/egigoka/py/test/ytdlp_progress_tracking.py", ".", "whiletrue"])


if dl:
    tt = Threading(verbose=debug, max_threads=count_of_threads-1+2, start_from_first=True)

    tt.add(progress)
    tt.add(free_space_watchdog, args=(20*GiB,))

    yt_ids = Str.nl(File.read(cache_file_path).strip())

    for cnt, line in enumerate(yt_ids):
        tt.add(download, kwargs=ImDict({"youtube_video_id": line, 
                                        "cnt": cnt,
                                        "total": len(yt_ids)}))
    
    tt.start(wait_for_keyboard_interrupt=True)
