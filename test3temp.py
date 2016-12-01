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
        filesavename="test3temp.py."+filename+".txt"
        file = open(filesavename, 'w')
        for task in list1:
            file.write(task + '\r')
        file.close()
    else: # создание бэкапа
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

listOfPrice = []
while True:
    while True:
        printlist(listOfPrice)
        printNoBr("Введите цену:")
        price=input()
        if price:
            try:
                price=int(price)
                listOfPrice.append(price)
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
    cnt=0
    pricemin=-1999
    while cnt<=19:
        counter=0
        pricemin += 2000
        pricemax=pricemin+1999
        print("pricemin = ", pricemin, "and pricemax =", pricemax)
        for price in listOfPrice:
            if price >= pricemin and price <= pricemax:
                printNoBr("*")
                counter += 1
        print()
        print("Count of S4 in this price = ", counter)
        print()
        cnt += 1
    printlist(listOfPrice)
    print()
    print("That's all!")
    break