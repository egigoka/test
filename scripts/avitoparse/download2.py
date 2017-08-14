#! python3
# -*- coding: utf-8 -*-

# import pymongo
try:  # https://stackoverflow.com/questions/11709079/parsing-html-using-python
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
# mine commands
import sys
sys.path.append("../..")
sys.path.append("..\..")
sys.path.append(".")
from commands7 import *


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

    number = None
    html = ""
    soup = None
    parsed = {}
    filename = ""
    title = ""
    ads = 0
    status = 204  # No Content

    @classmethod
    def get_url(cls):
        url = "https://www.avito.ru/" + State.region + "?p=" + str(cls.number) + \
              "&s=2&q=" + State.product
        return url

    @classmethod
    def get_status(cls):
        status = 204  # No Content
        if "Чтобы продолжить пользоваться сайтом, пожалуйста, введите символы с картинки" in cls.html:
            status = 429  # Too Many Requests
        elif cls.title == "":
            status = 100  # Continue
        elif cls.parsed == {}:
            status = 102  # Processing
        elif cls.ads != State.usual_number_of_ads:
            status = 206  # Partial Content
        elif cls.ads == State.usual_number_of_ads:
            # if cls.title == "":
            status = 200  # OK

        else:
            raise Exception("not realised")
        return status

    @classmethod
    def load(cls, number):
        cls.number = number
        filename = State.product + '_in_' + State.region + "_" + str(cls.number) + ".html"  # define ouput file name
        output = Path.extend(".", State.subfolder, filename)  # define path to output file
        Wget.download(cls.get_url(), output=output)  # download file
        cls.html = str(File.read(output))
        cls.status = cls.get_status()

    @classmethod
    def preparse(cls):
        cls.soup = BeautifulSoup(cls.html, "html.parser")  # https://stackoverflow.com/questions/11709079/parsing-html-using-python
        cls.title = str(cls.soup.head.title.text)
        cls.status = cls.get_status()

    @classmethod
    def parse(cls, printprettify=False):

        pass
        items = (cls.soup.find_all('div', attrs={'class': ['item', 'item_table']}))
        cls.ads = 0
        for item in items:
            cls.ads += 1
            if printprettify:
                print(item.prettify())
                print()
            cls.parsed[cls.ads] = {}
            try:
                cls.parsed[cls.ads]['mini_photo'] = urlish(item.div.a.img.get('src'))
            except AttributeError as err:
                print(err)
                cls.parsed[cls.ads]['mini_photo'] = None
            try:
                cls.parsed[cls.ads]['name'] = item.div.a.img.get('alt')
            except AttributeError as err:
                print(err)
                cls.parsed[cls.ads]['name'] = None
            try:
                cls.parsed[cls.ads]['url'] = urlish(item.div.a.get('href'))
            except AttributeError as err:
                print(err)
                cls.parsed[cls.ads]['url'] = None
            for price in item.find_all('div', attrs={'class':['about']}):
                price = stripify(price.text)
                if "руб." in price:
                    cls.parsed[cls.ads]['price'] = price
            for dataset in item.find_all('div', attrs={'class':['data']}):
                cnt_p = 0
                for p in dataset.find_all('p'):
                    ptexts = str(p.text).split(" | ")
                    for ptext in ptexts:
                        cnt_p += 1
                        if cnt_p == 1:
                            cls.parsed[cls.ads]["group"] = stripify(ptext)
                        elif (len(ptexts) == 2) and (cnt_p == 2):
                            cls.parsed[cls.ads]["store"] = stripify(ptext)
                        elif (len(ptexts) == 1) and (cnt_p == 2):
                            cls.parsed[cls.ads]["city"] = stripify(ptext)
                        else:
                            # cls.parsed[cls.ads]["store"] = "__--__"
                            cls.parsed[cls.ads]["city"] = stripify(ptext)
            for timeanddate in item.find_all('div', attrs={'class': ['date', 'c-2']}):
                cls.parsed[cls.ads]["time"] = stripify(timeanddate.text)
        cls.status = cls.get_status()


#print(Page.get_url())
#sys.exit()

pages = {}
for cnt in Int.from_to(1,100):
    def main():
        Page.load(cnt)
        Page.preparse()
        # debug_print("Page.title", Page.title)
        cprint("Page.title " + str(Page.title), "grey", "on_white")
        Page.parse()
        cprint("Page.ads " + str(Page.ads), "green", "on_white")
        cprint("Page.get_status() " + str(Page.get_status()), "red", "on_white")
        # cprint(json.dumps(Page.parsed, indent=4, sort_keys=True, ensure_ascii=False), "white", "on_grey")
    while Page.get_status() != 200:
        main()
        if Page.status == 429:
            cprint("Too many requests", "red")
            time.sleep(60)
        elif Page.status == 200:
            pass
        else:
            raise Exception("What status is" + str(Page.get_status()))
# def load_pages(product, region, subfolder=State.subfolder, usual_number_of_ads=State.usual_number_of_ads):

#    pages[cnt] = Page

#    raise Exception("not realised")

# load_pages(product=State.product, region=State.region)
