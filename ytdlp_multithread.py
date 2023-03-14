from commands import *

dl = "dl" in OS.args
ch = "ch" in OS.args
debug = "debug" in OS.args

directory = None
for arg in OS.args:
    if debug:
        print(f"{arg=} {Dir.exists(arg)=}")
    if Dir.exists(arg):
        directory = arg

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

if ch:
    File.wipe(cache_file_path)
    Print.colored("Getting links, please, be patient...")
    links = Console.get_output("python3", "-m", "yt_dlp", "--flat-playlist", "--print", "id", channel, print_std=debug).strip()
    File.write(cache_file_path, links)


def download(youtube_video_id):
    print(f"Started downloading {youtube_video_id}")
    Console.get_output("python3", "-m", "yt_dlp",
                       "-f", "bv[ext=mp4] +ba[ext=m4a]/best[ext=mp4]/best",
                       "-o", directory + Path.separator() + "%(title)s [%(id)s].%(ext)s",
                       "--retries", "1000",
                       "--fragment-retries", "1000",
                       "--file-access-retries", "1000",
                       "--extractor-retries", "1000",
                       "--download-archive", directory + Path.separator() + "archive.ytdlp",
                       f"https://youtube.com/watch?v={youtube_video_id}")
    print(f"Ended downloading {youtube_video_id}")


if dl:
    tt = Threading(verbose=True, max_threads=10, start_from_first=True)

    for line in Str.nl(File.read(cache_file_path).strip()):
        tt.add(download, kwargs=ImDict({"youtube_video_id": line}))

    tt.start(wait_for_keyboard_interrupt=True)
