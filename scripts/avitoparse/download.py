#! python3
# -*- coding: utf-8 -*-

#import pymongo
try:  # https://stackoverflow.com/questions/11709079/parsing-html-using-python
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
from commands7 import *

if get_os() == "macos":
    File.copy(Path.extend("..","..","commands7.py"), "commands7.py")  # update c7


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
    #if "|" in output:
    #    output = output[:output.find("|")]
    output = output.strip(newline)
    output = output.strip(" ")
    return output


def dirify(object):
    print("-"*Console.width())
    print(object.__class__.__name__)
    print("-"*Console.width())
    for subobject in dir(object):
        if subobject[:1] != "_":
            print("==>  " + subobject)


class State:
    product = urlish("iPhone SE")
    product = urlish("сим")
    region = avitish("Russia")
    region = avitish("Kurgan obl")
    subfolder = "test"
    usual_number_of_ads = 50






class Url:
    page = 1
    page -= 1

    @classmethod
    def get_page(cls):
        return str(cls.page)

    @classmethod
    def get(cls):
        cls.page += 1
        url = "https://www.avito.ru/" + State.region + "?p=" + str(cls.page) + \
        "&s=2&q=" + State.product
        return url


class Page():

    class Last(self):
        html = ""
        parsed = {}
        filename = ""
        title = ""
        ads = 0
        status = 204


    #class Get(self):
    #    print("!!!", self.Last.html, "!!!")
    #    @classmethod
    #    def status(cls):
    #        if cls.Last.title == "Доступ временно заблокирован":
    #            cls.Last.status = 429  # too many requests
    #        elif cls.Last.ads != State.usual_number_of_ads:
    #            cls.Last.status = 206  # partial content


    @classmethod
    def get(cls, debug=False):
        filename = State.product + '_in_' + State.region + str(Url.page+1) + ".html"  # define ouput file name
        output = Path.extend(".", State.subfolder, filename)  # define path to output file
        Wget.download(Url.get(), output=output)  # download file
        #page_info = Str.substring(File.read(output),
        #                          before = '<div class="catalog-list clearfix">',
        #                          after='<div class="avito-ads-container">')
        page_info = str(File.read(output))
        if debug:
            Process.start("atom", output)
        return page_info

    @classmethod
    def parse(cls, filename, debug=False, printprettify=False):
        output = {}
        parsed = BeautifulSoup(filename, "html.parser")  # https://stackoverflow.com/questions/11709079/parsing-html-using-python
        cnt = 0
        items = (parsed.find_all('div', attrs={'class':['item','item_table']}))#.text)
        if debug:
            cprint("loaded " + str(parsed.head.title.text), "white", "on_grey")
            cprint("Count of items: " + str(len(items)), "white", "on_grey")
        for item in items:
            if printprettify:
                print(item.prettify())
                print()
            cnt += 1
            output[cnt] = {}
            try:
                output[cnt]['mini_photo'] = urlish(item.div.a.img.get('src'))
            except AttributeError as err:
                print(err)
                output[cnt]['mini_photo'] = None
            try:
                output[cnt]['name'] = item.div.a.img.get('alt')
            except AttributeError as err:
                print(err)
                output[cnt]['name'] = None
            try:
                output[cnt]['url'] = urlish(item.div.a.get('href'))
            except AttributeError as err:
                print(err)
                output[cnt]['url'] = None
            for price in item.find_all('div', attrs={'class':['about']}):
                price = stripify(price.text)
                if "руб." in price:
                    output[cnt]['price'] = price
            for dataset in item.find_all('div', attrs={'class':['data']}):
                cnt_p = 0
                for p in dataset.find_all('p'):
                    ptexts = str(p.text).split(" | ")
                    for ptext in ptexts:
                        cnt_p += 1
                        if cnt_p == 1:
                            output[cnt]["group"] = stripify(ptext)
                        elif (len(ptexts) == 2) and (cnt_p == 2):
                            output[cnt]["store"] = stripify(ptext)
                        elif (len(ptexts) == 1) and (cnt_p == 2):
                            output[cnt]["city"] = stripify(ptext)
                        else:
                            output[cnt]["store"] = "__--__"
                            output[cnt]["city"] = stripify(ptext)
            for timedate in item.find_all('div', attrs={'class':['date', 'c-2']}):
                output[cnt]["time"] = stripify(timedate.text)
        return output

    @classmethod
    def reload(cls):
        pass






json_in_memory = {}


#for i in range(10):
while True:
    filename = Page.get()
    #reply = Page.preparse()
    #if reply == 429:
    #    pass
    json_in_memory['page'+Url.get_page()+'_of_'+State.product] = Page.parse(filename)#, debug=True)#, printprettify=True)
for page, contents in json_in_memory.items():
    print(newline + page)
    for cnt, contents in contents.items():
        print()
        print(cnt)
        for key, value in contents.items():
            print(key + ":", value)

#print(json_in_memory)
