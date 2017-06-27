import os
import utils
import ntpath

logfile = r"\\192.168.99.91\shares\scripts\bartenderprint\testlog.log"
utils.createfile(logfile)
bakfolder = r"\\192.168.99.91\shares\scripts\bartenderprint"

# print(os.path.getctime(logfile))

# utils.plog(logfile, "воссоздание лога")


# получить список файлов
files_ = os.listdir(bakfolder)
#print(files)
# # выделить среди них нужные ямлы\
files_ = filter(lambda x: x.endswith('.bak'), files_)
files_ = filter(lambda x: x.startswith('settings.json'), files_)

files = []
for file in files_:
    files += [file]
files += ["settings.json"]
#for file in files:
    #print(file)

cnt = 0
# main
for file in files:
    #print(file)
    file = utils.pathInWindowsExtend(r"\\192.168.99.91\shares\scripts\BartenderPrint", file)
# получить время создания
# #os.path.getctime(path) - время создания файла (Windows), время последнего изменения файла (Unix).
    #print(os.path.getctime(file))
    #проверка на правильную сортировку по времени
    try:
        # print(previoustime)
        currenttime = os.path.getmtime(file)
        # print(currenttime)
        #print(previoustime < currenttime)
        if previoustime > currenttime:
            print("Error!")
            sys.exit()
        previoustime = os.path.getmtime(file)
    except:
        previoustime = os.path.getmtime(file)

# отсортировать - не нужно
# сделать дифф
    try:
        previousjson
        currentjson = utils.loadjson(file, quiet = True)
        currentcustomtime = ntpath.getmtime(file)
        #print(currentcustomtime)
        #print(currentjson["group1"]["lastnum"] > previousjson["group1"]["lastnum"])
        if currentjson["group1"]["lastnum"] > previousjson["group1"]["lastnum"]:
            utils.plog(logfile,
                       "напечатано " + str(currentjson["group1"]["lastnum"] - previousjson["group1"]["lastnum"])
                       + " бирок для первой группы", currentcustomtime)
        if currentjson["group2"]["lastnum"] > previousjson["group2"]["lastnum"]:
            utils.plog(logfile,
                       "напечатано " + str(currentjson["group2"]["lastnum"] - previousjson["group2"]["lastnum"])
                       + " бирок для второй группы", currentcustomtime)
        if currentjson["group3"]["lastnum"] > previousjson["group3"]["lastnum"]:
            utils.plog(logfile,
                       "напечатано " + str(currentjson["group3"]["lastnum"] - previousjson["group3"]["lastnum"])
                       + " бирок для третьей группы", currentcustomtime)
        if currentjson["group4"]["lastnum"] > previousjson["group4"]["lastnum"]:
            utils.plog(logfile,
                       "напечатано " + str(currentjson["group4"]["lastnum"] - previousjson["group4"]["lastnum"])
                       + " бирок для четвёртой группы", currentcustomtime)
        if currentjson["group5"]["lastnum"] > previousjson["group5"]["lastnum"]:
            utils.plog(logfile,
                       "напечатано " + str(currentjson["group5"]["lastnum"] - previousjson["group5"]["lastnum"])
                       + " бирок для пятой группы", currentcustomtime)
        if currentjson["group10"]["lastnum"] > previousjson["group10"]["lastnum"]:
            utils.plog(logfile,
                       "напечатано " + str(currentjson["group10"]["lastnum"] - previousjson["group10"]["lastnum"])
                       + " бирок для десятой группы", currentcustomtime)
        if currentjson["group_forp"]["lastnum"] > previousjson["group_forp"]["lastnum"]:
            utils.plog(logfile,
                       "напечатано " + str(currentjson["group_forp"]["lastnum"] - previousjson["group_forp"]["lastnum"])
                       + " бирок для форпоста", currentcustomtime)
        if currentjson["group_alco"]["lastnum"] > previousjson["group_alco"]["lastnum"]:
            utils.plog(logfile,
                       "напечатано " + str(currentjson["group_alco"]["lastnum"] - previousjson["group_alco"]["lastnum"])
                       + " бирок для алкогольной группы", currentcustomtime)
        if currentjson["shipments"]["lastnum"] > previousjson["shipments"]["lastnum"]:
            utils.plog(logfile,
                       "напечатано " + str(currentjson["shipments"]["lastnum"] - previousjson["shipments"]["lastnum"])
                       + " бирок для приёмки", currentcustomtime)
        previousjson = utils.loadjson(file, quiet=True)
    except:
        previousjson = utils.loadjson(file, quiet=True)
# привести время к одному формату - сделано
# привести дифф к одному формату - сделано
