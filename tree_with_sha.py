from commands import *

path = OS.args[1]

for root, dirs, files in OS.walk(path):
    for file in files:
        filepath = Path.combine(root, file)
        sha = File.sha256_checksum(filepath)
        print(filepath, sha)
