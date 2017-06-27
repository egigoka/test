#! python3
# -*- coding: utf-8 -*-


from utils import winRepair_UnicodeEncodeError, path_extend, currentfolder, loadjson, savejson, ruble, cls
import collections


__json__ = path_extend(currentfolder(), "battaries_del.py.json")


battaries = loadjson(__json__)
battaries = collections.OrderedDict(sorted(battaries.items())) # sorted dict
winRepair_UnicodeEncodeError(quiet = True)


def printall():
    #battaries = {'alcatel': {'brr': {'price': 1000, 'capacity': 5000}, 'bf1': {'price': 100, 'capacity': 2000}}}
    for _maintainer, _models in battaries.items():
        for _model, _characterictics in _models.items():
            price = str(_characterictics["price"])
            capacity = str(_characterictics["capacity"])
            cost = int(price) / int(capacity)
            print(_maintainer, _model, price + ruble, capacity\
                  + "MAh", "  цена за 1MAh:", str(cost)[0:4] + ruble)


def main():
    try:
        cls()
        printall()
        try:
            maintainer
            print ("mainteiner is exist")
            previous_maintainer = maintainer
        except:
            print("mainteiner isn't exists")
            do = "nothing"
        maintainer = input("Производитель: ")
        maintainer = maintainer.title()
        global maintainer
        if maintainer == "":
            maintainer = previous_maintainer
        model = input("Модель: ")
        model = model.upper()
        price = input("Цена: ")
        capacity = input("Ёмкость: ")
        if maintainer not in battaries.keys():
            battaries[maintainer] = {}
        battaries[maintainer][model] = {}
        battaries[maintainer][model]["capacity"] = int(capacity)
        battaries[maintainer][model]["price"] = int(price)
        savejson(__json__, battaries)
        printall()
    except KeyboardInterrupt:
        print("^C")



while True:
    main()