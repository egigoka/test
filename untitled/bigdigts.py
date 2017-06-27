#! python3
import sys
from utils import *

Zero = ["   ###   ",
        "  #   #  ",
        " #     # ",
        "#       #",
        " #     # ",
        "  #   #  ",
        "   ###   ",]
One = ["    #    ",
       "   ##    ",
       "  # #    ",
       "    #    ",
       "    #    ",
       "    #    ",
       " ####### ",]
Two = [" ####### ",
       "#       #",
       "        #",
       " ####### ",
       "#        ",
       "#        ",
       "#########",]
Three = [" ####### ",
         "#       #",
         "        #",
         "     ### ",
         "        #",
         "#       #",
         " ####### ",]
Four = ["#       #",
        "#       #",
        "#       #",
        "#########",
        "        #",
        "        #",
        "        #",]
Five = ["#########",
        "#        ",
        "#        ",
        "######## ",
        "        #",
        "#       #",
        " ####### ",]
Six = [" ####### ",
       "#       #",
       "#        ",
       "######## ",
       "#       #",
       "#       #",
       " ####### ",]
Seven = ["#########",
         "#       #",
         "      ## ",
         "    ##   ",
         "  ##     ",
         " #       ",
         "#        ",]
Eight = [" ####### ",
         "#       #",
         "#       #",
         " ####### ",
         "#       #",
         "#       #",
         " ####### ",]
Nine = [" ####### ",
        "#       #",
        "#       #",
        " ########",
        "        #",
        "#       #",
        " ####### ",]
Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

stri = sys.argv[1]

column = 0
while column < len(Zero):
    line = ""
    for digit in stri:
        #try:
            digit = int(digit)
            line = line + Digits[digit][column] + " "
    print(line)
    column += 1


# This is ver 1.0
# Newest versions in utils_dev