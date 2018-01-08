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
sys.path.append("..")
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
    elif string == "spb":
        return "sankt-peterburg"
    else:
        raise IndexError("this script doesn't know how avito calls " + string)


def stripify(obj):
    output = str(obj)
    # if "|" in output:
    #     output = output[:output.find("|")]
    output = output.strip(newline)
    output = output.strip(" ")
    output = output.strip(newline)
    output = output.replace(u'\xa0', u' ')
    return output


def dirify(object_):
    print("-"*Console.width())
    print(object_.__class__.__name__)
    print("-"*Console.width())
    for subobject in dir(object_):
        if subobject[:1] != "_":
            print("==>  " + subobject)


class State:
    class Debug:
        on_parse_print_prettify = False
        print_missing_elements_while_parsing = True
        print_missing_img_elements_while_parsing = False
        print_count_of_ads_at_end_of_parsing = False
        print_status_of_page_after_parsing = False
        print_every_page_title = False
        print_wget_output = False
    class Arg:
        no_download = False
        integers = []
        for arg in sys.argv:
            try:
                integers.append(int(arg))
            except ValueError:
                pass
            if arg in ["",]:
                pass
            elif arg in ["nodownload", "nodl"]:
                no_download = True

    product = urlish("iPhone SE")
    # product = urlish("сим")
    # region = avitish("Russia")
    # region = avitish("Kurgan obl")
    region = avitish("SPB")
    number_of_pages = 100
    subfolder = "test"  # subfolder for downloaded content
    usual_number_of_ads = 50  # normal amount of ads on page



def get_Page():
    class Page:
        number = None
        html = ""
        soup = None
        soup_items = []
        json_items = {}
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
            elif cls.json_items == {}:
                status = 102  # Processing
            elif cls.ads < State.usual_number_of_ads:
                status = 206  # Partial Content
            elif (cls.number != 1) and ("страница" not in cls.title):
                status = 400  # Not normal page
            elif cls.ads >= State.usual_number_of_ads:
                status = 200  # OK
            else:
                raise Exception("not realised")
            return status

        @classmethod
        def load(cls, number):
            cls.number = number
            filename = State.product + '_in_' + State.region + "_" + str(cls.number) + ".html"  # define ouput file name
            output = Path.extend(".", State.subfolder, filename)  # define path to output file

            if not State.Arg.no_download:
                Wget.download(cls.get_url(), output=output, quiet=not State.Debug.print_wget_output)  # download file

            cls.html = str(File.read(output))
            cls.status = cls.get_status()

        @classmethod
        def preparse(cls):
            cls.soup = BeautifulSoup(cls.html, "html.parser")  # https://stackoverflow.com/questions/11709079/parsing-html-using-python
            cls.title = str(cls.soup.head.title.text)
            cls.status = cls.get_status()

        @classmethod
        def parse(cls):
            cls.preparse()
            pass
            cls.soup_items = (cls.soup.find_all('div', attrs={'class': ['item', 'item_table']}))
            cls.ads = 0
            for item in cls.soup_items:
                cls.ads += 1
                if State.Debug.on_parse_print_prettify:
                    print(item.prettify())
                    print()
                cls.json_items[cls.ads] = {}
                try:
                    cls.json_items[cls.ads]['mini_photo'] = urlish(item.div.a.img.get('src'))
                except AttributeError as err:
                    if State.Debug.print_missing_elements_while_parsing and State.Debug.print_missing_img_elements_while_parsing: print(err)
                    cls.json_items[cls.ads]['mini_photo'] = None
                try:
                    cls.json_items[cls.ads]['name'] = Str.substring(item.div.a.img.get('alt'),before="Продаю ")
                except AttributeError as err:
                    try:
                        cls.json_items[cls.ads]['name'] = stripify(item.find('div', attrs={'class':['description', 'item_table-description']}).div.h3.a.text)
                    except AttributeError as err:
                        if State.Debug.print_missing_elements_while_parsing: print(err)
                        cls.json_items[cls.ads]['name'] = None
                try:
                    cls.json_items[cls.ads]['url'] = urlish(item.div.a.get('href'))
                except AttributeError as err:
                    try:
                        cls.json_items[cls.ads]['url'] = urlish(item.find('div', attrs={'class':['description', 'item_table-description']}).div.h3.a.get('href'))
                    except AttributeError as err:
                        if State.Debug.print_missing_elements_while_parsing: print(err)
                        cls.json_items[cls.ads]['url'] = None

                cls.json_items[cls.ads]['price'] = "0"+ruble
                for price in item.find_all('div', attrs={'class':['about']}):
                    price = stripify(price.text)
                    if "руб." in price:
                        cls.json_items[cls.ads]['price'] = price.replace(" руб.", ruble)
                for dataset in item.find_all('div', attrs={'class':['data']}):
                    cnt_p = 0
                    for p in dataset.find_all('p'):
                        ptexts = str(p.text).split(" | ")
                        for ptext in ptexts:
                            cnt_p += 1
                            if cnt_p == 1:
                                cls.json_items[cls.ads]["group"] = stripify(ptext)
                            elif (len(ptexts) == 2) and (cnt_p == 2):
                                cls.json_items[cls.ads]["store"] = stripify(ptext)
                            elif (len(ptexts) == 1) and (cnt_p == 2):
                                cls.json_items[cls.ads]["city"] = stripify(ptext)
                            else:
                                # cls.json_items[cls.ads]["store"] = "__--__"
                                cls.json_items[cls.ads]["city"] = stripify(ptext)
                for timeanddate in item.find_all('div', attrs={'class': ['date', 'c-2']}):
                    cls.json_items[cls.ads]["time"] = stripify(timeanddate.text)

            cls.status = cls.get_status()

        @classmethod
        def do_your_work(cls, cnt):
            if cnt == 0:
                pass
            else:
                Print.rewrite("Downloading " + str(cnt) + " page...")
                cls.load(cnt)
                Print.rewrite("")

                Print.rewrite("Parsing " + str(cnt) + " page...")
                cls.parse()
                Print.rewrite("")
    return Page



