#!python3

import vk_requests
import requests
import time
import sys
import wget
import os

import win_unicode_console
win_unicode_console.enable()

import test11vk_test_usuless_login

# print(test11vk_test_usuless_login.varVkUser)
# print(test11vk_test_usuless_login.varVkPass)

api = vk_requests.create_api(app_id=5569080, login=test11vk_test_usuless_login.varVkUser, password=test11vk_test_usuless_login.varVkPass) # todo включить авторизацию
# api = vk_requests.create_api() # создание сессии без логина

#print(api.users.get(user_ids=1))
#print()
#print(api.users.get(user_ids=49920173))
#print()
cnt = 0  # с какого поста начинать отображать
cntend = 0  # последний пост
cntuse = 0  # используемый счётчик
timeSleep = .250  # так как программа однопоточная, то чтобы вк не банил, стоит задержка в 250 мс
#timeSleep = .500
whitespace = "   "  # отступ
postCount = 1  # количество постов за раз скачивать
group = "egigokasprint"

# temp vars
isDownloaded = 0 # todo сделать по-нормальному
# todo сделать проверку на повторяющиеся посты


def wprint(depth):
    print(whitespace * depth, end="")


def downloadImg(url):
    time.sleep(timeSleep)
    try:
        wget.download(url, out="C:/temp/") #, temp_dir = u"C:\temp" )  # todo вместо скачивания сделать gui
        global isDownloaded
        isDownloaded = 1
    except ConnectionResetError as err:
        print("Fuck! It doesn't downloaded again. Sleep for 5 secs...")
        time.sleep(5)
        print(err)
        downloadImg(url = url)
    except TimeoutError as err:
        print("Fuck! Timeout! Sleep for 10 secs...")
        time.sleep(10)
        print(err)
        downloadImg(url = url)
    except TypeError as err:
        print("Fuck! Timeout! Sleep for 10 secs...")
        time.sleep(10)
        print(err)
        downloadImg(url=url)
    except requests.exceptions.ReadTimeout as err:
        print("Fuck! Timeout! Sleep for 10 secs...")
        time.sleep(10)
        print(err)
        downloadImg(url=url)
    except NameError as err:
        print("Fuck! Something WRONG! Sleep for 10 secs...")
        time.sleep(10)
        print(err)
        downloadImg(url=url)
    else:
        print("Fuck! Unnown error! Sleep for 10 secs...")
        time.sleep(10)
        print(err)
        downloadImg(url=url)

def valueToGui(key, аоавл value, depth):
    photo0 = None
    photo1 = None
    photo2 = None
    photo3 = None
    photo4 = None
    photo5 = None
    photo6 = None
    photo7 = None
    photo8 = None
    photo9 = None
    if (key == "") & (value == None):
        print()
    else:
        print("Key '" + str(key) + "', value '" + str(value) + "' and depth '" + str(depth) + "' is not supported in GUI.")
        print("Script is ending at output", cnt)
        sys.exit()


