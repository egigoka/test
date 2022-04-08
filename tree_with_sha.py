from commands import *

path = OS.args[1]

try:
    output = OS.args[2]
    File.wipe(output)
except:
    output = None

for root, dirs, files in OS.walk(path):
    for file in files:
        filepath = Path.combine(root, file)
        sha = File.sha256_checksum(filepath)
        filepath = filepath.replace(path, "", 1)
        print(filepath, sha)
        if output is not None:
            File.write(output, f"{filepath} {sha}{newline}", mode="a")

if output is not None:
    content = File.read(output, auto_detect_encoding=False)
    lines = Str.nl(content)
    lines.sort()
    File.write(output, newline.join(lines), mode = "w")
