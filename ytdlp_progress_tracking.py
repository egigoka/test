from commands import *

directory = None

for arg in OS.args:
    if Dir.exist(arg):
        directory = arg

if directory is None:
    print("no directory specified")
    OS.exit(1)

previous_total_mib = None

previous_speeds = []

update_every = 30

runs_per_5_minutes = 10 * 60 / update_every


previous_mibs_per_file = {}


def main():

    b = Bench(verbose=True)
    global previous_total_mib
    global previous_mibs_per_file

    mibs_per_file = {}
    
    dt = Time.datetime()

    files = []

    for root, dirs, files_ in OS.walk(directory):
        for file in files_:
            files.append(Path.combine(root, file))    

    files.sort()

    mp4 = ""
    mp4temp = ""
    m4a = ""

    total_percent = 0
    file_bundle_count = 0
    total_mib = 0
    
    for file in files:
        if (file.find(".f") != -1 \
                or file.find(".temp") != -1
                or file.find(".live_chat.json.part") != -1 \
                or file.find(".part-Frag") != -1 \
            ):
            try:
                size_mib = int(File.get_size(file)/1024/1024)
            except FileNotFoundError:
                size_mib = 0
            if "logall" in OS.args:
                print(str(size_mib) + "MiB", file)
            total_mib += size_mib

            mibs_per_file[file] = size_mib

            if file.find(".m4a") != -1:
                m4a = file
            elif file.find(".temp.mp4") != -1:
                mp4temp = file
            elif file.find(".f") != -1 and file.find(".mp4") != -1: 
                mp4 = file

            if m4a != "" and mp4 != "" and mp4temp != "":
                try:
                    audioKiB = int(File.get_size(m4a)/1024)
                except FileNotFoundError:
                    audioKiB = 0
                try:
                    videoKiB = int(File.get_size(mp4)/1024)
                except FileNotFoundError:
                    videoKiB = 0
                try:
                    outputKiB = int(File.get_size(mp4temp)/1024)
                except FileNotFoundError:
                    outputKiB = 0
                
                sumKiB = audioKiB + videoKiB
                leftKiB = sumKiB - outputKiB
                percent = int(outputKiB/sumKiB * 10000) / 100
                total_percent += percent
                file_bundle_count += 1

                Print.colored(*Console.fit(f"{percent}%", f"{mp4temp[:-9]} audio {audioKiB} + video {videoKiB} = output {outputKiB} of {sumKiB} ({leftKiB} left)"), "green")

                mp4 = ""
                mp4temp = ""
                m4a = ""

    freespace = Str.nl(Console.get_output("df", "-kh", directory))[1]

    first_run = False
    if previous_total_mib == None:
        previous_total_mib = total_mib
        previous_mibs_per_file = mibs_per_file
        first_run = True

    is_bigger = total_mib > previous_total_mib
    change = total_mib - previous_total_mib

    total_mib_per_new_files = 0
    total_mib_per_old_files = 0
    for file, size_mib in mibs_per_file.items():
        if file in previous_mibs_per_file.keys():
            total_mib_per_old_files += previous_mibs_per_file[file]
        total_mib_per_new_files += size_mib

    total_mib = total_mib_per_new_files
    is_bigger = total_mib_per_new_files > total_mib_per_old_files
 
    plus = "+" if is_bigger else ""
    change = total_mib_per_new_files - total_mib_per_old_files
    speed = change / update_every

    if speed < 0:
        speed = 0

    if not first_run:
        previous_speeds.append(speed)
    
    if len(previous_speeds) > runs_per_5_minutes:
        previous_speeds.pop(0)

    try:
        medium_speed = sum(previous_speeds) / len(previous_speeds)
    except ZeroDivisionError:
        medium_speed = 0

    previous_total_mib = total_mib
    previous_mibs_per_file = mibs_per_file
    
    if file_bundle_count > 1:
        Print.colored(f"{total_percent:.2f}% total of {file_bundle_count * 100}%", "magenta")

    print(f"{str(dt.hour).zfill(2)}:{str(dt.minute).zfill(2)}:{str(dt.second).zfill(2)}", end = " | ")
    
    Print.colored(
        Str.rightpad(f"{Str.leftpad(total_mib, 5, ' ')}MiB total, {plus}{change}MiB, {speed:.2f}MiB/s, {medium_speed:.2f}MiB/s", 
                     50,
                     " "),
        "green" if is_bigger else "", 
        end="\t| ")
    
    print(Str.get_words(freespace)[3] + "B free", end=" | ")
    
    b.end()
    
    
if __name__ == "__main__":

    if "whiletrue" in OS.args:
        while True:
            main()
            Time.sleep(update_every - 2, verbose=True)
            
    else:
        main()

