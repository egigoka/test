import os

file_path = "environ.txt"

what_to_write = ""

for name, value in os.environ.items():
    what_to_write += name + ":" + value + "\n"

for name, value in os.environ.items():
    with open(file_path, mode="w") as file:
        file.write(what_to_write)
