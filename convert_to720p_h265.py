from commands import *

TMP_END = ".720.tmp.mp4"
OUT_END = ".720.mp4"
PATH = OS.args[1]
FILES = Dir.list_of_files(PATH)
LENFILES = len(FILES)
REMOVEOLD = "--remove-old" in OS.args



def get_command(input, output, fps):
    command = [
        'ffmpeg', 
        '-i', input, 
        '-c:v', 'libx265', 
        '-preset', 'medium', 
        '-crf', '28', 
        '-vf', f'scale=1280:720,fps={fps}', 
        '-c:a', 'copy', 
        output]
    return command


for cnt, file in enumerate(FILES):
    file = Path.combine(PATH, file)
    print(f"{cnt+1} / {LENFILES} : {file}")
    if file.endswith(TMP_END):
        File.delete(file)
        print ("tmp deleted, skip")
        continue
    if file.endswith(OUT_END) or file.endswith(".py"):
        print("done or py, skip")
        continue

    output = file.replace(File.get_extension(file), "")
    output_temp = output + TMP_END
    output += OUT_END
    

    if File.exist(output):
        if REMOVEOLD:
            File.delete(file)
        print("output exist, skip")
        continue

    lenght = Video.get_length(file)
    width, height = Video.get_resolution(file)
    width_orig = width
    height_orig = height
    fps = Video.get_fps(file)
    fps_orig = fps

    if width <= 1280 and height <= 720 and fps <= 30:
        print(f"already {width_orig}x{height_orig} {fps_orig} fps")
        File.copy(file, output)
        continue

    while fps > 30:
        fps /= 2

    if height > 720:
        height = 720
        width = int(width_orig * height / height_orig / 2)
        width *= 2 # it should be even

    
    print()
    print(f"{cnt+1} / {LENFILES}\t({Time.human_readable(lenght)})")
    print(f"converting from {width_orig}x{height_orig}\t{fps_orig} fps")
    print(f"             to {width}x{height}\t{fps} fps")
    print()

    
    command = get_command(file, output_temp, fps)

    try:
        Console.get_output(command, print_std=True)
    except KeyboardInterrupt:
        print("^C")
        OS.exit(1)

    File.move(output_temp, output)
