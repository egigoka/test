#! python3
list1 = []  # создание пустого списка

#prioritystate = 0
#issettingpriority = 0

# list_.append() - добавление в список
# list_.insert(a,0) - добавление в определённое место списка
# list_.remove(0) - удаление из списка
# list_.pop(1) - удаление из списка
# def add(x, y):
#    return x+y
# def test():
#    print("Hello, world!")

def printlist():
    if list1:
        print("Ваш список задач:")
        cnt=0
        for task in list1:
            cnt=cnt+1  # для счёта с 1, а не с 0, ну и чтобы отличалось видом не "cnt += 1"
            if cnt<10 and len(list1)>10:
                print("  0", cnt, " > ", task, sep='') # ещё можно использовать end=''
            else:
                print(" ", cnt, ">", task)
            cnt=cnt-1  # для счёта с 1, а не с 0
            cnt += 1
        cnt=0
    else:
        print("Ваш список задач пуст.")


def sortlist():
    list1.sort()

def addtasktolist(tolist):
    print()
    print("Введите важность задачи, если обычная, то Enter")
    print("1 - первоочередная, 2 - важная, 0 - совсем не важная > ", end='')
    priority=input()
    if priority:
        if priority=="1":
            tolist="! "+tolist
        elif priority=="2":
            tolist="@ "+tolist
        elif priority=="0":
            tolist="z "+tolist
        #todo сделать так, чтобы работали другие команды во время назначения
        #приоритета делу
    list1.append(tolist)
    print()
    print("Задача добавлена")
    sortlist()
    print()
    printlist()
    savefile("save")

def addtasktolist_v3():
    print()

def deltask():
    print()
    printlist()
    print("Введите номер задачи для удаления:")
    try:
        todel = input()
        todel = int(todel)
        todel -= 1 # исправление проблем, связанных со счётом массива с 1, а не с 0
        list1.pop(todel)
    except ValueError as err:
        #print(err)
        print("Это даже на номер не похоже")
    except IndexError as err:
        #print(err)
        print("Такого номера задачи нет")
    print()
    savefile("save")
    printlist()

def savefile(filename):
    if filename=="save":
        filesavename="test2todo.py."+filename+".txt"
        file = open(filesavename, 'w')
        for task in list1:
            file.write(task + '\n')
        file.close()
    else:
        try:
            global cntbakup
            filenamecnt=filename
            try:
                cntbakup
            except NameError:
                cntbakup = 1
            cntbakupstr = str(cntbakup)
            filenamecnt += cntbakupstr
            filesavename = "test2todo.py."+filenamecnt+".txt"
            file = open(filesavename, 'x')
            for task in list1:
                file.write(task + '\r')
            file.close()
        except FileExistsError:
            cntbakup += 1
            savefile(filename)

def clnscr():
    print()
    print("You really wanna clean zis sheet?(y/д)")
    cnt=input()
    if cnt == "yes" or cnt == "y" or cnt == "да" or cnt == "д":
        savefile("backup")
        global list1
        list1 = []
        print()
        savefile("save")
    list1.append("testdel")
    printlist()

def loadfile():
    file = open('test2todo.py.save.txt')
    for line in file:
        cnt=0
        cnt=len(line)-1
        line=line[0:cnt]
        list1.append(line)
        cnt=0
    file.close()
    sortlist()
    printlist() # проверка правильности чтения


# print(add("abc","def"))
# test()

# создание файла
try:
    file = open('test2todo.py.save.txt', 'x')
    file.close()
except FileExistsError:
    print("Файл успешно загружен. Все ваши задачи на месте, надеюсь.")

loadfile()

while True:
    #break
    # print("Введите новую задачу или команду:")
    # print("(с)делано, (з)акрыть:")
    print()
    print("Введите нов. задачу или команду: (c)ompleted, (s)top, /save(sv), (l)oad/")
    inputed = input()
    if inputed == "stop" or inputed == "s" or inputed == "закрыть" or inputed == "з" or inputed == "ы":
        break
    #elif inputed == "add" or inputed == "a" or inputed == "добавить" or inputed == "д":
    #    addtasktolist()
    #if inputed == "print" or inputed == "p" or inputed == "вывести" or inputed == "в":
    #    printlist()
    elif inputed == "completed" or inputed == "c" or inputed == "сделано" or inputed == "с":
        deltask()
#то, что ниже - выбросить
    elif inputed == "clean zis sheet" or inputed == "cls":
        if list1:
            clnscr()
    elif inputed == "save" or inputed == "sv" or inputed == "ым":
        filesavename="test2todo.py.goodsave.txt"
        file = open(filesavename, 'w')
        for task in list1:
            file.write(task + '\r')
        file.close()
        print()
        print("Сохранено. Что тут мудрёного?")
    elif inputed == "load" or inputed == "l" or inputed == "д":
        # чтение файла
        if list1:
            clnscr()
        file = open('test2todo.py.goodsave.txt')
        for line in file:
            cnt=0
            cnt=len(line)-1
            line=line[0:cnt]
            list1.append(line)
            cnt=0
        file.close()
        sortlist()
        # чтение файла
        printlist() # проверка правильности чтения
#то, что выше - выбросить
    else:
        addtasktolist(inputed)