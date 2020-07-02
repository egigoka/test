import sys

count = int(sys.argv[1])
sym = sys.argv[2]

for i in range(count):
    i += 1
    print(sym*i)
