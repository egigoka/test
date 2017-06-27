#! python3

from utils import *

__file_to_parse__ = path_extend(currentfolder(), "toparse.txt")

parseline = ""

file = open(__file_to_parse__, 'r')
for line in file:
    parseline += line
file.close()

#print (parseline)

pricecode = '<span data-of="price-total" data-product-param="price" data-value="'
priceend = '"'
while
priceio = substring(parseline, pricecode, priceend)
price = priceio[0]
parseline = parseline[priceio[1]:]
print ("price =", price)

#def getNext
print ('Ёмкость')
print (parseline.find('" class="ec-price-item-link">['))
print ('Модель')
print (parseline.find('" class="ec-price-item-link">'))
print ('Производитель')
print (parseline.find('<span class="category-group-title">'))
#print (parseline[,])