import sys
sys.path.insert(0, "..")
sys.path.insert(0, "../..")
sys.path.insert(0, "..\..")
from commands7 import *  # mine commands

Process.start('py', Path.extend("T:", "scripts", "solvounload", "solvounload.bat.gui.codegen.py"), new_window=True)
