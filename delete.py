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
from commands8 import *
import inspect

Print.debug("os.path.dirname(os.path.realpath(__file__))",os.path.dirname(os.path.realpath(__file__)),
            "os.getcwd()", os.getcwd(),
            "os.path.abspath(inspect.getsourcefile(lambda:0))", os.path.abspath(inspect.getsourcefile(lambda:0)))
Print.debug('os.chdir("..")')
os.chdir("..")
Print.debug("os.path.dirname(os.path.realpath(__file__))",os.path.dirname(os.path.realpath(__file__)),
            "os.getcwd()", os.getcwd(),
            "os.path.abspath(inspect.getsourcefile(lambda:0))", os.path.abspath(inspect.getsourcefile(lambda:0)))
