#! python3
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "..")
sys.path.insert(0, "../..")
sys.path.insert(0, "..\..")
from commands8 import *  # mine commands



#cmnd1 = """osascript -e 'tell app "Terminal"
#    do script "echo hello; sleep 10; osascript -e 'quit'"
#    end tell'"""

#debug_print(cmnd1, raw=True)
#os.system(cmnd1)

def applescript_quotize(input_script):
    for symbol in input_script:
        if symbol in ["'", '"']:
            quote = symbol
            break
    count_of_quotes = 0
    output_text = ""
    for symbol in input_script:
        if symbol == quote:
            count_of_quotes += 1
            if count_of_quotes%2 != 0:  # нечётное число кавычек
                output_text += quote + " & quoted form of (" + quote
            else:  # чётное количество
                output_text += quote + ")"
        else:
            output_text += symbol

    if count_of_quotes%2 != 0:
        raise ValueError("Unexpected ")

    return output_text

print(Random.integer(1,100000))

scrpt1 = r"""echo -n -e \"\033]0;My Window Name\007\"; echo hello; sleep 10; osascript -e 'tell application "Terminal" to close (every window whose name contains "My Window Name")' & exit'"""

scrpt1 = applescript_quotize(scrpt1)
debug_print("applescript_quotize(scrpt1)", scrpt1)

cmnd2 = """osascript -e 'tell app "Terminal" """[:-1] + newline
cmnd2 += """    do script " """[:-1]
#cmnd2 += r"""echo -n -e " & quoted form of ("fuck")"""
#cmnd2 += r"""echo -n -e quoted form of (\033]0;My Window Name\007)"""
#cmnd2 += r"""echo -n -e \"\033]0;My Window Name\007\"; """  # как тут экранировать двойные кавычки для эплскрипта?!
#cmnd2 += """echo hello; """
#cmnd2 += """sleep 10; """
#cmnd2 += """osascript -e 'quit'"""
cmnd2 += scrpt1
cmnd2 += '"'
cmnd2 += newline
cmnd2 += """    end tell'"""





#debug_print(cmnd2, raw=True)
debug_print("full command", cmnd2)
#Str.diff_simple(cmnd1, cmnd2)
os.system(cmnd2)