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

update_every = 20

runs_per_5_minutes = 5 * 60 / update_every


def main():

    b = Bench(verbose=True)
    global previous_total_mib
    
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
        if (file.find(".f") != -1 or file.find(".temp") != -1):
            if "logall" in OS.args:
                print(str(int(File.get_size(file)/1024/1024)) + "MiB", file)
            total_mib += int(File.get_size(file)/1024/1024)
            if file.find(".m4a") != -1:
                m4a = file
            elif file.find(".temp.mp4") != -1:
                mp4temp = file
            elif file.find(".f") != -1 and file.find(".mp4") != -1: 
                mp4 = file

            if m4a != "" and mp4 != "" and mp4temp != "":
     
                audioKiB = int(File.get_size(m4a)/1024)
                videoKiB = int(File.get_size(mp4)/1024)
                outputKiB = int(File.get_size(mp4temp)/1024)
                sumKiB = audioKiB + videoKiB
                leftKiB = sumKiB - outputKiB
                percent = int(outputKiB/sumKiB * 10000) / 100
                total_percent += percent
                file_bundle_count += 1

                Print.colored(*Console.fit(f"{percent}%", f"{mp4temp[:-9]} audio {audioKiB} + video {videoKiB} = output {outputKiB} of {sumKiB} ({leftKiB} left)"), "green")

                mp4 = ""
                mp4temp = ""
                m4a = ""

    freespace = Str.nl(Console.get_output("df -kh ."))[1]

    first_run = False
    if previous_total_mib == None:
        previous_total_mib = total_mib
        first_run = True

    is_bigger = total_mib > previous_total_mib
 
    plus = "+" if is_bigger else ""
    change = total_mib - previous_total_mib
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
    
    if file_bundle_count > 1:
        Print.colored(f"{total_percent:.2f}% total of {file_bundle_count * 100}%", "magenta")

    print(f"{str(dt.hour).zfill(2)}:{str(dt.minute).zfill(2)}:{str(dt.second).zfill(2)}", end = "\t|\t")
    
    Print.colored(
        f"{Str.leftpad(total_mib, 5, ' ')}MiB total, {plus}{change}MiB, {speed:.2f}MiB/s, {medium_speed:.2f}MiB/s", 
        "green" if is_bigger else "", 
        end="\t|\t")
    
    print(Str.get_words(freespace)[3] + "B free", end="\t|\t")
    
    b.end()
    
    
if __name__ == "__main__":

    if "whiletrue" in OS.args:
        while True:
            main()
            Time.sleep(update_every - 1, verbose=True)
            
    else:
        main()

