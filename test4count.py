#! python3
def inc(x):
    x += 1
    return x
def printNoBr(x):
    print(x, end='', sep='')
def printlist(list1):
    if list1:
        print("Ваш список:")
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
        print("Cписок пуст.")

def savefile(filename):
    if filename=="save":
        filesavename="test4count.py."+filename+".txt"
        file = open(filesavename, 'w')
        for line in listOfPrice:
            line=str(line)
            file.write(line + '\r')
        file.close()
    else: # создание бэкапа
        try:
            filesavename="test4count.py."+filename+".txt"
            file = open(filesavename, 'x')
            for task in listOfPrice:
                file.write(task + '\r')
            file.close()
        except FileExistsError:
            if len(listOfPrice) != 0:
                global cntbackup
                try:
                    cntbackup
                except NameError:
                    cntbackup = 0
                cntbackup += 1
                if cntbackup > 1:
                    cntr=len(filename)-1
                    filename=filename[0:cntr]
                cntbackup=str(cntbackup)
                filename=filename+cntbackup
                cntbackup=int(cntbackup)
                savefile(filename)
def sortlist():
    listOfPrice.sort()
def loadfile():
    try:
        file = open('test4count.py.save.txt')
        for line in file:
            cnt=0
            cnt=len(line)-1
            line=line[0:cnt]
            try:
                line=int(line)
                listOfPrice.append(line)
            except ValueError:
                continue
            cnt=0
        file.close()
        sortlist()
    except FileNotFoundError as err:
        print("Can't load file. Check file. Error:")
        print(err)
    #printlist(listOfPrice) # проверка правильности чтения

##############################################################################
##############################################################################
##############################################################################
listOfPrice = []
savefile("backup")
print("test4conunt ver 1.1.12s5 loaded!")
while True:
    while True:
        printlist(listOfPrice)
        printNoBr("Введите цену (*100):")
        price=input()
        if price == "stop":
            break
        elif price == "load":
            loadfile()
        elif price:
            try:
                price=int(price)
                price *= 100
                listOfPrice.append(price)
                savefile("save")
            except ValueError as err:
                print(err)
                continue
        else:
            printNoBr("End? ")
            end=input()
            if end == "y" or end == "yes" or end == "д" or end == "да":
                break
            else:
                continue
    step=1000
    pricemin=0-step+1
    pricemax=0
    while pricemax<40000:
        counter=0
        pricemin += step
        pricemax=pricemin+step-1
        for price in listOfPrice:
            if price >= pricemin and price <= pricemax:
                counter += 1
        if counter != 0:
            print("pricemin = ", pricemin, "and pricemax =", pricemax)
            printCounter=counter
            while counter !=0:
                printNoBr("*")
                counter -= 1
            print()
            print("Count of S3 in this price = ", printCounter)
            print()
    #printlist(listOfPrice)
    print()
    print("That's all!")
    break