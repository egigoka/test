#!python3

# mine commands
import sys
sys.path.append("../..")
sys.path.append("..\..")
sys.path.append(".")
sys.path.append("..")
sys.path.append("./term")
sys.path.append(r".	erm")
from commands8 import *

#Internal.mine_import("vk_requests")
import vk_requests


if OS.name == "winows":
    import win_unicode_console
    win_unicode_console.enable()

import test11vk_test_usuless_login

#print(test11vk_test_usuless_login.varVkUser)
#print(test11vk_test_usuless_login.varVkPass)
Print.rewrite("Try to log in...")
api = vk_requests.create_api(app_id=5569080, login=test11vk_test_usuless_login.varVkUser, password=test11vk_test_usuless_login.varVkPass) # todo включить авторизацию
Print.rewrite("Succesfully logged in, trying create api")
api_status_kim = vk_requests.create_api(app_id=5569080, login=test11vk_test_usuless_login.varVkUser, password=test11vk_test_usuless_login.varVkPass, scope=['offline', 'status'])#, api_version='5.00')
Print.rewrite("Succesfully created api, trying create interactive api")
api_mine_interactive = vk_requests.create_api(interactive=True, scope=['offline', 'status'])
Print.rewrite("Created interactive api??? Trying to set status")
#api = vk_requests.create_api() # создание сессии без логина

api_status_kim.status.set(text='Не Ким!1один')
Print.rewrite("Status set, trying to download posts")

cnt = 7774 # с какого поста начинать отображать
timeSleep = .250 # так как программа однопоточная, то чтобы вк не банил, стоит задержка в 250 мс
whitespace = "   " # отступ


def wprint(depth):
    print(whitespace * depth, end="")

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
            raise TypeError("type must be dict")


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


class Vk:
    last_download = datetime.datetime.now()
    @classmethod
    def download_post(Vk, groupname, post_number, posts_count=1, quiet=False):
        time_started = datetime.datetime.now()
        time_delta = Time.delta(Vk.last_download, time_started)
        print(time_delta)
        if time_delta<timeSleep:
            time.sleep(timeSleep-time_delta)
        post_dict = api.wall.get(domain=groupname, count=posts_count, offset=post_number)
        if not quiet:
            printReversely(post_dict)
        Vk.last_download = datetime.datetime.now()  # last logic line!!!
        return post_dict



while True:
    print()
    print("тест ", cnt)
    print()
    postCurrent = Vk.download_post("egigokasprint", cnt, quiet=False)
    cnt+=1
    cnt_ = 0
    print(",,,,,,,,,,,,,,,,,,,,,,,,")
    if cnt >= postCurrent ["count"]:
        print("Ошибка! Пустой пост №" + str(postCurrent['count']) + r"!")
        break




import tkinter
from PIL import ImageTk, Image

#This creates the main window of an application
window = tkinter.Tk()
window.title("Join")
#window.geometry("300x300")
window.configure(background='grey')

path = Path.extend(Path.home(), "Desktop", "Pictures", "1496861327127533991.jpg")

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tkinter.Label(window, image = img)

#The Pack geometry manager packs widgets in rows or columns.
#panel.pack(side = "bottom", fill = "both", expand = "yes")
panel.grid(row=1, column=1, columnspan=3)


exitBtn = tkinter.Button(window, text = 'Закрыть')
def closeWindow(ev):
    window.destroy()
exitBtn.bind("<Button-1>", closeWindow)
exitBtn.grid(row=2,column=1)

exit2Btn = tkinter.Button(window, text = 'Закрыть2')
def closeWindow2(ev):
    window.destroy()
exit2Btn.bind("<Button-1>", closeWindow2)
exit2Btn.grid(row=2,column=2)

exit3Btn = tkinter.Button(window, text = 'Закрыть3')
def closeWindow3(ev):
    window.destroy()
exit3Btn.bind("<Button-1>", closeWindow3)
exit3Btn.grid(row=2,column=3)


#Start the GUI
window.mainloop()






































"""
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
    GUI.warning("Доделай это нормально!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

def savePic(ev):
    global root
    root.destroy()
    raise NotImplementedError("Доделай грёбаный код!")

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
"""
