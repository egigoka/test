from commands import *

dir = '/Users/mac/Desktop/1C Junior Developer Training course'
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
    out = Str.get_integers(dur, float_support=True)[0]
    return out


for file in files:
    num = Str.get_integers(file)[0]
    if num >= 30:
        if num <= 38:
            secs += l(Path.combine(dir, file))
            # print(secs, file)

mins = secs / 60
mins_left = mins % 60
hours = mins // 60

print(f"{int(hours)}:{int(mins_left)}")
