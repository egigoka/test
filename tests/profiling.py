#! python3
# -*- coding: utf-8 -*-
# http://python.su/forum/topic/15531/?page=1#post-93316
import sys
sys.path.append("../..")
sys.path.append("..\..")
sys.path.append(".")
sys.path.append("..")
sys.path.append("./term")
sys.path.append(r".\term")


from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput


with PyCallGraph(output=GraphvizOutput()):  # "dot" must be in PATH https://github.com/gak/pycallgraph/issues/177
    from commands8 import *
