import sys
import os

if len(sys.argv) != 2:  # first arg is filename
    raise ValueError("There must be ")

os.system("help "+sys.argv[1])
