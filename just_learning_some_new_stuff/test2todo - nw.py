#! python3
list1 = []  # создание пустого списка

# list.append() - добавление в список
# list.insert(a,0) - добавление в определённое место списка
# list.remove(0) - удаление из списка
# list.pop(1) - удаление из списка
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


# def addtasktolist():
#     while True:
#         print()
#         print("Введите новую задачу (или нажмите Enter для завершения):")
#         tolist = input()
#         if tolist:
#             list1.append(tolist)
#             print("Задача добавлена")
#             sortlist()
#             printlist()
#         else:
#             break
#     print()
#     savefile("save")


def addtasktolist2(tolist):
    while True:
        #print()
        #print("Введите новую задачу (или нажмите Enter для завершения):")
        #tolist = input()
        #print()
        #if tolist:
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
                else:
                    body(priority)
            list1.append(tolist)
            print()
            print("Задача добавлена")
            sortlist()
            print()
            printlist()
            body(input())
        #else:
        #    break
    savefile("save")

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
            file.write(task + '\r')
        file.close()
    else:
        try:
            filesavename="test2todo.py."+filename+".txt"
            file = open(filesavename, 'x')
            for task in list1:
                file.write(task + '\r')
            file.close()
        except FileExistsError:
            global cntbackup
            try:
                cntbackup
            except NameError:
                cntbackup = 0
            cntbackup += 1
            cntbackup=str(cntbackup)
            filename=filename+cntbackup
            cntbackup=int(cntbackup)
            savefile(filename)


def clnscr():
    print()
    print("You really wanna clean zis sheet?")
    cnt=input()
    if cnt == "yes" or "y" or "да" or "д":
        savefile("backup")
        global list1
        list1 = []
        print()
        savefile("save")
        printlist()


# print(add("abc","def"))
# test()

# создание файла
try:
    file = open('test2todo.py.save.txt', 'x')
    file.close()
except FileExistsError:
    print("Файл успешно загружен. Все ваши задачи на месте, надеюсь.")
# чтение файла
file = open('test2todo.py.save.txt')
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
def body(inputed):
    while True:
        #break
        # print("Введите новую задачу или команду:")
        # print("(с)делано, (з)акрыть:")
        print()
        print("Введите новую задачу или команду: (d)one, (s)top")
        if inputed == "stop" or inputed == "s" or inputed == "закрыть" or inputed == "з":
            break
        #elif inputed == "add" or inputed == "a" or inputed == "добавить" or inputed == "д":
        #    addtasktolist2()
        #if inputed == "print" or inputed == "p" or inputed == "вывести" or inputed == "в":
        #    printlist()
        elif inputed == "finished" or inputed == "d" or inputed == "сделано" or inputed == "с":
            deltask()
        elif inputed == "clean zis sheet":
            if list1:
                clnscr()
        else:
            addtasktolist2(inputed)
            # print("Команды: add, finished, print, stop")
        inputed=input()

body("1")

