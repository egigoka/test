from commands import *

# don't read, it's shit

subd = OS.args[1]

ff = Dir.list_of_files(subd)
ll = Str.nl(File.read("archive.ytdlp"))
fff = {}
llf = {}

for f in ff:
    id = Str.substring(f[-19:], "[", "]")
    if id in fff.keys():
        print(f"file with id {id} appeared twice: {f} and {fff[id]}")
        raise KeyError
    fff[id] = f


for l in ll:
    if not l:
        continue
    id = Str.substring(l, "youtube ")
    if id in llf.keys():
        print(f"archive with id {id} appeared twice: {l} and {llf[id]}")
        raise KeyError
    llf[id] = l

cnt = 0
for id1, f in fff.items():
    if id1 not in llf.keys():
        print(f"{cnt} file {id1} {f} is an impostor")
    cnt += 1

cnt = 0
for id2, l in llf.items():
    if id2 not in fff.keys():
        print(f"{cnt} video {id2} not downloaded")
    cnt += 1
