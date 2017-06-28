# -*- coding: utf-8 -*-
from commands7 import *
import PIL


class State:
    json_file = "pngwork.json"


class JsonLocal:
    string = None
    json_file = State.json_file

    @classmethod
    def load(cls, filename=json_file):
        cls.string = Json.load(filename)

    @classmethod
    def save(cls, filename=json_file):
        Json.save(filename, cls.string)


JsonLocal.load()
JsonLocal.string = {}
JsonLocal.save()


class ImageCurrent:
    pass


image = PIL.Image.open("test2x2.png")
image_out = PIL.Image.new(image.mode,image.size)

pixels = list(image.getdata())
debug_print("pixels", pixels)
pixels.pop()
debug_print("pixels", pixels)
# cnt = 0
# for pixel in pixels:
#     cnt += 1
#     pixels_2
# pixels = []
print(type([]))
print(type(()))
cnt =0
# while cnt<255:
#     cnt += 1
#     pixels.append([(100,cnt,100,255)])
image_out.putdata(pixels)
image_out.save('test2x2_out.png')