def valuePrintCmd(key, value = None, depth = 0):
    wprint(depth)
    if (key == "photo") & (value is None):
        print("Фото:")
    elif (key == "height"):
        print("Высота фото:", value)
        global photoHeight
        photoHeight = value
    elif key[0:5] == "photo":
        print("Фото с высотой " + key[6:] + ":", value) # todo start of photo
        if ((int(key[6:]) >= int(photoHeight)) & (isDownloaded == 0)): # todo bug
            while isDownloaded == 0: # чоооо?
                downloadImg(value)
        else:
            print(key[6:], photoHeight)
    elif key == "text":
        print("Текст:", value)  # todo обработка оригинала фото
        #  fuck = input()

    elif key == "width":
        print("Ширина фото:",value) # todo end of photo
        global isDownloaded
        if isDownloaded == 1:
            isDownloaded = 0
        else:
            #input("Fuck! Dat imag iz not downloaded!")
            err = "echo img in post " + str(cnt) + " is not downloaded >> log_vk.log"
            os.system(err)
            print(err)
            os.system("timeout 120")
    elif (key == "count") & (depth == 0):
        print("Количество записей в группе:", value)
        if cntend == 0:
            global cntend
            cntend = value
    elif key == "items":
        print("Начало поста:")
    elif key == "comments":
        print("Комментарии:",)
    elif (key == "count") & (depth == 2):
        print("Количество:", value)
    elif key == "copy_history":
        print("История репостов:")
    elif key == "attachments":
        print("Вложения:")
    elif key == "access_key":
        print("Код доступа:", value)
    elif key == "album_id":
        print("ID альбома:", value)
    elif (key == "date") & (depth == 1):
        print("Дата поста:", value)
    elif key == "date":
        print("Дата:", value)
    elif (key == "id") & (depth == 1):
        print("ID поста:", value)
    elif (key == "id"):
        print("ID", value)
    elif (key == "lat") | (key == "latitude"):
        print("latitude:", value)
    elif (key == "long") | (key == "longitude"):
        print("longitude:", value)
    elif (key == "owner_id") & (depth == 1):
        print("ID владельца поста:", value)
    elif (key == "owner_id"):
        print("ID владельца:", value)
    elif (key == "post_id"):
        print("ID поста", value)
    elif (key == "user_id"):
        print("ID пользователя:", value)
    elif (key == "type") & (value == "photo"):
        print("Тип:", "фото")
    elif (key == "type") & (value == "audio"):
        print("Тип:", "музыка")
    elif (key == "type") & (value == "doc"):
        print("Тип:", "документ")
    elif (key == "type") & (value == 2):
        print("Неизвестный тип:", "2")
    elif (key == "type") & (value == "link"):
        print("Тип:", "ссылка")
    elif (key == "type") & (value == "album"):
        print("Тип:", "альбом")
    elif (key == "type") & (value == "point"):
        print("Тип", "геометка")
    elif (key == "type") & (value == "poll"):
        print("Тип:", "голосование")
    elif (key == "type") & (value == "api"):
        print("Тип:", "API")
    elif (key == "type") & (value == "vk"):
        print("Тип:", "VK")
    elif (key == "type") & (value == "mvk"):
        print("Тип:", "m.VK")
    elif (key == "platform") & (value == "iphone"):
        print("Платформа", "iPhone")
    elif (key == "platform") & (value == "android"):
        print("Платформа", "Android")
    elif (key == "platform") & (value == "wphone"):
        print("Платформа:", "Windows Phone")
    elif (key == "platform") & (value == "ipad"):
        print("Платформа:", "iPad")
    elif (key == "platform") & (value == "instagram"):
        print("Платформа", "Instagram")
    elif (key == "from_id"):
        print("Опубликовано пользователем:", value)
    elif (key == "likes"):
        print("Лайки:")
    elif (key == "post_type") & (value == "post"):
        print("Тип поста:", "пост")
    elif (key == "post_type") & (value == "photo"):
        print("Тип поста:", "фото")
    elif (key == "post_type") & (value == "reply"):
        print("Тип:", "ответ")
    elif (key == "reply_post_id"):
        print("ID отвеченного поста", value)
    elif (key == "reposts"):
        print("Репосты:")
    elif (key == "post_source"):
        print("Источник поста:")
    elif (key == "signer_id"):
        print("ID предложившего новость:", value)
    elif (key == "audio"):
        print("Музыка:")
    elif (key == "artist"):
        print("Исполнитель:", value)
    elif (key == "duration"):
        print("Длительность:", value, "секунд")
    elif (key == "genre_id"):
        print("ID жанра:", value)
    elif (key == "title"):
        print("Название:", value)
    elif (key == "url"):
        print("URL:", value)
    elif (key == "lyrics_id"):
        print("ID слов песни:", value)
    elif (key == "doc"):
        print("Документ:")
    elif (key == "ext"):
        print("Расширение:", value)
    elif (key == "preview"):
        print("Предпросмотр:")
    elif (key == "sizes"):
        print("Размеры:", value)
    elif (key == "src"):
        print("Источник:", value) #todo тут бывает появляются фото (возможно, гифки)
    elif (key == "type") & (value == "m"):
        print("Тип:", "мальенький") # todo
    elif (key == "type") & (value == "s"):
        print("Тип:", "средний") # todo
    elif (key == "type") & (value == "o"):
        print("Тип:", "оригинал")  # todo
    elif (key == "video"):
        print("Видео:")
    elif (key == "file_size"):
        print("Размер файла:", value)
    elif (key == "size"):
        print("Размер:", value)
    elif (key == "type") & (value == 3):
        print("", value)
    elif (key == "link"):
        print("Ссылка:")
    elif (key == "description"):
        print("Описание:", value)
    elif (key == "album"):
        print("Альбом:")
    elif (key == "created"):
        print("Создан:", value)
    elif (key == "thumb"):
        print("Миниатюры:")
    elif (key == "updated"):
        print("Обновлён:", value)
    elif (key == "geo"):
        print("Геотег:")
    elif (key == "coordinates"):
        print("Координаты:", value)
    elif (key == "place"):
        print("Место:")
    elif (key == "city"):
        print("Город:", value)
    elif (key == "country"):
        print("Страна:", value)
    elif (key == "icon"):
        print("Иконка:", value)
    elif (key == "data") & (value == "profile_photo"):
        print("Данные:", "фотография профиля")
    elif (key == "poll"):
        print("Голосование:", value)
    elif (key == "anonymous"):
        print("Анонимное:", value)
    elif (key == "answer_id"):
        print("ID ответа:", value)
    elif (key == "answers"):
        print("Ответы:")
    elif (key == "rate"):
        print("Показатель:", value)
    elif (key == "votes"):
        print("Голосов:", value)
    elif (key == "question"):
        print("Вопрос:", value)
    elif (key == "can_post"):
        print("Может ли постить?", value)
    elif (key == "can_like"):
        print("Может ли лайкать?", value)
    elif (key == "can_publish"):
        print("Может ли публиковать?", value)
    elif (key == "user_likes"):
        print("Лайкнуто?", value) # todo лайк от текущего юзера :3
    elif (key == "user_reposted"):
        print("Репостнуто?", value)
    else:
        print("Key '" + str(key) + "', value '" + str(value) + "' and depth '" + str(depth) + "' is not supported.")
        print("Script is ending at output", cnt)
        sys.exit()
    valueToGui(key, value, depth)

