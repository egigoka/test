from commands import *

text = ""
for cnt, line in enumerate(Str.nl(File.read("text.txt"))):
    line = line.replace(",", ".")
    if cnt%4 == 0 and cnt != 0:
        text = text[:-1] + newline
    text += line + ","
text = text[:-1]

for line in Str.nl(text):
    no, name, taste, price = line.split(",")
    price += ruble
    if Str.get_integers(price)[0] < 300:
        print(no, name, taste, price)

