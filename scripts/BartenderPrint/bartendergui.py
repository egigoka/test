#! python3
# -*- coding: utf-8 -*-


from tkinter import *
# mine commands
import sys
sys.path.append("../..")
sys.path.append("..\..")
sys.path.append(".")
from commands7 import *

basicLogicScript = Path.extend("T:", "scripts", "bartenderprint", "bartendernogui.py")
class Debug:
    enable_one_bar = True
    latex_broken = True
    
class State:
    loaders = False
    xelatex = False

# todo база грузчиков
# todo несколько потоков программы
# todo доделать гуи для всех вариантов



def open_legacy(event):
    Process.start("py", basicLogicScript, new_window=True)


def open_log(event):
    Process.start("pyw", basicLogicScript, "ol", new_window=True)


def runLogicScript(*arguments):
    Process.start("py", basicLogicScript, *arguments)


def open_bartender(event):
    bartender = Path.extend("C:", "Program Files (x86)", "Seagull", "Bartender Suite", "bartend.exe")
    Process.start(bartender, new_window=True)

def printBars(event):
    if v.get() == "":
        pass
    else:
        if Debug.latex_broken:
            runLogicScript(v.get(), count.get())
        else:
            if State.xelatex:
                runLogicScript(v.get(), count.get(), "--print-from-gui", "-xelatex")
            else:
                runLogicScript(v.get(), count.get(), "--print-from-gui")
        v.set("")


def print_bars_multitext(event = None):
    Process.start("pyw", basicLogicScript, "mt", new_window=True)


def print_bars_loaders(login, name, count, event=None):
    Process.start("py", basicLogicScript, "g", login, name, count, new_window=True)
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


def doNothing():
    pass

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
if Debug.enable_one_bar:
    counts += [1]

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
    if not State.loaders:
        State.loaders = True
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