def printListReversely(input_, depth=0):
    for value in input_:
        if isinstance(value, list):
            for value_ in value:
                #print(whitespace * depth + (value_))  # Напечатать только ключ, так как значение это большой (не факт) лист (факт)
                valuePrintCmd(value_, depth=depth + 1)
                printReversely(value, depth + 1)
                print("")
        elif isinstance(value, dict):
            printReversely(value, depth)
        else:
            print("ЕГГОГ! Этава! Не можед! Быд!")
            print("type of input_: ", type(input_))


def printReversely(input_, depth=0):
    if isinstance(input_, dict):
        for key, value in sorted(input_.items(), key=lambda x: x[0]):
            if isinstance(value, dict):
                #print (whitespace*depth + (key)) # Напечатать только ключ, так как значение это большой (не факт) словарь (факт)
                valuePrintCmd(key, depth = depth)
                printReversely(value, depth + 1)
            elif isinstance(value, list):
                #print(key)
                valuePrintCmd(key, depth = depth)
                printListReversely(value, depth+1) #обход листа
            else:
                #print (whitespace*depth + "%s %s" % (key, value)) # Напечатать и ключ, и значение, так как это просто значение
                valuePrintCmd(key, value, depth)
    elif isinstance(input_, list):
        for key in input_: #key is value
            printListReversely(key, depth + 1)
    else:
        print("ЕГГОГ! Этава! Не можед! Быд!")
        print("type of input_: ", type(input_))

os.system("cls")
os.system("echo started >> yeah.txt")
while True:
    os.system("echo " + str(cnt) + " >> log_vk.log")
    postForCntEnd = api.wall.get(domain='egigokasprint', count=postCount, offset=cntuse)
    cntend = postForCntEnd['count']
    cntuse = cntend - cnt
    print()
    print()
    print()
    print("тест ", cnt, "output =", cnt, "cntend =", cntend, "cntuse =", cntuse)
    print()
    time.sleep(timeSleep)
    postCurrent = api.wall.get(domain=group, count=postCount, offset=cntuse) #  домен - короткое имя группы в адрессной строке
    print(",,,,,,,,,,,,,,,,,,,,,,,,")
    printReversely(postCurrent)
    if cnt == postForCntEnd['count']:
        os.system("echo 'yeah' >> yeah.txt")
    cnt += postCount

    if cnt >= postCurrent ["count"]:
        print("Ошибка! Пустой пост №" + str(postCurrent['count']) + r"!")
        break











































# Вывод изображения!!!! (просто тестового)
from PIL import Image, ImageTk
import tkinter as tk

# init gui
btnWidth = 100
btnHeight = 24
btnGap = 10

root = tk.Tk()

img = Image.open(r"D:\Облака\Box Sync\!Work\!StackOverflow\Без имени-1.jpg")

winWidth = img.width - 2; winWidthMin = btnWidth*3 + btnGap*4 - 2 # window size
if (winWidth < winWidthMin):
    winWidth = winWidthMin
winHeight = img.height+btnGap*2+btnHeight-2

canvas = tk.Canvas(root, width=winWidth, height=winHeight)##
#print(img.width)
#print(img.height)
canvas.pack()
tk_img = ImageTk.PhotoImage(img)
canvas.create_image(img.width/2, img.height/2, image=tk_img) ##

def closeWindow(ev):
    global root
    root.destroy()

def editPic(ev):
    img.show() # открывает BMP в Photoshop.
    print("Доделай это нормально!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

def savePic(ev):
    global root
    root.destroy()
    print("Доделай грёбаный код!")

exitBtn = tk.Button(root, text = 'Закрыть')
editBtn = tk.Button(root, text = 'Редактировать')
saveBtn = tk.Button(root, text = 'Сохранить')

exitBtn.bind("<Button-1>", closeWindow)
editBtn.bind("<Button-1>", editPic)
saveBtn.bind("<Button-1>", savePic)

exitBtn.place(x = btnGap, y = img.height + btnGap, width = btnWidth, height = btnHeight)
editBtn.place(x = btnGap*2 + btnWidth, y = img.height + btnGap, width = btnWidth, height = btnHeight)
saveBtn.place(x = btnGap*3 + btnWidth*2, y = img.height + btnGap, width = btnWidth, height = btnHeight)



#root.mainloop() # todo включить обратно

#from tkinter import * # другой вариант вывода изображения
#
#windowMain = Tk()
#windowMain.geometry('600x600+50+50')
#im = r'D:\1.png'
#ph_im = PhotoImage(file=im)
#canv111 = Canvas(windowMain, width=500, height=300)
#canv111.create_image(1, 1, anchor=NW, image=ph_im)
#canv111.place(x=10, y=10)
#windowMain.mainloop()