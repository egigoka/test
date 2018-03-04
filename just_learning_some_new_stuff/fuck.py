#! python3
__version__ = "1.0.0"
import sys
try:
    if sys.argv[1] == "you":
        print("Fuck you too")
    else:
        print("Fucking shit!")
except:
    print("Fuck!"*3)