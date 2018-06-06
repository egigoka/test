#! python3
# -*- coding: utf-8 -*-

def a():
    print("called a")

def c():
    a()
    from d.b import b
    b()
    print("called c")

c()
