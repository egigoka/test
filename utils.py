#! python3
import os, json


def createdirs(filename):
    dir = os.path.dirname(filename)
    if not os.path.exists(dir):
        os.makedirs(dir)


def createfile(filename):
    dir = os.path.dirname(filename)
    if not os.path.exists(dir):
        os.makedirs(dir)
    if not os.path.exists(filename):
        open(filename, 'a').close()


def savejson(filename, jsonstring):
    settingsJsonTextIO = open(filename, "w")
    json.dump(jsonstring, settingsJsonTextIO)
    settingsJsonTextIO.close()


def loadjson(filename):
    settingsJsonTextIO = open(filename)
    jsonStringInMemory = json.load(settingsJsonTextIO)
    settingsJsonTextIO.close()
    return jsonStringInMemory
