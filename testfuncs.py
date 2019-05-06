#! python3
# -*- coding: utf-8 -*-

def func1(arg1, arg2, arg3="work", arg4="I", arg5="don't", arg6="know"):
    print(arg1, arg2, arg3, arg4, arg5, arg6)

def func2(arg1, arg2, arg3="work", arg4="I", arg5="don't", arg6="know"):
    func1(arg1=arg1, arg2=arg2, arg3=arg3, arg4=arg4, arg5=arg5, arg6=arg6)
    #doing_some_other_stuff()


func2("How", "this")
