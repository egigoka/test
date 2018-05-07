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


import pip
from subprocess import call

packages = [dist.project_name for dist in pip.get_installed_distributions()]
for package in packages:
    Process.start("pip", "install", "--upgrade", package)
