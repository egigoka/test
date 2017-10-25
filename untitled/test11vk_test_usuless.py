#!python3

import vk_requests
import time
import sys

# mine commands
import sys
sys.path.append("../..")
sys.path.append("..\..")
sys.path.append(".")
sys.path.append("..")
sys.path.append("./term")
sys.path.append(r".	erm")
from commands7 import *

if OS.name == "winows":
    import win_unicode_console
    win_unicode_console.enable()

import test11vk_test_usuless_login

#print(test11vk_test_usuless_login.varVkUser)
#print(test11vk_test_usuless_login.varVkPass)

api = vk_requests.create_api(app_id=5569080, login=test11vk_test_usuless_login.varVkUser, password=test11vk_test_usuless_login.varVkPass) # todo включить авторизацию
api_status_kim = vk_requests.create_api(app_id=5569080, login=test11vk_test_usuless_login.varVkUser, password=test11vk_test_usuless_login.varVkPass, scope=['offline', 'status'])#, api_version='5.00')
api_mine_interactive = vk_requests.create_api(interactive=True, scope=['offline', 'status'])
#api = vk_requests.create_api() # создание сессии без логина

api_status_kim.status.set(text='Не Ким!1один')
#print(api.users.get(user_ids=1))
#print()
#print(api.users.get(user_ids=49920173))
#print()
cnt = 7400 # с какого поста начинать отображать
timeSleep = .250 # так как программа однопоточная, то чтобы вк не банил, стоит задержка в 250 мс
whitespace = "   " # отступ
postCount = 1 # количество постов за раз скачивать

def wprint(depth):
    print(whitespace * depth, end="")

#def valuePrintCmd(key, value = None, depth = 0):
#    if (key == "photo") & (value is None):
#        wprint(depth)
#        print("!!!STARTED PHOTO!!!")
#    elif key[0:5] == "photo":
#        wprint(depth)
#        print("!!!PHOTO!!!")
#    elif (key == "count") & (depth == 0):
#        wprint(depth)
#        print("Количество записей в группе:", value)
#    elif key == "items":
#        wprint(depth)
#        print("Начало поста:")
#    elif key == "comments":
#        wprint(depth)
#        print("Комментарии:",)
#    elif (key == "count") & (depth == 2):
#        wprint(depth)
#        print("Количество комментариев:", value)
#    elif (key == "copy_history"):
#        wprint(depth)
#        print("История репостов:", value)
#    else:
#        print(whitespace * depth, end="")
#        print("Key '", key, "' is not supported. Script is ending")
#        sys.exit()

def printListReversely(input_, depth=0):
    for value in input_:
        if isinstance(value, list):
            for value_ in value:
                print(whitespace * depth + (value_))  # Напечатать только ключ, так как значение это большой (не факт) лист (факт)
                #valuePrintCmd(value_, depth=depth + 1)
                printReversely(value, depth + 1)
        elif isinstance(value, dict):
            printReversely(value, depth)
        else:
            print("ЕГГОГ! Этава! Не можед! Быд!")
            print("type of input_: ", type(input_))


def printReversely(input_, depth=0):
    if isinstance(input_, dict):
        for key, value in sorted(input_.items(), key=lambda x: x[0]):
            if isinstance(value, dict):
                print (whitespace*depth + (key)) # Напечатать только ключ, так как значение это большой (не факт) словарь (факт)
                #valuePrintCmd(key, depth = depth)
                printReversely(value, depth + 1)
            elif isinstance(value, list):
                #valuePrintCmd(key, depth = depth+1)
                printListReversely(value, depth + 1) #обход листа
            else:
                print (whitespace*depth + "%s %s" % (key, value)) # Напечатать и ключ, и значение, так как это просто значение
                #valuePrintCmd(key, value, depth)
    elif isinstance(input_, list):
        for key in input_: #key is value
            printListReversely(key, depth + 1)
    else:
        print("ЕГГОГ! Этава! Не можед! Быд!")
        print("type of input_: ", type(input_))



while True:
    sys.exit()
    print()
    print("тест ", cnt)
    print()
    time.sleep(timeSleep)
    postCurrent = api.wall.get(domain='egigokasprint', count=postCount, offset=cnt) #  домен - короткое имя группы в адрессной строке
    #print(postCurrent_str)
    ############################
    cnt_ = 0
    print(",,,,,,,,,,,,,,,,,,,,,,,,")
    #print(str(postCurrent))
    printReversely(postCurrent)
    cnt += postCount
    #printReversely(postCurrent["items"])
    #print(type(postCurrent["items"]))
    #print(type(postCurrent["items"][0]))


    #for i in postCurrent['items']:
    #    cnt_ += 1
    #    print(cnt_)
    #    #print(i)
    #    #print(type(i))
    #    #print(dict.items(i))
    #    print(i.get('copy_history'))
    #    for j in i:
    #        #print(j)
    #
    #        if j == "":
    #            print("Найдено! Найдено!")
    #print("''''''''''''''''''''''''")
    #######################
    # todo доделать парсер
    # todo найти последний пост
    #if cnt == 3:
    #    break
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
    warning("Доделай это нормально!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

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
