import os
import sys

path = sys.argv[1]

if os.path.isdir(path):
    print(", ".join([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]))
elif os.path.isfile(path):
    with open(path, "r") as file:
        print(file.read())
