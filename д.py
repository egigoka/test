import os

path = r"C:\users\public\d.txt"
path = "test.txt"

if not os.path.isfile(path):
    with open(path, mode="w") as file:
        file.write("0")

with open(path, "r") as file:
    content = file.read()

try:
    count = int(content)
except ValueError:
    with open(path, mode="w") as file:
        file.write("0")
    count = 0

count += 1

with open(path, mode="w") as file:
    file.write(str(count))

print(count)
