#! python3
import random
x = ["X", "Ks", "S", "К", "Sh", "Ss",
     "К", "Кс", "С", "Х", "Ш", "Сс", "Х"]
i = ["i", "y", "e", "u", "m", "э",
     "ю", "и", "е", "м", "о", "а"]
a = ["a", "o", "y", "m", "", "a",
     "a", "o", "у", "м", "", "а"]
o = ["o", "u", "y", "o", "u", "y",
     "о", "у", "ю", "у", "", "", ]
m = ["m", "m", "m", "", "", "",
     "", "", "", "м", "м", "м"]
i_ = ["i", "y", "e", "u", "m", "ъ",
     "ы", "э", "ю", "и", "е", "м"]

x = [
     "К", "Кс", "С", "Х", "Ш", "Сс", "Х"]
i = [ "э",
     "ю", "и", "е", "м", "о", "а"]
a = [
     "a", "o", "у", "м", "", "а"]
o = [
     "о", "у", "ю", "у", "", "", ]
m = [
     "", "", "", "м", "м", "м"]
i_ = [ "ъ",
     "ы", "э", "ю", "и", "е", "м"]

xiaomi = ""
xiaomiall = ""

def main():
    xiaomi = random.choice(x) + random.choice(i) + random.choice(a) + random.choice(o) + random.choice(m) + random.choice(i_)
    good = input(xiaomi)
    if good == "":
        global xiaomiall
        xiaomiall = xiaomiall + xiaomi + ", "
    elif good == "print":
        print(xiaomiall)
        xiaomiall = ""

while True:
    main()


for q in x:
    for w in i:
        for e in a:
            for r in o:
                for t in m:
                    for y in i_:
                        xiaomi = q+w+e+r+t+y
                        print(xiaomi)