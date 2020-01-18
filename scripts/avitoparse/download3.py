#! python3
# -*- coding: utf-8 -*-
# import pymongo
import sys
try:  # https://stackoverflow.com/questions/11709079/parsing-html-using-python
    from BeautifulSoup import BeautifulSoup
except ImportError as exception:
    from bs4 import BeautifulSoup
    #raise ImportError(exception)
from commands import *


def urlish(string, force_lowercase=True):
    # приведение имени в строку, поддерживаемую в url
    if force_lowercase:
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

    product_original_name = "iPhone X"
    product = urlish(product_original_name)
    # product = urlish("сим")
    # region = avitish("Russia")
    # region = avitish("Kurgan obl")
    region = avitish("SPB")
    number_of_pages = 100
    subfolder = "test"  # subfolder for downloaded content
    usual_number_of_ads = 50  # normal amount of ads on page


class Page:
    def __init__(self):
        self.number = None
        self.html = ""
        self.soup = None
        self.soup_items = []
        self.json_items = {}
        self.filename = ""
        self.title = ""
        self.ads = 0
        self.status = 204  # No Content

    def get_url(self):
        url = "https://www.avito.ru/" + State.region + "?p=" + str(self.number) + \
              "&s=2&q=" + State.product
        return url

    def get_status(self):
        status = 204  # No Content
        if "Чтобы продолжить пользоваться сайтом, пожалуйста, введите символы с картинки" in self.html:
            status = 429  # Too Many Requests
        elif self.html == "":
            status = 204  # No Content
        elif self.title == "":
            status = 100  # Continue
        elif self.json_items == {}:
            status = 102  # Processing
        elif self.ads < State.usual_number_of_ads:
            status = 206  # Partial Content
        elif (self.number != 1) and ("страница" not in self.title):
            status = 400  # Not normal page
        elif self.ads >= State.usual_number_of_ads:
            status = 200  # OK
        else:
            raise NotImplementedError()
        return status

    def load(self, number):
        self.number = number
        filename = State.product + '_in_' + State.region + "_" + str(self.number) + ".html"  # define ouput file name
        output = Path.combine(Path.working(), State.subfolder, filename)  # define path1 to output file

        if not State.Arg.no_download:
            Print.debug("wget output", Wget.download(self.get_url(), output_filename=output, quiet=not State.Debug.print_wget_output, no_check_certificate=OS.windows))

        self.html = str(File.read(output))
        self.status = self.get_status()

    def preparse(self):
        self.soup = BeautifulSoup(self.html, "html.parser")  # https://stackoverflow.com/questions/11709079/parsing-html-using-python
        try:
            self.title = str(self.soup.head.title.text)
        except AttributeError:
            pass
        self.status = self.get_status()

    def parse(self):
        self.preparse()
        pass
        self.soup_items = (self.soup.find_all('div', attrs={'class': ['item', 'item_table']}))
        self.ads = 0
        for item in self.soup_items:
            self.ads += 1
            if State.Debug.on_parse_print_prettify:
                print(item.prettify())
                print()
            self.json_items[self.ads] = {}
            try:
                self.json_items[self.ads]['mini_photo'] = urlish(item.div.a.img.get('src'))
            except AttributeError as err:
                if State.Debug.print_missing_elements_while_parsing and State.Debug.print_missing_img_elements_while_parsing: print(err)
                self.json_items[self.ads]['mini_photo'] = None
            try:
                self.json_items[self.ads]['name'] = Str.substring(item.div.a.img.get('alt'), before="Продаю ", safe=True)
            except AttributeError as err:
                try:
                    self.json_items[self.ads]['name'] = stripify(item.find('div', attrs={'class':['description', 'item_table-description']}).div.h3.a.text)
                except AttributeError as err:
                    if State.Debug.print_missing_elements_while_parsing: print(err)
                    self.json_items[self.ads]['name'] = None
            try:
                self.json_items[self.ads]['url'] = urlish(item.div.a.get('href'))
            except AttributeError as err:
                try:
                    self.json_items[self.ads]['url'] = urlish(item.find('div', attrs={'class':['description', 'item_table-description']}).div.h3.a.get('href'))
                except AttributeError as err:
                    if State.Debug.print_missing_elements_while_parsing: print(err)
                    self.json_items[self.ads]['url'] = None

            self.json_items[self.ads]['price'] = "fuck" #"0" + ruble
            for price in item.find_all('div', attrs={'class': ['about']}):
                price = stripify(price.text)
                #if "руб." in price:
                self.json_items[self.ads]['price'] = price.replace(" руб.", ruble)
            #print(self.json_items[self.ads]['price'])
            for dataset in item.find_all('div', attrs={'class':['data']}):
                cnt_p = 0
                for p in dataset.find_all('p'):
                    ptexts = str(p.text).split(" | ")
                    for ptext in ptexts:
                        cnt_p += 1
                        if cnt_p == 1:
                            self.json_items[self.ads]["group"] = stripify(ptext)
                        elif (len(ptexts) == 2) and (cnt_p == 2):
                            self.json_items[self.ads]["store"] = stripify(ptext)
                        elif (len(ptexts) == 1) and (cnt_p == 2):
                            self.json_items[self.ads]["city"] = stripify(ptext)
                        else:
                            # self.json_items[self.ads]["store"] = "__--__"
                            self.json_items[self.ads]["city"] = stripify(ptext)
            for timeanddate in item.find_all('div', attrs={'class': ['date', 'c-2']}):
                self.json_items[self.ads]["time"] = stripify(timeanddate.text)

        self.status = self.get_status()

    def do_your_work(self, cnt):
        if cnt == 0:
            pass
        else:
            Print.rewrite("Downloading " + str(cnt) + " page...")
            self.load(cnt)

            Print.rewrite("Parsing " + str(cnt) + " page...")
            self.parse()
            Print.rewrite("")


