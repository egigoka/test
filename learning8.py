#! python3
# -*- coding: utf-8 -*-
from commands7 import *
def bubblesort(list, quiet=True):
    list = copy.deepcopy(list)
    is_sorted = False
    if not quiet:
        maxcnt = 0
        lenlist = len(list)
    while not is_sorted:
        cnt = 0
        while True:
            try:
                if list[cnt] > list[cnt+1]:
                    temp_var = list[cnt]
                    list[cnt] = list[cnt+1]
                    list[cnt+1] = temp_var
                    if not quiet:
                        if cnt > maxcnt:
                            maxcnt = cnt
                            output_string = Str.leftpad(str(maxcnt), len(str(lenlist)))+"/"+str(lenlist)
                            if OS.name == "macos":
                                output_string = " " + output_string
                            Print.rewrite(output_string)
                    break
                cnt += 1
            except IndexError:  # значит, прошлись по всему списку и всё ок
                is_sorted = True
                break
    return list

def bigdigits(digits):
    def digits_init(height = False):
        Zero = ["   ###   ",
                "  #   #  ",
                " #     # ",
                "#       #",
                " #     # ",
                "  #   #  ",
                "   ###   ", ]
        One = ["    #    ",
               "   ##    ",
               "  # #    ",
               "    #    ",
               "    #    ",
               "    #    ",
               " ####### ", ]
        Two = [" ####### ",
               "#       #",
               "        #",
               " ####### ",
               "#        ",
               "#        ",
               "#########", ]
        Three = [" ####### ",
                 "#       #",
                 "        #",
                 "     ### ",
                 "        #",
                 "#       #",
                 " ####### ", ]
        Four = ["#       #",
                "#       #",
                "#       #",
                "#########",
                "        #",
                "        #",
                "        #", ]
        Five = ["#########",
                "#        ",
                "#        ",
                "######## ",
                "        #",
                "#       #",
                " ####### ", ]
        Six = [" ####### ",
               "#       #",
               "#        ",
               "######## ",
               "#       #",
               "#       #",
               " ####### ", ]
        Seven = ["#########",
                 "#       #",
                 "      ## ",
                 "    ##   ",
                 "  ##     ",
                 " #       ",
                 "#        ", ]
        Eight = [" ####### ",
                 "#       #",
                 "#       #",
                 " ####### ",
                 "#       #",
                 "#       #",
                 " ####### ", ]
        Nine = [" ####### ",
                "#       #",
                "#       #",
                " ########",
                "        #",
                "#       #",
                " ####### ", ]
        Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]
        height_int = len(Zero)
        if height:
            return height_int
        else:
            return Digits
    Digits = digits_init()
    column = 0
    while column < digits_init(height=True):
        line = ""
        digits = str(digits)
        for digit in digits:
            # try:
            digit = int(digit)
            line = line + Digits[digit][column].replace("#", str(digit)) + " "
        print(line)
        column += 1

def simple_calc_page65():
    list = []
    try:
        while True:
            list.append(Str.input_int(quiet=True))
    except ValueError:
        mean = 0
        for item in list:
            mean += item
        mean /= len(list)
        print("numbers:", list)
        print("count =", len(list), "lowest =", min(list), "highest =", max(list), "mean =", mean)

def simple_calc_advanced_page66():
    list = []
    try:
        while True:
            list.append(Str.input_int(quiet=True))
    except ValueError:
        if len(list) == 0:
            print("no input")
        else:
            mean = 0
            for item in list:
                mean += item
            mean /= len(list)
            if len(list) % 2 == 1:
                median = list[int(0.5+((len(list)-1)/2))]  # средний элемент списка
            else:
                median = (list[int(len(list)/2)]+list[int(len(list)/2)-1])/2  # среднеарифметическое среди двух средних элементов
            print("numbers:", list)
            print("count =", len(list), "lowest =", min(list), "highest =", max(list), "mean =", mean, "median =", median)

def awful_poetry_page65(sentences=5):
    articles = ["a", "the"]
    pronouns = ['my', 'your', 'his', 'her', 'its', 'our', 'your', 'their'] + articles
    pronouns_plural = ['mine', 'yours', 'his', 'hers', 'its', 'ours', 'its', 'ours', 'yours', 'theirs'] + articles
    pronouns = [pronouns, pronouns_plural]
    nouns = ["cat", "women", "men", "dog", "cluster", "Sonic the Hedgehog", "queen", "breast"]
    nouns_multiple = ["cats", "women", "men", "dogs", "clusters", "Sonics the Hedgehogs", "queens", "breasts"]
    nouns = [nouns, nouns_multiple]
    verbs = ["jumped", "fucked", "fucks", "sang", "ran", "clusteryfied", "died"]
    adverbs = ["as fuck", "loudly", "well", "badly", "quetly"]

    for _ in Int.from_to(1,sentences):
        multiple = Random.integer(0,1)
        print(pronouns[multiple][Random.integer(0, len(pronouns[multiple])-1)].capitalize(), end=" ")
        print(nouns[multiple][Random.integer(0, len(nouns[multiple]) - 1)], end=" ")
        print(verbs[Random.integer(0, len(verbs)-1)], end=" ")
        print(adverbs[Random.integer(0, len(adverbs) - 1)], end="")
        print(".", end=" ")
    print()
