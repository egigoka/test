#! python3
# -*- coding: utf-8 -*-
# mine commands
import sys
sys.path.append("../..")
sys.path.append("..\..")
sys.path.append(".")
sys.path.append("..")
sys.path.append("./term")
sys.path.append(r".\term")
from commands8 import *


def get_percentage():
    percent = Console.get_output('pmset -g batt')
    percent = Str.get_integers(percent)[2]
    return percent


Process.start('say', get_percentage(), 'percents')