#print(Page.get_url())
#sys.exit()

pages = {}
ads = []


def download_all_pages():
    for cnt in Int.from_to(1,State.number_of_pages):
        pages[cnt] = Page()  # create new page in list
        pages[cnt].do_your_work(cnt)  # download and parse page

        ############## SOME DEBUG PRINTS ###############
        if State.Debug.print_every_page_title:
            Print.colored("pages[" + str(cnt) + "].title " + str(pages[cnt].title), "grey", "on_white")
        if State.Debug.print_count_of_ads_at_end_of_parsing:
            Print.colored("pages[" + str(cnt) + "].ads " + str(pages[cnt].ads), "green", "on_white")
        if State.Debug.print_status_of_page_after_parsing:
            Print.colored("pages[" + str(cnt) + "].get_status() " + str(pages[cnt].get_status()), "red", "on_white")
        # cprint(json.dumps(pages[cnt].json_items, indent=4, sort_keys=True, ensure_ascii=False), "white", "on_grey")
        if pages[cnt].status != 200:  # check status
            if pages[cnt].status == 206:
                Print.colored("Loaded!", "white", "on_green")
            else:
                Print.colored("Stop loading! ERROR STATUS " + str(pages[cnt].status), "white", "on_red")
            break


def print_debug_single_position(page, item):
    import json
    # raw soap
    # print(pages[page].soup_items[item-1].prettify(), newline)
    print(json.dumps(pages[page].json_items[item], indent=4, sort_keys=True, ensure_ascii=False))
    return pages[page].soup_items[item-1] # возвращаю соуп объект для улучшения парсера


def get_all_positions():  # пока непонятно, чо делать с данными
    for page in pages:
        for ad_cnt in pages[page].json_items:
            print("page", page, "item", ad_cnt)
            print_debug_single_position(page, ad_cnt)
            input()


def print_all_prices():
    for page_cnt, page in Dict.iterable(pages):
        for item_cnt, item in Dict.iterable(page.json_items):
            print(f'page {page_cnt} item {item_cnt} {item["price"]}')


def represent_prices(step=1000, min_count_items=10, min_price=10000):
    prices = []
    prices_repr = {}
    for page_cnt, page in Dict.iterable(pages):
        for item_cnt, item in Dict.iterable(page.json_items):
            add = True
            for subname in State.product_original_name:
                if not subname.lower() in item["name"].lower():
                    add=False
            if add:
                prices.append(item["price"])
            else:
                pass  # print(item["name"])
    for price in prices:
        try:
            price = int(price.strip("  ₽").replace(" ", ""))
        except ValueError:
            continue
        val = price//step
        repr_name = val*step  # f"{val*step}-{val*step+step}"
        try:
            prices_repr[repr_name] += 1
        except KeyError:
            prices_repr[repr_name] = 1
    for repr_name, count in Dict.iterable(Dict.sorted_by_key(prices_repr)):
        if count>=min_count_items and repr_name>=min_price:
            print(f"{repr_name}: {count}{newline}{'*'*count}")
    return prices_repr


def get_all_items():
    output_items = []
    for page_cnt, page in Dict.iterable(pages):
        for item_cnt, item in Dict.iterable(page.json_items):
            output_items.append(item)
    return output_items


def main():
    bench = Bench()
    bench.start()
    bench.prefix = "Downloaded in"
    download_all_pages()

    print_all_prices()

    represent_prices()

    bench.end()


if __name__ == '__main__':
    main()


# old pages loader from download2 without factory of Page's
# for cnt in Int.from_to(1,100):  # What the fuck? Why it load only one page?
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
