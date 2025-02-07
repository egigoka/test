from commands import *
import datetime


def to_min_sec(sec):
    min = int(sec // 60)
    sec = str(int(sec % 60)).zfill(2)
    return min, sec

context = paste()

ll = Str.nl(context)

my = 0
not_my = 0

for cnt, l in enumerate(ll):
    if cnt == 0:
        continue
    if l == "":
        continue

    previous = ll[cnt-1]

    previous = Str.substring(previous, '"', '"')
    current = Str.substring(l, '"', '"')

    df = "%d.%m.%Y %H:%M:%S"
    previous = datetime.datetime.strptime(previous, df)
    current = datetime.datetime.strptime(current, df)
    delta = Time.delta(previous, current)

    #print(ll[cnt-1])
    #print(l)
    #print(f"{cnt % 2=} {current=} {previous=} {delta=}")
    
    if cnt % 2 == 0:
        my += delta
    else:
        not_my += delta

my_min, my_sec = to_min_sec(my)
not_my_min, not_my_sec = to_min_sec(not_my)
total_min, total_sec = to_min_sec(my + not_my)

result = f"Время выполнения: {my_min}:{my_sec} - обработка у нас, {not_my_min}:{not_my_sec} - обработка запроса на стороне МЛ, {total_min}:{total_sec} всего"

print(result)
copy(result)
