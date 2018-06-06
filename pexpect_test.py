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
from commands import *

import pexpect.popen_spawn  # http://pexpect.readthedocs.io/en/stable/overview.html#pexpect-on-windows
import 

def testttt_(command):



    pingg = pexpect.popen_spawn.PopenSpawn(command)
    #dirify(pingg)
    print(pingg.read())
    print(pingg.expect(pexpect.EOF, timeout=None))
    print(pingg.read())  # output nothing, expect read all



testttt_("ping fuck")
testttt_("ping 8.8.8.8 -n 10")
