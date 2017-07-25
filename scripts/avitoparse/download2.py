#! python3
# -*- coding: utf-8 -*-

# import pymongo
try:  # https://stackoverflow.com/questions/11709079/parsing-html-using-python
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
from commands7 import *

if get_os() == "macos":
    File.copy(Path.extend("..", "..", "commands7.py"), "commands7.py")  # update c7


def urlish(string):
    # приведение имени в строку, поддерживаемую в url
    string = string.lower()
    string = string.replace(' ', '+')
    # восстановление полной ссылки из обрезка в html
    if string[:2] == "//":
        string = "https:" + string
    elif string[:1] == "/":
        string = "https://avito.ru" + string
    return string


def avitish(string):
    string = urlish(string)
    if string == "russia":
        return "rossiya"
    elif string == "kurgan+obl":
        return "kurganskaya_oblast"
    else:
        raise IndexError("this script doesn't know how avito calls " + string)


def stripify(obj):
    output = str(obj)
    # if "|" in output:
    #     output = output[:output.find("|")]
    output = output.strip(newline)
    output = output.strip(" ")
    return output


def dirify(object_):
    print("-"*Console.width())
    print(object_.__class__.__name__)
    print("-"*Console.width())
    for subobject in dir(object_):
        if subobject[:1] != "_":
            print("==>  " + subobject)


class State:
    # product = urlish("iPhone SE")
    product = urlish("сим")
    # region = avitish("Russia")
    region = avitish("Kurgan obl")
    subfolder = "test"
    usual_number_of_ads = 50


class Page:

    html = ""
    parsed = {}
    filename = ""
    title = ""
    ads = 0
    status = 204  # No Content

    @classmethod
    def get_status(cls):
        status = 204  # No Content
        if "Чтобы продолжить пользоваться сайтом, пожалуйста, введите символы с картинки" in cls.html:
            status = 429  # Too Many Requests
        elif cls.ads != State.usual_number_of_ads:
            status = 206  # Partial Content
        elif cls.ads == State.usual_number_of_ads:
            staus = 200  # OK
        else:
            raise Exception("not realised")
        return status

    @classmethod
    def load(cls, nubmer):
        
        raise Exception("not realised")
        cls.status = cls.get_status()

pages = {}
def load_pages(product, region, subfolder=State.subfolder, usual_number_of_ads=State.usual_number_of_ads):

    pages[cnt] = Page

    raise Exception("not realised")

load_pages(product=State.product, region=State.region)
