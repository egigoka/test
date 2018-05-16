#! python3
# -*- coding: utf-8 -*-
# http://python.su/forum/topic/15531/?page=1#post-93316
__version__ = "2.0.0"
#some shitty functions that i wrote million time in other shitty scripts

def dirify(object, quiet=False):
    output = []
    for subobj in dir(object):
        if "__" not in subobj:
            if not quiet: print(subobj)
            output.append(subobj)
    return output
