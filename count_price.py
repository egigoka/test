from commands import *

prices = JsonList("prices.json")
prices.load()

while True:
    inp = input("input price, 'exit' or 'clear' ")
    try:
        prices.append(int(inp))
    except ValueError:
        if inp == "exit":
            break
        elif inp == "clear":
            prices.clear()
        else:
            pass
    prices.save()

freq = {}

for p in prices:
    try:
        freq[p] += 1
    except KeyError:
        freq[p] = 1

freq = Dict.sorted_by_key(freq)

for k, v in freq.items():
    print(k, "*"*v)
