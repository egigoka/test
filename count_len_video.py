from commands import *

dir = OS.args[1]

files = Dir.list_of_files(dir)
secs = 0


def l(filename):
    command = [
        'ffprobe', 
        '-v', 
        'error', 
        '-show_entries', 
        'format=duration', 
        '-of', 
        'default=noprint_wrappers=1:nokey=1', 
        filename
      ]
    dur = Console.get_output(command)
    try:
        out = Str.get_integers(dur, float_support=True)[0]
    except IndexError:
        out = 0
    return out

for cnt, file in enumerate(files):
    Print.rewrite(f"{cnt+1} / {len(files)}", file)
    secs += l(Path.combine(dir, file))

mins = secs / 60
mins_left = mins % 60
hours = mins // 60

Print.rewrite()
print(f"{int(hours)}h {int(mins_left)}m")
