#! python3
# Вывод изображения!!!! (просто тестового)
from PIL import Image, ImageTk
import tkinter as tk

# init
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

def editPhoto(ev):
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
editBtn.bind("<Button-1>", editPhoto)
saveBtn.bind("<Button-1>", savePic)

exitBtn.place(x = btnGap, y = img.height + btnGap, width = btnWidth, height = btnHeight)
editBtn.place(x = btnGap*2 + btnWidth, y = img.height + btnGap, width = btnWidth, height = btnHeight)
saveBtn.place(x = btnGap*3 + btnWidth*2, y = img.height + btnGap, width = btnWidth, height = btnHeight)



root.mainloop()