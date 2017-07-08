#! python3
# -*- coding: utf-8 -*-

try:  # https://stackoverflow.com/questions/11709079/parsing-html-using-python
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

from commands7 import *
import myhtmlsheetyparser

File.copy(Path.extend("..","..","commands7.py"), "commands7.py")


def urlish(string):
    string = string.lower()
    string = string.replace(' ', '+')
    return string


def avitish(string):
    string = urlish(string)
    if string == "russia":
        return "rossiya"
    else:
        raise IndexError("this script doesn't know how avito calls" + string)




class State:
    product = urlish("iPhone SE")
    region = avitish("Russia")
    subfolder = "test"






class Url:
    page = 0

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
    pages = []
    @classmethod
    def get(cls, debug=False):
        # define ouput file name
        filename = State.product + '_in_' + State.region + str(Url.page+1) + ".html"
        # define path to output file
        output = Path.extend(".", State.subfolder, filename)
        # download file
        Wget.download(Url.get(), output=output)
        # create blank string to parse
        onestring = ""
        with open(output, "r") as f:
            page_info = f.read()
        page_info = Str.substring(page_info,
                                  before = '<div class="catalog-list clearfix">',
                                  after='<div class="avito-ads-container">')
        if debug:
            Process.start("atom", output)
        return page_info


page = Page.get()
#debug_print("page", page)
page_lines = Str.newlines_to_strings(page)
#debug_print("page_lines", page_lines)

parsed = BeautifulSoup(page, "html.parser")  # https://stackoverflow.com/questions/11709079/parsing-html-using-python
#debug_print("parsed", parsed)
parsed = parsed.prettify()
print(parsed)
sys.exit()
parsed_lines = Str.newlines_to_strings(parsed)
for line in parsed_lines:
    line = line.lstrip(" ")
    myhtmlsheetyparser.s_print(line)
#print (parsed_html.body.find('div', attrs={'class':'container'}).text)
