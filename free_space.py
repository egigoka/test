from commands import *

def human_readable(bytes):
    gib = int(bytes / GiB)
    bytes -= gib * GiB
    mib = int(bytes / MiB)
    bytes -= mib * MiB
    kib = int(bytes / KiB)
    byt = ""  # f" {bytes - kib * KiB:03}"
    return f"{gib}G {mib:03}M {kib:03}K{byt}"

previous = None
diff_string = ""
while True:
    free = Dir.get_free_space("/")
    space_string = human_readable(free)

    time_string = str(Time.datetime())

    if previous is not None:
        diff = free - previous
        diff_string = "" if diff >= 0 else "-"
        diff_string += human_readable(abs(diff))

    print(f"{time_string}\t{space_string}\t{diff_string}")

    previous = free
    
    Time.sleep(60, verbose=True)
    Print.rewrite()
