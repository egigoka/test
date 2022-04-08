#! python3
# -*- coding: utf-8 -*-
from commands import *
import pyperclip


last_string = ""


def do_old(string):
    new_string = ""

    # Print.colored(repr(string), "red")

    dates = Str.get_words(string)
    cnt = 0
    for cnt, d in enumerate(dates):
        try:
            number, date = d.split("-")
        except ValueError as e:
            print(f"{e=}: {d=}")
            raise e
        if len(number.strip()) > len(date.strip()):
            number_ = date
            date = number
            number = number_
        new_string += f"{date}\t{number}\n"
    new_string = new_string[:-1]

    # pyperclip.copy(new_string)
    # Print.colored(new_string, "green")
    # Print.colored("+", cnt+1, "magenta")
    return new_string


def do(string):
    new_rows = []

    strings = Str.nl(string)

    table = []
    for string_ in strings:
        # Print.colored(string_, "red")
        if string_.strip() == "":
            continue
        # Print.colored(string_.split("\t"), "yellow")
        try:
            _, name, cnt, dates = string_.split("\t")
            table.append({"name": name, "dates": dates, "cnt": cnt})
        except ValueError:
            name, cnt, dates = string_.split("\t")
            table.append({"name": name, "dates": dates, "cnt": cnt})
        # Print.colored(len(table), "magenta")

    for row in table:
        if not len(row["dates"]):
            continue
        Print.colored(row, "on_red")
        if len(row["dates"].strip()) == len('22,06,20'):
            # Print.colored(len(row["cnt"].strip()), len(row["dates"].strip()), "on_green")
            if len(row["cnt"].strip()) > len(row["dates"].strip()):
                number = row["cnt"]
                try:
                    date = row["dates"]
                except KeyError as e:
                    print(f"{e=} {row=}")
                    raise e
                row["cnt"] = number
                row["dates"] = date
            row_to_add = f"{row['name']}\t{row['dates']}\t{row['cnt']}"
            new_rows.append(row_to_add)
            Print.colored(row_to_add, "on_green")
        else:
            try:
                out = do_old(row['dates'])
            except ValueError as e:
                print(f"{e=}, {row=}")
                raise e
            for line in Str.nl(out):
                row_to_add = f"{row['name']}\t{line.strip()}"
                new_rows.append(row_to_add)
                Print.colored(row_to_add, "on_green")
        # Print.colored(len(new_rows), "magenta")

    new_string = "\n".join(new_rows)
    # Print.colored(new_string, "green")
    Print.colored(len(Str.nl(new_string)), "on_magenta")
    return new_string



