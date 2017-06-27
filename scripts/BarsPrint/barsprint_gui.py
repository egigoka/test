#! python3
# -*- coding: utf-8 -*-

# old version, new in share

from tkinter import *
from utils import *

isDebug = False
basicLogicScript = path_extend(backslash, "192.168.99.91", "shares", "scripts",
                                       "bartenderprint", "bartendernogui.py")


# todo база грузчиков
# todo несколько потоков программы
# todo доделать гуи для всех вариантов

# def варианты запуска основного скрипта
#     openInNewWindow(basicLogicScript, v.get(), count.get()) работает в несколько потоков, но пока потоки не нужны
#     openInCurrentWindow(basicLogicScript, v.get(), count.get()) # работает
#     os.system(basicLogicScript + " " + str(v.get()) + " " + str(count.get())) # работает в один поток
#     subprocess.call(["py", basicLogicScript, str(v.get()), str(count.get())]) # работает


def open_legacy(event):
    openInNewWindow("py", basicLogicScript)


def open_log(event):
    openInNewWindow("pyw", basicLogicScript, "ol")


def runLogicScript(*arguments):
    openInCurrentWindow(*arguments, commands=["py", basicLogicScript])

def open_bartender(event):
    bartenderFolder = "C:\Program Files (x86)\Seagull\Bartender Suite"
    bartenderExecName = "bartend.exe"
    bartenderExec = bartenderFolder + "\ "[:1] + bartenderExecName
    subprocess.call(bartenderExec)

def printBars(event):
    if v.get() == "":
        pass
    else:
        runLogicScript(v.get(), count.get())
        v.set("")



def print_bars_multitext(event = None):
    openInNewWindow("pyw", basicLogicScript, "mt")

def print_bars_loaders(login, name, count, event=None):
    openInNewWindow("py", basicLogicScript, "g", login, name, count)
    loaders_var_login.set("")
    loaders_var_name.set("")


root = Tk()

v = StringVar()
count = IntVar()
count.set(1500)
# string = StringVar()
row = 0


groups = \
    [
    ("Первая",1),
    ("Вторая",2),
    ("Третья",3),
    ("Четвёртая",4),
    ("Пятая",5),
    ("Десятая",10),
    ("Алкоголь",8),
    ("Фрукты",9),
    ("Форпост",7),
    ("Грузы",6),
    ]


for group, value in groups:
    row += 1
    Radiobutton(root, text=group, variable=v, command=doNothing, value=value).grid(row=row, column=0, sticky=W)

# row += 1
# radioBtn_1 = Radiobutton(root, text="1 бирка :D", variable=count, value=1).grid(row=row, column = 0)
# row += 1
# radioBtn_1500 = Radiobutton(root, text="1500 бирок", variable=count, value=1500).grid(row=row, column = 0)
# row += 1
# radioBtn_3000 = Radiobutton(root, text="3000 бирок", variable=count, value=3000).grid(row=row, column = 0)
# row += 1
# radioBtn_4000 = Radiobutton(root, text="4000 бирок", variable=count, value=4000).grid(row=row, column = 0)
# row += 1
# radioBtn_5000 = Radiobutton(root, text="5000 бирок", variable=count, value=5000).grid(row=row, column = 0)
# row += 1
# radioBtn_15000 = Radiobutton(root, text="15000 бирок", variable=count, value=15000).grid(row=row, column = 0)

counts = [1500, 3000, 4000, 5000, 15000]
if isDebug:
    count += [1]

row_count = 0
for count_ in counts:
    row_count += 1
    Radiobutton(root, text=str(count_) + " бирок", variable=count, command=doNothing, value=count_).grid(row=row_count, column=1, sticky=W)

row += 1
### Старый вариант
# btn = Button(root)
# btn["text"] = "Печать"
# btn.bind("<Button-1>", printBars)
# btn.grid(row=row, column = 0)
# row += 1
btn_Print = Button(root, text = "Печать")
btn_Print.bind("<Button-1>", printBars)
btn_Print.grid(row=row, column = 0, sticky=W+E, columnspan = 2)
row += 1
btn_OpenLegacy = Button(root, text = "Открыть консольную версию")
btn_OpenLegacy.bind("<Button-1>", open_legacy)
btn_OpenLegacy.grid(row=row, column = 0, sticky=W+E, columnspan = 2)
row += 1
btn_OpenLog = Button(root, text = "Открыть лог")
btn_OpenLog.bind("<Button-1>", open_log)
btn_OpenLog.grid(row=row, column = 0, sticky=W+E, columnspan = 2)
row += 1
btn_OpenLog = Button(root, text = "Несколько бирок")
btn_OpenLog.bind("<Button-1>", print_bars_multitext)
btn_OpenLog.grid(row=row, column = 0, sticky=W+E, columnspan = 2)
row += 1
btn_OpenBartender = Button(root, text = "Открыть GUI Bartender")
btn_OpenBartender.bind("<Button-1>", open_bartender)
btn_OpenBartender.grid(row=row, column = 0, sticky=W+E, columnspan = 2)


def add_loaders(event=None):
    global row
    row += 1
    loaders_label_login = Label(root, text='Логин:')
    loaders_label_login.grid(row=row, column=0,  rowspan=2)#, sticky=E)
    row += 1
    loaders_var_login = StringVar()
    loaders_var_login.set("")
    loaders_entry_login = Entry(root, textvariable=loaders_var_login)
    loaders_entry_login.grid(row=row, column=1, sticky=W+E+S+N, columnspan=1)

    row += 1
    loaders_label_name = Label(root, text='Имя и фамилия:')
    loaders_label_name.grid(row=row, column=0, rowspan=2)  # , sticky=E)
    row += 1
    loaders_var_name = StringVar()
    loaders_var_name.set("")
    loaders_entry_name = Entry(root, textvariable=loaders_var_name)
    loaders_entry_name.grid(row=row, column=1, sticky=W + E + S + N, columnspan=1)

    row += 1
    loaders_label_count = Label(root, text='Количество:')
    loaders_label_count.grid(row=row, column=0, rowspan=2)  # , sticky=E)
    row += 1
    loaders_var_count = StringVar()
    loaders_var_count.set("10")
    loaders_entry_count = Entry(root, textvariable=loaders_var_count)
    loaders_entry_count.grid(row=row, column=1, sticky=W + E + S + N, columnspan=1)

    row += 1
    loaders_print_btn = Button(root, text="Печать")
    loaders_print_btn.bind("<Button-1>", lambda x: print_bars_loaders(loaders_var_login.get(),
                                                                          loaders_var_name.get(),
                                                                          loaders_var_count.get()
                                                                         )
                           )
    loaders_print_btn.grid(row=row, column=0, sticky=W + E, columnspan=2)
row += 1
loaders_btn = Button(root, text = "Грузчики")
loaders_btn.bind("<Button-1>", add_loaders)
loaders_btn.grid(row=row, column = 0, sticky=W+E, columnspan = 2)


root.title("BartenderLoader GUI")
root.iconbitmap(r"C:\Program Files (x86)\Seagull\BarTender Suite\bartend.ico")
mainloop()