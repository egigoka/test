from commands import *
import ytdlp_multithread

(dl, ch, debug, wait, no_meta, no_subs, directory,
 count_of_threads, channel_file_path) = ytdlp_multithread.parse_arguments(OS.args)

if debug:
    print(f"{channel_file_path=}")
channel = File.read(channel_file_path).strip()
cache_file_path = directory + Path.separator() + "channel_videos_cache.txt"
cookies_path = directory + Path.separator() + "cookies.txt"
cookies_exist = File.exist(cookies_path)

if (not dl and not ch) or directory is None:
    print("usage: py ytdlp_multithread.py [dl] [ch] dir_with_config_and_files")
    if not dl and not ch:
        print("please, use at least argument 'dl' and/or 'ch'")
    if directory is None:
        print("please, specify working directory")
    OS.exit(1)

if debug:
    print(f"Working dir is {directory}")

regen = True
try:
    if File.get_size(cache_file_path):
        if not CLI.get_y_n("Cache file already written. Do you wish to recreate it?"):
            regen = False
except OSError:
    pass
if regen:
    links = ytdlp_multithread.regen_cache(channel=channel,
                                          cookies_path=cookies_path,
                                          debug=debug,
                                          cookies_exist=cookies_exist)
    File.wipe(cache_file_path)
    File.write(cache_file_path, links)

yt_ids = Str.nl(File.read(cache_file_path).strip())
total = len(yt_ids)
for cnt, line in enumerate(yt_ids):
    ytdlp_multithread.download(youtube_video_id=line,
                               cnt=cnt,
                               total=total,
                               cookies_exist=cookies_exist,
                               cookies_path=cookies_path,
                               no_meta=no_meta,
                               debug=debug,
                               directory=directory,
                               wait=False,
                               ytdlp_format=ytdlp_multithread.ytdlp_format)