string = """Аджика Домашняя 360 гр. PERVA стекло, шт	6 152,000	03,06,20
Баранина "Курганская" 290 г. Халяль ключ, шт	14,000	22,04,20
Баранина тушеная 290 гр. Особая ключ, шт	1 064,000	59-10,06,20  1005-29,06,20
Баранина тушеная 325 гр. Особая ключ, шт	143,000	19,06,18
Баранина тушеная в/с 290 г. Халяль ключ, шт	284,000	22,04,20
Баранина тушеная в/с 325 г. Халяль ключ, шт	816,000	22,04,20
Ветчина говяжья 180 гр. Perva Extra ключ, шт	58,000	18,06,20
Ветчина из мяса курицы 180 гр. Perva Extra ключ, шт	21 134,000	08,06,20
Ветчина из мяса курицы 180 гр. Самокат ключ, шт	945,000	14,07,20
Ветчина Классическая  325 гр. Стандарт ключ, шт	8 796,000	1560-04,07,20   5772-12,06,20   1464-12,04,20
Ветчина Классическая 325 гр. Perva Extra  ключ, шт	2 800,000	1608-17,07,20   1192-12,06,20
Ветчина свиная "Курганская" 180 гр. ключ для ТС "Гулливер", шт	30,000	23,04,20
Ветчина свиная "Курганская" 325 гр Пригожино, шт	672,000	27,06,20
Ветчина свиная 180 гр. Perva Extra  ключ (этикет), шт	1 995,000	30-26,03,20     1965-13,06,20
Ветчина свиная 180 гр. Самокат ключ, шт	810,000	90-23,06,20   720-14,07,20
Ветчина свиная 325 гр. Perva Extra  ключ, шт	81,000	15,02,20
Говядина  "Курганская" 290 гр. Пригожино, шт	915,000	09,06,20
Говядина  "Курганская" 325 гр. Пригожино, шт	4 716,000	612-03,06,20  4104-17,07,20
Говядина  "Курганская" 340 гр. Пригожино , шт  	189 925,000	19800-14,06,20  12600-13,06,20  12600-16,06,20  2130-24,06,20  1800-10,06,20  300-31,05,20  90-30,05,20  60-04,06,20  60-16,06,20  18000-06,06,20  9000-07,06,20  5400-03,06,20  10800-09,06,20  16200-27,05,20  1800-10,06,20  1800-11,06,20  1800-26,05,20  5400-07,06,20    21600-15,06,20   3600-19,06,20  1800-16,06,20  7200-13,06,20  1800-07,06,20  5400-12,06,20  5400-10,06,20  5400-27,05,20  12600-24,06,20  5400-11,06,20  15-11,06,20  15-24,06,20  14-04,06,20  14-02,06,20  14-24,05,20  13-19,06,20
Говядина  "Курганская" 340 гр. Пригожино (этикет), шт	24 330,000	24105-11,07,20  150-18,04,20  75-08,02,20
Говядина "Курганская" 290 г. Халяль ключ , шт	11 429,000	10979-09,07,20  450-09,07,20
Говядина "Курганская" 340 гр Хозяйке на заметку, шт	150,000	105-24,11,19  45-25,04,20
Говядина "Курганская" 340 гр. Байкал, шт	82 305,000	16185-28,06,20  8430-30,06,20  16800-27,06,20  5400-29,06,20  4890-24,06,20  9000-15,06,20  1800-11,06,20  5400-07,06,20  12600-28,05,20  1800-02,05,20
Говядина "Курганская" 340 гр. Щедрое застолье, шт	645,000	630-27,04,20  15-18,11,19
Говядина "Курганская" 525 г. Пригожино, шт	3 312,000	2952-17,07,20   360-04,05,19
Говядина "Курганская" 525 г. Пригожино (синоним без сл "Курганская"), шт	6 552,000	2892-27,06,20   3660-26,06,20
Говядина Волжская 325 гр Волга, шт	6 096,000	1440-27,06,20  1668-04,07,20  2988-13,07,20
Говядина Курганская 340 гр СТМ Хлеб соль, шт	53 430,000	3600-02,07,20  16200-03,07,20  16200-07,07,20  17430-06,07,20
Говядина обжаренная с черносливом 340 гр. Exclusive standard (Премиум) ключ, шт	15,000	29,05,20
Говядина тушеная  в/с 290 гр. Пригожино, шт	27 585,000	14985-12,07,20  12600-12,05,20
Говядина тушеная  в/с 338 гр. Пригожино, шт	30,000	15-29,12,18  15-30,05,19
Говядина тушеная 1/с 325 г ключ для ТС "Гулливер", шт	1 008,000	17,07,20
Говядина тушеная 1/с 338 г. Стандарт этикет, шт	29 250,000	23640-08,07,20  1800-09,07,20  3810-12,05,20
Говядина тушеная Богатырская 325 гр Стандарт, шт	6 290,000	4008-17,07,20   2280-04,07,20  2-12,06,20
Говядина тушеная в/c 290 гр. Особая ключ, шт	8 964,000	1800-29,06,20   5205-17,07,20  480-30,06,20  450-29,06,20  1020-28,06,20  9-29,05,20
Говядина тушеная в/c 325 гр. Особая ключ, шт	3 574,000	312-08,07,20  371-18,04,20  1440-,4,08,19  1440-17,09,19  11-13,09,19
Говядина тушеная в/с 290 г. Халяль ключ, шт	4 750,000	3735-09,07,20  325-13,04,20  690-10,06,20
Говядина тушеная в/с 290 г. Халяль ключ (Акция), шт	3 810,000	3270-11,09,19  540-10,06,20
Говядина тушеная в/с 290 гр СТМ Доброгост ключ, шт	5 670,000	1875-29,06,20  1020-28,06,20  2280-15,05,20  495-30,06,20
Говядина тушеная в/с 325 г. Халяль ключ, шт	2 191,000	2184-09,07,20  7-13,04,20
Говядина тушеная в/с 325 гр СТМ Мегамарт (Сунцов), шт	84,000	30,01,20
Говядина тушеная в/с 325 гр. Семейный запас, шт	564,000	516-24,05,20  48-12,0720
Говядина тушеная в/с 325 гр. Стандарт ключ, шт	9 084,000	8640-21,5,20  60-17,07,20  384-24,0320
Говядина тушеная в/с 325 гр. Стандарт Резерв, шт	1 272,000	22,06,20  
Говядина тушеная в/с 325гр. Вершины Алатау ключ, шт	10 620,000	10260-18,05,20  360-12,04,20
Говядина тушеная в/с 338 г.  Черный Стандарт ключ, шт	55 629,000	18885-08,07,20  28-22,05,20  14400-05,04,20  14400-06,04,20  1800-02,04,20  1800-31,03,20  75-10,11,18  15-07,04,20
Говядина тушеная в/с 338 г. Байкал, шт	8 760,000	03,07,19
Говядина тушеная в/с 338 г. Самокат (Премиум) ключ, шт	1 155,000	60-12,07,20  30-26,05,20  390-09,07,20  315-29,06,20  360-09,07,20
Говядина тушеная в/с 338 г. Самокат ключ, шт	1 170,000	75-19,04,20  15-09,04,20  1080-17,04,20
Говядина тушеная в/с 338 г. Семейный запас, шт	15,000	12,07,20
Говядина тушеная в/с 338 г. Стандарт, шт	30,000	01,09,18
Говядина тушеная в/с 338 г. Стандарт ключ, шт	12 345,000	08,07,20
Говядина тушеная в/с 338 г. Стандарт ключ этикет, шт	144 629,000	5400-30,05,20  10800-29,05,20  14400-06,06,20  1800-05,06,20  3600-22,05,20  3600-21,05,20  12600-09,07,20  19800-08,07,20  30-25,06,20  630-30,06,20  45-22,06,20  10814-13,06,20  5400-14,06,20  5400-19,06,20  1800-17,06,20  3600-28,06,20  3600-01,07,20  12600-05,06,20     1800-25,06,20  9000-30,,06,20  12600-01,07,20  1800-23,06,20  1800-22,06,20  1650-28,06,20  30-+22,06,20  15-09,07,20  15-27,06,20   1800-22,06,20  450-27,06,20
Говядина тушеная в/с 338 г. Стандарт ключ этикет (для НЕДРА), шт	6 030,000	5715-16,02,20  315-20,01,20
Говядина тушеная в/с 338 г. Стандарт этикет, шт	60,000	09,05,19
Говядина тушеная в/с 338 гр Оранжевая банка для ТС Мегамарт ключ, шт	1 350,000	345-28,05,20   1005-29,06,20
Говядина тушеная в/с 338 гр Правильное Решение ключ, шт	6 195,000	4425-18,09,19  15-28,0319  345-22,08,19  60-13,0619  1350-18,0619
Говядина тушеная в/с 338 гр. КУРГАН (Метрополис), шт	12 030,000	10800-31,05,20  1230-09,05,20
Говядина тушеная в/с 338 гр. Резервный продукт, шт	4 245,000	01,05,20
Говядина тушеная в/с 338 гр. СЛАТА, шт	360,000	30-10,07,19  30-15,07,19  300-09,02,20
Говядина тушеная в/с 338 гр. Стандарт Резерв, шт	3 075,000	2640-08,04,20  435-19,07,19
Говядина тушеная в/с 338 гр. Стандарт Резерв этикет ключ (Почта России), шт	10 065,000	6195-06,07,20    3750-25,01,20  120-17,04,20
Говядина тушеная в/с 338 гр. Хороший день ключ, шт	1 740,000	13,04,20
Говядина тушеная в/с 525 г. Пригожино, шт	1 440,000	12-05,03,19  1428-29,06,20
Говядина тушеная в/с 525 гр. Белый этикет (для тендера), шт	84,000	29,04,20
Говядина тушеная в/с 525 гр. Стандарт ключ, шт	1 686,000	03,06,20
Горох с говядиной  350 г Стандарт ключ, шт	3 779,000	14-05,05,20  3765-29,06,20
Горох с копченостями 315 гр. Особая ключ, шт	1 836,000	1824-13,07,20  12-11,06,20
Горох с копченостями 330 гр Стандарт, шт	13 574,000	719-27,03,20  5670-06,07,20  7185-14,07,20
Каша гречневая с говядиной  340 гр. Правильное решение ключ ГОСТ, шт	14 924,000	7305-12,07,20  405-01,05,20  5400-15,06,20  1800-01,05,20  14-31,03,20
Каша гречневая с говядиной 525 г Курганский стандарт ключ, шт	587,000	24,03,20
Каша особая гречневая с говядиной 290 гр. Халяль ключ, шт	14,000	13,04,20
Каша особая гречневая с говядиной 325 гр. Стандарт , шт	2 280,000	1440-18,05,20  840-26,04,20
Каша особая гречневая с говядиной 340 г. Стандарт, шт	3 419,000	3390-09,07,20  14-28,03,20
Каша особая гречневая с говядиной 340 г. Стандарт этикет, шт	39 360,000	6960-09,07,20  19800-16,07,20  9000-01,07,20  1800-31,05,20  1800-26,05,20  15-08,05,20   1005-16,07,20  345-09,07,20
Каша особая перловая с говядиной 290 гр. Халяль ключ, шт	14,000	13,04,20
Каша особая перловая с говядиной 340 г. Стандарт, шт	404,000	21,03,20
Каша особая перловая с говядиной 340 г. Стандарт этикет, шт	32 145,000	15-25,06,20  27870-18,07,20  4260-09,07,20  1350-09,07,20
Каша особая перловая с говядиной 340 гр Мясокомбинат (Пригожино для ТС Метрополис), шт	6 045,000	30-07,06,20   6015-09,07,20
Каша особая рисовая с говядиной 290 гр. Халяль ключ, шт	1 214,000	1169-19,04,20  45-13,04,20
Каша особая рисовая с говядиной 325 гр. Стандарт , шт	2 220,000	06,05,20
Каша особая рисовая с говядиной 340 г. Стандарт, шт	359,000	345-09,07,20  14-23,03,20
Каша особая рисовая с говядиной 340 г. Стандарт этикет, шт	11 790,000	150-30,0319  2595-05,07,20  9015-01,06,20  30-26,05,20   1350-05,07,20
Каша перловая с говядиной   340 гр. Правильное решение ключ ГОСТ, шт	19 079,000	9764-15,06,20  9315-12,07,20
Каша походная гречневая с говядиной 340 г (для КиБ), шт	4 860,000	07,03,20
Каша походная перловая с говядиной 340 г (для КиБ), шт	7 845,000	08,03,20
Конина  тушеная  338 гр. Пригожино , шт	5,000	15,07,19
Конина "Курганская" 290 г. Халяль ключ , шт	1 934,000	1769-06,08,19  165-18,04,20
Конина "Курганская" 340 гр. Пригожино , шт	8 295,000	3525-18,06,20  4770-09,07,20
Конина Волжская 325 гр Волга, шт	1 320,000	17,07,20
Конина тушеная 290 гр. Особая ключ, шт	1 914,000	1860-29,06,20  54-18,06,20
Конина тушеная 325 гр. Вершины Алатау ключ, шт	6 192,000	18,05,20
Конина тушеная 325 гр. Особая ключ, шт	770,000	22,09,19
Конина тушеная 325 гр. Стандарт ключ, шт	20 556,000	10068-17,07,20   3264-13,0720  2880-22,06,20  4344-27,06,20
Конина тушеная 338 г. ключ КУРГАН (Метрополис), шт	10 695,000	06,06,20
Конина тушеная 338 г. Семейный запас, шт	375,000	06,11,19
Конина тушеная 338 г. Стандарт ключ, шт	150,000	22,03,20
Конина тушеная 338 г. Стандарт ключ этикет, шт	8 745,000	24,06,20   225-24,06,20
Конина тушеная в/с 290 г. Халяль ключ, шт	3 254,000	18,04,20
Конина тушеная в/с 290 г. Халяль ключ (Тандер акция), шт	22 545,000	18,04,20
Конина тушеная в/с 325 г. Халяль ключ, шт	3 468,000	18,04,20
Консервы мясные Сытные из мяса гусей жб 325 гр СТО, шт	9 972,000	4716-27,06,20  2232-24,03,20  3024-04,07,20  120-27,06,20
Консервы мясные Сытные из мяса индейки жб 325 гр СТО, шт	10 308,000	7200-27,06,20   780-24,03,20  792-22,06,20  1536-04,07,20  120-27,06,20
Консервы мясные Сытные из мяса кур жб 325 гр СТО, шт	5 424,000	1524-13,07,20    2232-24,03,20  1608-26,4,20  60-27,06,20
Консервы мясные Сытные из мяса уток жб 325 гр СТО, шт	8 316,000	888-24,03,20  4428-27,06,20  3000-04,07,20
Консервы мясные Сытные из мяса цыплёнка жб 325 гр СТО, шт	960,000	27,06,20  60-24,03,20  120-27,06,20
Консервы мясные Сытные с говядиной жб 325 гр СТО, шт	7 740,000	03,06,20
Консервы мясные Сытные с говядиной жб 525 гр СТО, шт	4 452,000	2724-03,06,20   1728-13,07,20
Консервы мясные Сытные со свининой  жб 325 гр СТО, шт	1 680,000	1440-17,07,20  240-18,07,20
Консервы мясные Сытные со свининой жб 525 гр СТО, шт	6 192,000	21,05,20
Лосятина в с/с "Охотничья" 330 гр Exclusive standard (Премиум) ключ, шт	15,000	30,04,20
Мясо ветчинно-рубленое 325 гр. К завтраку (белый этикет), шт	10 440,000	4320-02,07,20  1440-30,06,20  2160-03,07,20  840-01,07,20  1440-04,07,20  240-27,06,20
Мясо ветчинно-рубленое 325 гр. К завтраку (желтый этикет), шт	2 532,000	1440-17,06,20   1092-19,01,20
Мясо косули в с/с "Охотничье" 330 гр Exclusive standard (Премиум) ключ, шт	45,000	15-26,11,19  15-01,03,20  15-20,01,20
Мясо птицы  (индейки) Российское 290 г. Халяль ключ, шт	493,000	13,04,20
Мясо птицы  (индейки) тушеное Российское 325 г. Халяль ключ, шт	1 110,000	762-04,04,19  348-13,04,20
Мясо птицы (индейки)  Российское  290 гр. Курганский Стандарт ключ, шт	1 875,000	13,05,20
Мясо птицы (индейки)  Российское  290 гр. Особая ключ, шт	789,000	540-12,07,20  249-09,4,20
Мясо птицы (индейки)  тушеное Российское 325 гр. Особая ключ, шт	335,000	22,05,20
Мясо птицы (утки) "Российское" 340 гр. Черный Стандарт ключ, шт	27 759,000	9-25,05,20  16200-02,06,19  3600-21,04,19  1800-12,04,19  4830-03,03,19  1305-02,06,20    15-25,05,20
Мясо птицы (цыплят-бройлеров) "Российское" 325 гр. ключ Рефть (Товар), шт	2,000	
Мясо цыпленка в с/с 290 гр. Халяль Ключ, шт	2 596,000	2520-18,04,20  76-29,08,19
Мясо цыпленка в с/с 325 гр. Пригожино для ТС Гулливер, шт	3 960,000	04,07,20
Мясо цыпленка в с/с 325 гр. Халяль Ключ, шт	492,000	120-11,03,19   372-18,04,20
Мясо цыпленка в с/с 350 гр. SPAR этикет, шт	480,000	345-21,11,19  135-17,09,19
Мясо цыпленка в с/с 350 гр. Правильное решение ключ , шт	7 800,000	4650-20,09,18  3150-20,03,18  
Мясо цыпленка в с/с 350 гр. Семейный запас, шт	16 097,000	11520-05,07,20  2880-08,07,20  1320-09,07,20  360-16,05,20  14-02,05,20  2-24,01,20
Мясо цыпленка в с/с 350 гр. Стандарт ключ, шт	15,000	09,04,20
Мясо цыпленка в с/с 350 гр. Стандарт ключ этикет, шт	11 955,000	9000-30,06,20   2955-29,06,20
Мясо цыпленка в с/с 350 гр. Хороший день ключ, шт	1 590,000	13,04,20
Начинка для буррито куриная 180 гр Perva ключ, шт	5 202,000	3000-25,03,20  2190-24,03,20  12-23,03,20
Начинка для буррито куриная 180 гр Perva ключ (Этикет), шт	390,000	12,07,20
Начинка для лаваша куриная 180 гр Perva ключ, шт	3 191,000	2711-22,03,20  450-03,06,20  30-24,03,20
Начинка для лаваша куриная 180 гр Perva ключ (Этикет), шт	14 441,000	360-12,07,20  2250-12,0420  11831-10,05,20
Окорок свиной подкопченный в желе 340 гр. Самокат ключ, шт	690,000	06,05,20
Оленина с ягодами можжевельника 340 гр. Exclusive standard (Премиум) ключ, шт	30,000	12,07,20
Оленина тушеная особая 290 гр. Особая ключ, шт	794,000	06,04,20
Оленина тушеная особая 325 гр Особая ключ, шт	827,000	23,05,20
Оленина тушеная особая 338 гр.Черный стандарт ключ, шт	35 890,000	795-05,07,20  1605-13,06,20  930-14,06,20  16335-05,07,20  16215-04,07,20  10-30,04,20
Паштет "Грибной" 100 гр Perva ламистер круглый, шт	18,000	15,03,20
Паштет "Грибной" 100 гр СТМ Доброгост ламистер круглый, шт	1 940,000	30,05,20 
Паштет "Нежный" с мясом птицы" 180 гр. ключ Рефть (Товар), шт	225,000	11,11,18
Паштет "Нежный" с мясом птицы" 250 гр. ключ Рефть (Товар), шт	4 048,000	30-03,08,18  280-26,08,18  1261-05,08,18  581-07,08,18  225-13,11,18  1671-31,07,18
Паштет "Охотничий" с олениной 180 г. Perva Extra ключ, шт	6 629,000	3225-10,07,20  3000-28,10,19  404-18,11,19
Паштет "Печеночный" с печенью птицы 250 гр. ключ Рефть (Товар), шт	1 050,000	26,08,18
Паштет "Сливочный" с гусиной печенью 250 гр Perva Extra ключ, шт	10 688,000	5168-22,06,20  6570-11,07,20
Паштет Деликатесный с говяжьей печенью 250 гр Мамин паштет, шт	16 410,000	1800-27,05,20  5775-06,07,20  8835-09,07,20
Паштет Деликатесный с говяжьей печенью 70 гр Perva ламистер круглый, шт	8 565,000	8344-15,07,20  196-23,07,20  25-23,04,20   280-23,04,20
Паштет Деликатесный с говяжьей печенью 95 гр Perva ламистер круглый, шт	37 319,000	21360-18,07,20   12100-30,06,20  3859-02,06,20
Паштет Деликатесный с говяжьей печенью 95 гр SPAR ламистер круглый, шт	9 760,000	600-29,06,20  380-05,03,19  8780-14,07,20
Паштет Деликатесный с говяжьей печенью 95 гр ламистер круглый СТОЕВ, шт	20,000	10,05,20
Паштет Деликатесный с говяжьей печенью 95 гр Мамин паштет ламистер круглый, шт	23 215,000	4320-19,07,20  18880-07,07,20  15-18,0320
Паштет Деликатесный с говяжьей печенью 95 гр СТМ Доброгост ламистер круглый, шт	8 820,000	8600-08,07,20  220-29,02,20
Паштет из мяса индейки 100 гр Perva ламистер круглый, шт	220,000	10,07,20
Паштет Курганский c говяжьей печенью 180 гр. Perva Extra ключ, шт	1 392,000	1380-30,06,20  12-05,03,20
Паштет Курганский острый 180 гр. Perva Extra ключ, шт	3 735,000	3000-30,06,20  735-04,06,20
Паштет Курганский с говяжьей печенью 325 гр. Perva Extra ключ, шт	1 464,000	864-05,07,20  600-04,0420
Паштет Курганский с гусиной печенью 100 гр. Perva Extra ключ, шт	3 793,000	3712-26,06,20  1-23,06,20  80-11,06,20
Паштет Курганский с гусиной печенью 180 гр. Perva Extra ключ, шт	1 395,000	30,06,20
Паштет Курганский с копченостями 325 гр. Perva Extra ключ, шт	275,000	04,04,20
Паштет Нежный с индюшиной печенью 95 гр. ламистер круглый СТОЕВ, шт	200,000	10,05,20
Паштет Печеночный с индюшиной печенью  95 гр  СТМ Доброгост ламистер круглый, шт	10 620,000	7680-08,07,20  2940-18,04,20
Паштет Печеночный с индюшиной печенью 250 гр. Мамин паштет, шт	11 234,000	6555-11,07,20  2085-12,07,20  2580-27,05,20  14-14,03,20   150-27,05,20
Паштет Печеночный с индюшиной печенью 70 гр. Perva ламистер круглый, шт	7 097,000	13-19,04,20  7084-15,07,20   280-15,07,20
Паштет Печеночный с индюшиной печенью 90 гр. Perva Extra ключ, шт	15 401,000	3280-01,07,20  8064-11,07,20  4057-23,06,20
Паштет Печеночный с индюшиной печенью 95 гр SPAR ламистер круглый, шт	7 860,000	280-10,07,20  420-06,06,20  200-29,06,20  960-17,03,20  1620-08,03,20  80-29,11,19  4280-14,07,20
Паштет Печеночный с индюшиной печенью 95 гр. Perva ламистер круглый, шт	28 959,000	5840-02,06,20  19-02,02,20  7700-24,06,20  7680-02,06,20  7680-12,05,20  40-23,03,20  20-06,06,20
Паштет Печеночный с индюшиной печенью 95 гр. Мамин паштет ламистер круглый, шт	5 219,000	900-06,11,18  180-15,02,19    4120-17,07,20  19-15,05,20
Паштет Печеночный с куриной печенью  250 гр Мамин паштет, шт	10 710,000	1605-11,10,19  7305-09,07,20  1800-20,03,20   150-09,07,20
Паштет Печеночный с куриной печенью  70 гр Perva ламистер круглый, шт	9 408,000	7616-15,07,20  1456-04,07,20  336-23,04,20   420-23,04,20
Паштет Печеночный с куриной печенью  95 гр  СТМ Доброгост ламистер круглый, шт	6 900,000	4180-30,06,20  2720-08,07,20
Паштет Печеночный с куриной печенью  95 гр Perva ламистер круглый, шт	2 379,000	1860-13,07,20  480-25,03,20  39-27,06,20
Паштет Печеночный с куриной печенью  95 гр SPAR ламистер круглый, шт	9 380,000	360-06,06,20  800-29,06,20  8220-14,07,20  
Паштет Печеночный с куриной печенью  95 гр Мамин паштет ламистер круглый, шт	7 759,000	4140-17,07,20  2460-14,03,19  1159-30,06,20
Паштет печеночный со сливочным маслом 100 гр Perva Extra ключ, шт	7 066,000	7056-12,07,20  10-25,05,20
Паштет печеночный со сливочным маслом 100 гр Perva Extra ключ (Акция), шт	5 008,000	4464-30,03,20   96-05,06,19  448-12,07,20
Паштет печеночный со сливочным маслом 250 гр Perva Extra ключ, шт	22 211,000	5400-23,06,20  9000-11,07,20  8850-14,07,20  11-16,06,20
Паштет печеночный со сливочным маслом 250 гр Курганский Стандарт этикет ключ, шт	960,000	03,12,19
Паштет печеночный со сливочным маслом 325 гр Perva Extra ключ, шт	12,000	04,04,20
Паштет с белым нутом 100 гр Perva Extra ключ, шт	8 651,000	875-11,02,20  3744-27,01,20  4032-31,01,20
Паштет с копченостями 100 гр Perva ламистер круглый, шт	210,000	10,07,20
Паштет с копченостями 100 гр СТМ Доброгост  ламистер круглый, шт	2 020,000	30,05,20
Паштет с лесными грибами 100 гр Perva Extra ключ, шт	794,000	24,02,20
Паштет с укропом 100 гр Perva ламистер круглый, шт	400,000	12,06,20
Паштет Сливочный  с гусиной печенью  95 гр  СТМ Доброгост ламистер круглый, шт	8 160,000	08,07,20
Паштет Сливочный с гусиной печенью 250 гр Мамин паштет, шт	9 669,000	7200-29,06,20  2460-09,07,20  9-10,06,20  150-09,07,20
Паштет Сливочный с гусиной печенью 70 гр Perva ламистер круглый, шт	14 837,000	109-21,08,19    12992-15,07,20  1736-04,07,20    560-21,08,19
Паштет Сливочный с гусиной печенью 95 гр Perva ламистер круглый, шт	51 819,000	21500-18,07,20  3840-10,07,20  7220-13,07,20  19200-16,07,20  19-27,06,20    1000-13,07,20
Паштет Сливочный с гусиной печенью 95 гр SPAR  ламистер круглый , шт	3 120,000	700-10,07,20  1080-14,06,20  1020-30,05,20  320-30,06,20  40-08,03,20
Паштет Сливочный с гусиной печенью 95 гр Мамин паштет ламистер круглый, шт	29 239,000	23040-19,07,20   6180-05,07,20  19-11,06,20
Печень говяжья в с/с 325 гр Особая ключ, шт	17 231,000	5448-12,06,20  695-11,06,20  11088-17,07,20
Печень говяжья в с/с 325 гр. Стандарт, шт	3 911,000	996-17,07,20  2880-04,07,20  24-12,06,20  11-03,03,20
Плов с говядиной Восточный 340 г. Стандарт, шт	6 330,000	1800-31,03,20  4530-29,06,20
Свинина  "Курганская" 290 гр. Пригожино, шт	435,000	06,06,20
Свинина  "Курганская" 340 гр. Пригожино , шт	32 639,000	15-08,06,20  16410-12,07,20  9000-08,06,20  7214-29,5,20
Свинина "Курганская" 325 гр. Пригожино, шт	1 356,000	996-17,07,20  360-30,01,20
Свинина "Курганская" 340 гр. Щедрое застолье, шт	405,000	180-27,04,20   180-18,11,19  45-29,04,19
Свинина Волжская 325 гр Волга, шт	996,000	05,05,20
Свинина тушеная 290 г. Пригожино, шт	20 055,000	5400-0503,20  10800-12,07,20  3870-16,05,20
Свинина тушеная 290 гр. Особая ключ, шт	7 634,000	4950-17,07,20  2100-29,06,20  15-23,05,20  569-30,05,20
Свинина тушеная 325 гр. Особая ключ, шт	4 607,000	1704-18,02,20  2880-17,07,20  23-04,10,19
Свинина тушеная 338 г. Пригожино, шт	6 420,000	2820-24,04,20   3600-05,04,20
Свинина тушеная 338 г. Пригожино (этикет), шт	570,000	05,04,20
Свинина тушеная 338 г. Семейный запас, шт	2 550,000	240-12,07,20  2310-19,08,19
Свинина тушеная 338 г. Стандарт ключ, шт	44,000	20,11,19
Свинина тушеная 338 г. Стандарт ключ этикет, шт	30 180,000	15-21,06,20  16200-10,05,20   5400-09,05,20  8565-31,05,20    2250-31,05,20
Свинина тушеная 338 г. Стандарт ключ этикет (Х5 Акция), шт	8 760,000	8715-07,05,20  15-11,02,20  15-17,11,19  15-16,02,20
Свинина тушеная 338 г. Стандарт Тандер Акция, шт	120,000	75-29,03,20  45-31,03,20
Свинина тушеная 338 г. Стандарт этикет, шт	1 020,000	22,03,20
Свинина тушеная 338 гр Правильное Решение ключ ГОСТ, шт	5 475,000	5400-27,04,20  30-21,04,19  15-16,4,19  15-30,03,19  15-18,04,19
Свинина тушеная 338 гр. Хороший день ключ, шт	1 365,000	60-18,03,20  1305-13,04,20
Свинина тушеная Богатырская 325 гр Стандарт, шт	1 716,000	27,06,20
Свинина тушеная в/с 290 гр СТМ Доброгост ключ, шт	2 970,000	16,05,20 
Свинина тушеная в/с 325 гр СТМ Дикси (Сунцов), шт	264,000	12-12,04,20  228-26,01,20  48-17,01,19
Свинина тушеная в/с 325 гр. Стандарт ключ, шт	9 586,000	2880-18,05,20 3084-27,06,20  2484-03,06,20 1128-17,07,20
Свинина тушеная в/с 325 гр. Стандарт Резерв, шт	852,000	22,06,20
Свинина тушеная в/с 338 г. Самокат (Премиум) ключ, шт	1 635,000	780-19,04,20   855-26,04,20
Свинина тушеная в/с 338 г. Черный Стандарт ключ, шт	25 005,000	5400-21,04,20  15990-01,07,20  1815-31,05,20  1800-22,04,20
Свинина тушеная в/с 338 гр. ключ КУРГАН (Метрополис), шт	21 105,000	5445-10,05,20    15660-01,07,20
Свинина тушеная в/с 338 гр. Стандарт Резерв, шт	1 200,000	135-22,06,20  945-29,06,20   120-18,03,20
Свинина тушеная в/с 338 гр. Стандарт Резерв этикет ключ (Почта России), шт	7 800,000	5400-05,07,20  1485-15,06,20  90-10,04,20  210-22,05,20  45-12,11,19  570-25,01,20
Свинина тушеная в/с 525 гр. Стандарт ключ, шт	2 926,000	12-18,04,20  1416-18,07,20  1498-18,04,20
Соус томатный Краснодарский 360 гр. PERVA стекло, шт	9 228,000	04,06,20
Соус томатный Острый 360 гр. PERVA стекло, шт	8 590,000	07,10,19
Соус томатный Шашлычный 360 гр. PERVA стекло, шт	9 286,000	03,06,20
Узбекский плов с курицей 525 г. Курганский стандарт ключ, шт	3 395,000	3348-18,07,20  47-27,06,20
Фасоль белая в собственном соку 400 гр. Perva, шт	2 086,000	08,05,19
Фасоль белая в томатном соусе 400 гр. Perva, шт	4 390,000	05,12,18
Фасоль красная в томатном соусе 400 гр. Perva, шт	2 492,000	204-13,11,18   2287-14,05,19
Фасоль с говядиной 350 г. Стандарт ключ, шт	3 953,000	2085-09,07,20  1680-26,06,20  8-02,04,20  180-09,07,20
Фасоль с копченостями 315 гр. Особая ключ, шт	2 650,000	1596-13,07,20  70-22,06,20  984-27,06,20
Фасоль с копченостями 330 гр Стандарт, шт	5 354,000	14,06,20
Филе индейки в собственном соку 180 гр. Perva Fitness ключ, шт	78,000	18,02,20
Филе индейки в собственном соку 180 гр. Perva Fitness ключ (Этикет), шт	3 835,000	60-12,07,20  3775-12,12,19
Филе индейки с зеленым перцем 340 гр. Самокат ключ, шт	645,000	45-04,05,20  600-21,04,20
Филе цыпленка в собственном соку 180 гр. Perva Fitness ключ, шт	228,000	18,02,20
Филе цыпленка в собственном соку 180 гр. Perva Fitness ключ (Этикет), шт	10 189,000	7918-06,04,20  60-12,07,20  1956-27,05,20  255-24,04,20
Языки свиные в собственном соку 250 гр. Cтандарт ключ, шт	3 540,000	2700-27,06,20  840-19,04,20
Языки свиные в собственном соку 325 гр. Cтандарт ключ, шт	1 965,000	1440-04,07,20  525-12,12,19
"""
pyperclip.copy(do(string))