#! python3
# -*- coding: utf-8 -*-
from commands7 import *

###### ЧТО ЗА NONE ПОСТОЯННЫЕ?!

def check(string, beginstr):
    if string[:len(beginstr)] == beginstr:
        args = Str.substring(string, beginstr)
        if len(beginstr) == 1:
            return string
        return beginstr.upper() + " with args " + args
    else:
        #debug_print(string, beginstr)
        #input()
        return None

def s_print(string):
    #input()
    #print(string)
    for sym in ['A', '❄', '●', 'A', '2', '«', "1", "О", "Р", "8", "В",  "4",  "Т",  "|",
                "i",  "К",  "C",  "Б",  "В",  "Г",  "Д",  "Е",  "Ё",  "Ж",  "З",  "И",  "Й",
                "Ш",  "Х",  "Ф",  "У",  "Т",  "С",  "Р",  "П",  "О",  "Н",  "М",  "Л",  "К",
                "Щ",  "Ъ",  "Ы",  "Ь",  "Э",  "Ю",  "Я",  "3",  "5",  "6",  "7",  "9",  " ",
                "L",  "0",  "А",  "N",  "н",  "a",  " ",  " ",  " ",  " ",  " ",  " ",  " ",
                ]:
        if check(string, sym):
            print(newline*5 + "PURE INFO" + check(string, sym))
            if ("р" in string) or ("Р" in string):
                print(newline*5 + "ЦЕНА??!!")
                input("if1")
            return


    if ("р" in string) or ("Р" in string):
        print(newline*5 + "PURE INFO" + check(string, ""))
        print(newline*5 + "ЦЕНА??!!")
        input("if2")

    if check(string, "<div "):
        if check(string, '<div class="about">'):
            print("ЦЕНА!!! " + check(string, '<div class="about">'))
        print(check(string, "<div "))


    elif check(string, "<span "):
        print(check(string, "<span "))

    elif check(string, "<a "):
        print(check(string, "<a "))
    elif check(string, "<p"):
        print(check(string, "<p"))
    elif check(string, "<i"):
        print(check(string, "<i"))
    elif check(string, "<ul"):
        print(check(string, "<ul"))

    elif check(string, "<img "):
        print("IMAGE " + check(string, "<img "))

    elif check(string, "</"):
        pass
        #print("END OF " + check(string, "</"))

    elif check(string, "<!--"):
        print(check("COMMENT??? " + string, "<!--"))

    elif check(string, "<noscript"):
        print(check("COMMENT??? " + string, "<noscript"))

    elif check(string, "<noindex"):
        print(check("SEARCHENGINEFIX " + string, "<noindex"))


    elif check(string, " "):
        print("PURE INFO" + check(string, " "))



    elif check(string, "<h3 "):
        print("!!!NAME???" + check(string, "<h3 "))



    elif len(string) == 0:
        print("just empty line")
    else:
        raise IndexError(string + "isn't recognised")
