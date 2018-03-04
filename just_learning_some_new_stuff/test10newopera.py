#! python3

# init
import os
import time

# vars
# todo сделать выбор браузера
nameFolderTemp = '_Current_Session_'
nameFileCurrentsession = 'Current Session'
pathBrowserAppdata = r'C:\Users\EGiGoka\AppData\Roaming\Opera Software'
nameBrowser = 'Opera Stable'
fileBrowserLauncher = '"C:\Program Files (x86)\Opera\launcher.exe"'
fileBrowserExecuted = 'opera.exe'
pathBrowser = pathBrowserAppdata + "\ "[:-1] + nameBrowser
pathTemp = pathBrowser + "\ "[:-1] + nameFolderTemp
filesTemp = os.listdir(pathTemp)


# функции
# noinspection PyShadowingNames
def pathFileNew():
    fileLast = filesTemp[-1]

    #cnt = input(test = "sadf") todo проверить, что это за говно
    cnt = int(fileLast[-1:]) + 1
    fileNew = fileLast[0:-1] + str(cnt)
    pathFileNew = pathTemp + '\ '[:-1] + fileNew
    return pathFileNew

def sessionRestore():
    # todo доделать восстановление и длину строки ровную
    print("watch todo")
    for file in filesTemp:
        file_timeCreated = str(time.ctime(os.path.getctime(pathTemp + "\ "[:-1] + file)))
        file_size = str(os.path.getsize(pathTemp + "\ "[:-1] + file))
        print(file + " *** " + file_timeCreated + " *** " + file_size)

def sessionClean():
    os.system("taskkill /f /im " + fileBrowserExecuted)
    pathFileCurrent = pathBrowser + "\ "[:-1] + nameFileCurrentsession
    cmd = 'move "' + pathFileCurrent + '" "' + pathFileNew() + '"'
    print(cmd)
    os.system(cmd)
    os.system(fileBrowserLauncher)

def main():
    os.system('cls')
    print('Вас приветствует скрипт управлениями сессиями ' + nameBrowser)
    print('Команды:')
    print('r [номер сессии] - восстановить сессию')
    print('')
    case = input('(n)ew session or (r)estore session? ')
    if case == "n" or case == "N" or case == "т" or case == "Т":
        sessionClean()
    elif case == "r" or case == "R" or case == "к" or case == "К":
        sessionRestore()
    else:
        main()

#старт
main()
