#! python3
# -*- coding: utf-8 -*-
# http://python.su/forum/topic/15531/?page=1#post-93316
import sys
sys.path.append("../..")
sys.path.append("..\..")
sys.path.append(".")
sys.path.append("..")
sys.path.append("./term")
sys.path.append(r".\term")
from commands8 import *
from base64_8 import *
from temp_html import sss, html_doc
from bs4 import BeautifulSoup
sys.path.append(Path.extend(".", "scripts", "avitoparse"))
#sys.path.append(r".\scripts\avitoparse")
#sys.path.append(r"./scripts/avitoparse")
#from download3 import urlish


def urlish(string, force_lowercase=True):
    # приведение имени в строку, поддерживаемую в url
    if force_lowercase:
        string = string.lower()
    string = string.replace(' ', '+')
    return string

soup = BeautifulSoup(html_doc, 'html.parser')
#Print.debug("*soup.find_all()", *soup.find_all("img",class="image event__img"))

lines = Str.newlines_to_strings(sss)

splitted = []
cnt = 0

for line in lines:
    try:
        splitted[cnt]
    except IndexError:
        #output[cnt] = list()
        splitted.append(list())
    splitted[cnt].append(line)
    for cinema in ["кинотеатрах", "кинотеатре", "Родина", "Каро", "Дом Кино", "Angleterre Cinema Lounge", "Аврора"]:
        if cinema in line:
            cnt+=1

#Print.debug(*splitted)

bd = []
cnt=-1
for film in splitted:
    bd.append({})
    cnt+=1
    #print(len(film))
    #if len(film)>7:
    #    print(film)
    bd[cnt]["filmname"] = film[0]
    bd[cnt]["youtube_link"] = "https://www.youtube.com/results?search_query=" + urlish(bd[cnt]["filmname"]+" трейлер", force_lowercase=False)
    try:
        Str.get_integers(film[2])[1]
        bd[cnt]["rating"] = film[2]
        bd[cnt]["genre"] = film[3]
    except IndexError:
        bd[cnt]["rating"] = "нет :("
        bd[cnt]["genre"] = film[2]
    ##############Print.debug(splitted[cnt],bd[cnt])  # - инфа
#Print.debug(*bd)
print(len(bd))

print(len(soup.find_all("div", {"class": "event"})))

for aaa in soup.find_all("div", {"class": "event"}):
    aaa = aaa.a  # гениально, я себя обожаю
    aaa = str(aaa)
    aaa = Str.substring(aaa, before='href="', after='"')
    #Print.debug("https://afisha.yandex.ru"+aaa.replace("?schedule-preset=tomorrow", "?schedule-date=2018-04-15"))

print(len(soup.find_all("img", {"class": "event__img"})))
for png in soup.find_all("img", {"class": "event__img"}):
    #Print.debug(png.prettify(), Str.substring(png.prettify(), before='src="data:image/png;base64,', after='" '))
    pass
cnt=0
#for png in soup.find_all("img", {"class": "event__img"}):
#    cnt+=1
#    png_base64 = Str.substring(png.prettify(), before='src="data:image/png;base64,', after='" ')
#    print(len(png_base64))
#    import base64_8
#    #Base64.to_png(png_base64, filename=cnt)
#    #Print.debug(png_base64, png_recovered, raw=True)


#from temp_html import xml
#return_s = xml
#b64strings = []
#cnt = 0
#while return_s:
#    cnt+=1
#    Print.rewrite(cnt)
#    print()
#    b64string, return_s = Str.substring(return_s, before="data:image/png;base64,", after=")", return_after_substring=True)
#    print("len(return_s)", len(return_s), "len(b64string)", len(b64string), "len(b64strings)", len(b64strings))
#    if b64string == "":
#        break
#    b64strings.append(b64string)

#print(b64strings)
#cnt = 0
#for b64string in b64strings:
#    cnt += 1
#    Base64.to_png(b64string, cnt)

import tmdbsimple as tmdb
import uuid

tmdb.API_KEY = 'f7b34fec9298959611b1a513cdb48c0d'

class Tmdb:
    @staticmethod
    def image(url, width="original", outputfile=str(uuid.uuid4())+".png", no_download=False):
        width_symbol = ""
        if width != "original":
            width_symbol = "w"

        url = "https://image.tmdb.org/t/p/" + width_symbol + str(width) + str(url)
        if not no_download: Wget.download(url=url, output=outputfile)
        return url

    @classmethod
    def downloadimage(cls, film_name, outputfile, width, no_download):
        Print.rewrite("-")
        search = tmdb.Search()
        response = search.movie(query=film_name)
        Print.rewrite(backslash)
        if response["total_results"] == 1:
            print("all okay")
            filmid = search.results[0]["id"]
        else:
            cnt = 0
            Print.rewrite("|")
            filmid = None
            failsafe_None_filmid_cnt = 0
            while not filmid:
                if failsafe_None_filmid_cnt < 1000:
                    failsafe_None_filmid_cnt += 1
                else:
                    raise UnboundLocalError("what wrong with " + film_name + "?")
                Print.rewrite("/"+str(len(response)))
                print("Все варианты:")
                for film in search.results:
                    print(film["original_title"] + "(" + str(film['release_date']) + ")")
                print()
                for film in search.results:
                    cnt+=1
                    print(film_name, "is", film["original_title"]+"("+str(film['release_date'])+")?")

                    answer = None
                    # answer = "y"  # заглушка
                    while not answer:
                        input_ = input("y/n?")
                        if input_ == "y":
                            answer = "y"
                        elif input_ == "n":
                            answer = "n"
                        else:
                            pass

                    if answer == "y":
                        filmid = film["id"]
                        break


        return Tmdb.image(tmdb.Movies(filmid).info()['backdrop_path'],
                            outputfile=outputfile,width=width, no_download=no_download)


cnt = 0
for film in bd:
    cnt += 1
    print(cnt)
    if (film["filmname"] not in ["Мульт в кино. Выпуск №73. Просто космос!",
                                "Italian Best Shorts 2: Любовь в вечном городе",
                                "Oscar Shorts 2017: Фильмы",
                                "Фестиваль короткометражной анимации «А4»",
                                "Best of shnit 2017"]):
        bd[cnt-1]["img"] = Tmdb.downloadimage(film["filmname"], str(cnt)+"_"+film["filmname"]+".png", width=200, no_download=True)


Json.save("films.json", bd)
#movie = tmdb.Movies(123)
#print(movie.info())

#Tmdb.image(movie.info()['backdrop_path'])
#Tmdb.image(movie.info()['poster_path'])