#print(Page.get_url())
#sys.exit()

pages = {}
ads = []

def download_all_pages():
    for cnt in Int.from_to(1,State.number_of_pages):
        pages[cnt] = get_Page()  # create new page in list
        pages[cnt].do_your_work(cnt)  # download and parse page

        ############## SOME DEBUG PRINTS ###############
        if State.Debug.print_every_page_title:
            cprint("pages[" + str(cnt) + "].title " + str(pages[cnt].title), "grey", "on_white")
        if State.Debug.print_count_of_ads_at_end_of_parsing:
            cprint("pages[" + str(cnt) + "].ads " + str(pages[cnt].ads), "green", "on_white")
        if State.Debug.print_status_of_page_after_parsing:
            cprint("pages[" + str(cnt) + "].get_status() " + str(pages[cnt].get_status()), "red", "on_white")
        # cprint(json.dumps(pages[cnt].json_items, indent=4, sort_keys=True, ensure_ascii=False), "white", "on_grey")
        if pages[cnt].status != 200:  # check status
            if pages[cnt].status == 206:
                cprint("Loaded!", "white", "on_green")
            else:
                cprint("Stop loading! ERROR STATUS " + str(pages[cnt].status), "white", "on_red")
            break



def print_debug_single_position(page, item):
    print(newline, item)
    # raw soap
    # print(pages[page].soup_items[item-1].prettify(), newline)
    print(json.dumps(pages[page].json_items[item], indent=4, sort_keys=True, ensure_ascii=False))
    return pages[page].soup_items[item-1] # возвращаю соуп объект для улучшения парсера

def get_all_positions():  # пока непонятно, чо делать с данными
    for page in pages:
        for ad_cnt in pages[page].json_items:
            print_debug_single_position(page, ad_cnt)
            input()






def main():
    Bench = get_Bench()
    Bench.start()
    Bench.prefix = "Downloaded in"
    download_all_pages()
    #print_debug_single_position(1, 23)
    #print_debug_single_position(1, 24)


    #print("Debug shit:")
    #fi1_23 = print_debug_single_position(1, 23)
    #item = fi1_23
    #print(urlish(item.find('div', attrs={'class':['description', 'item_table-description']}).div.h3.a.get('href')))

    # item find
    # name = item.find('div', attrs={'class':['description', 'item_table-description']}).div.h3.a.text

    #name = item.div.a.img.get('alt')
    #get_all_positions()

    Bench.end()


main()


# old pages loader from download2 without factory of Page's
#for cnt in Int.from_to(1,100):  # What the fuck? Why it load only one page?
#    def main():
#        Page.load(cnt)
#        Page.preparse()
#        # debug_print("Page.title", Page.title)
#        cprint("Page.title " + str(Page.title), "grey", "on_white")
#        Page.parse()
#        cprint("Page.ads " + str(Page.ads), "green", "on_white")
#        cprint("Page.get_status() " + str(Page.get_status()), "red", "on_white")
#        # cprint(json.dumps(Page.json_items, indent=4, sort_keys=True, ensure_ascii=False), "white", "on_grey")
#    while Page.get_status() != 200:
#        main()
#        if Page.status == 429:
#            cprint("Too many requests", "red")
#            time.sleep(60)
#        elif Page.status == 200:
#            pass
#        else:
#            raise Exception("What status is" + str(Page.get_status()))


# def load_pages(product, region, subfolder=State.subfolder, usual_number_of_ads=State.usual_number_of_ads):

#    pages[cnt] = Page

#    raise Exception("not realised")

# load_pages(product=State.product, region=State.region)
