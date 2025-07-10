from commands import *
import os

folder = OS.args[1]

bad_exts = [
    ".Heart", ". All", ". grow", ". Dr", ".0", ".3", ".M", ".I", ".", ". djkaktus", 
    ".11 Update", ".720"
]

def main():
    print()
    exts = {}

    for file in Dir.list_of_files(folder):
        file = Path.combine(folder, file)
        file_1, ext = os.path.splitext(file)
        if ext in [".py", ".txt", ".sh"]:
            continue
        file_2, second_ext = os.path.splitext(file_1)
        file_3, third_ext = os.path.splitext(file_2)
        try:
            size = File.get_size(file)
        except FileNotFoundError:
            size = 0
        if second_ext != "" and len(second_ext) < 16 and "[" not in second_ext \
                and second_ext not in bad_exts:
            ext = second_ext + ext
        if third_ext != "" and third_ext != "." and len(third_ext) < 16 \
                and "[" not in third_ext and third_ext not in bad_exts:
            ext = third_ext + ext
        try:
            exts[ext][0] += 1
            exts[ext][1] += size
        except KeyError:
            exts[ext] = []
            exts[ext].append(1)
            exts[ext].append(size)

    exts = Dict.sorted_by_key(exts)

    total = {"files": 0,
             "size": 0}

    print(Time.dotted())

    for ext, cnt in exts.items():
        if len(ext) <= 8:
            ext += "\t\t"
        elif len(ext) <= 16:
            ext += "\t"
        
        total['files'] += cnt[0]
        total['size'] += cnt[1]
        size = f"{cnt[1]/GiB:.2f}GiB"
        if len(size) < 8:
            size += "\t"

        color = "green" if ext == ".mp4\t\t" else ""

        vids = 519
        add = f"{(cnt[1]/cnt[0]/GiB)*vids:.2f}GiB" if ext ==".mkv\t\t" else ''
        
        Print.colored(ext, cnt[0], size, f"{(cnt[1]/cnt[0])/GiB:.2f}GiB", add, color, sep="\t")

    print(f"\t\t\t{total['files']}\t{total['size']/GiB:.2f}GiB")

if __name__ == "__main__":
    main()
    if "whiletrue" in OS.args:
        while True:
            Time.sleep(60, verbose=True)
            main()
