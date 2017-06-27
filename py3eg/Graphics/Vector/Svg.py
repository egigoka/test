#!/usr/bin/env python3

import Graphics.Png as Png1
from ..Graphics import Png


def load(filename):
    print("svg: load", filename)


def save(filename):
    print(Png.SAMPLE_RATE, Png1.SAMPLE_RATE)
    print("svg: save", filename)


def width():
    print("svg: width")


def height():
    print("svg: height")


def color_at(x, y):
    print("svg: color_at")


def set_color_at(x, y, color):
    print("svg: set_color_at")
