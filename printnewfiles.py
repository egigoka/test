from commands import *
import commands
if Str.get_integers(commands.__version__)[-1] < 474:
    Console.get_output("pip install git+https://github.com/egigoka/commands", print_std=True)

dir = r"C:\Users\mac\uni"

printed_files = []

while True:
    Time.sleep(0.5, quiet_small=True)
    filepaths = []
    for root, dirs, files in OS.walk(dir):
        for file in files:
            filepaths.append(Path.combine(root, file))
    for file in filepaths:
        file_stamp = file+str(File.get_modification_time(file))
        if file_stamp not in printed_files:
            printed_files.append(file_stamp)
            Print.colored(file, "green")
            for cnt, line in enumerate(Str.nl(File.read(file))):
                print(f"[{cnt}]", line)
            Print()
