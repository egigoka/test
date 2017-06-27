#! python3
import sys, os, win_unicode_console, subprocess
from utils import dir_create, file_create, savejson, loadjson, path_extend

# init
win_unicode_console.enable()
scriptsFolder = r"\\192.168.99.91\shares\scripts"
scriptsSubFolderName = "BartenderPrint"
scriptsSubFolder = scriptsFolder + "\ "[:1] + scriptsSubFolderName # "\\192.168.99.91\shares\scripts\BartenderPrint"
bartenderDocumentsFolder = r"\\192.168.99.91\shares\scripts\BartenderPrint\Bartender Documents"
bartenderMineDockumentsSubFolder = bartenderDocumentsFolder + "\ "[:1] + "Егоров"
bartenderFolder = "C:\Program Files (x86)\Seagull\Bartender Suite"
bartenderExecName = "bartend.exe"
bartenderExec = bartenderFolder + "\ "[:1] + bartenderExecName # "C:\Program Files (x86)\Seagull\Bartender Suite\bartend.exe"
notepadExecName = "notepad++.exe"
notepadFolder = r"C:\Program Files (x86)\Notepad++"
notepadExec = path_extend(notepadFolder, notepadExecName)
settingsJsonName = "settings.json"
settingsJsonFile = scriptsSubFolder + "\ "[:1] + settingsJsonName # "\\192.168.99.91\shares\scripts\BartenderPrint\settings.json"
outputFileName = "Бирки_output.txt"
outputFile = bartenderDocumentsFolder + "\ "[:1] + outputFileName # "C:\Users\Sklad_solvo\Documents\BarTender\BarTender Documents\Бирки_output.txt"
dir_create(scriptsFolder)
dir_create(scriptsSubFolder)
file_create(settingsJsonFile)
jsonStringInMemory = loadjson(settingsJsonFile)
savejson(settingsJsonFile, jsonStringInMemory)

debugprint = False
if debugprint == True:
    print("settingsJsonFile:", end = "")
    print(settingsJsonFile)


def bartenderDocument(name):
    path = str(bartenderDocumentsFolder) + "\ "[:1] + str(name) + ".btw"
    return path


def bartenderMineDocument(name):
    path = str(bartenderMineDockumentsSubFolder) + "\ "[:1] + str(name) + ".btw"
    return path


def bartenderPreload():
    subprocess.call([bartenderExec, "/P"])


def newPrintBars(cntBars, groupName, filesavename = outputFile):
    prefix = jsonStringInMemory[groupName]["prefix"]
    startCnt = jsonStringInMemory[groupName]["lastnum"]
    cnt = startCnt + 1
    file = open(filesavename, 'w')
    endCnt = startCnt + cntBars
    jsonStringInMemory[groupName]["lastnum"] = endCnt
    savejson(settingsJsonFile, jsonStringInMemory)
    while cnt <= endCnt:
        file.write(str(prefix) + str(cnt) + '\n')
        print(str(prefix) + str(cnt))
        cnt += 1
    file.close()


def runBartender(database = outputFile, type = "kompl",size = "58*60"):
    database = None
    if type == "kompl" and size == "58*60":
        bartenderFile = bartenderMineDocument("Бирки 58x60")
        print([bartenderExec, bartenderFile])
        subprocess.call([bartenderExec, bartenderFile, "/P", "/X"])



if __name__ == '__main__':
    bartenderPreload()
    def main():
        #os.system("taskkill /f /im bartend.exe")
        #1stItem = ["1"]
        #2ndItem = ["2"]
        print("Выберите группу:")
        print("[1]      1 группа")
        print("[2]      2 группа")
        print("[3]      3 группа")
        print("[4]      4 группа")
        print("[5]      5 группа")
        print("[6]      Грузы")
        print("[7]      Форпост")
        print("[8]      Алкоголь")
        print("[9]      Текст в штрихкод")
        print("[10]     10 группа")
        print("[e]      Выход")
        print("[d]      Debug")
        inputGroupAndCount = input("Введите номер: ")
        if (inputGroupAndCount[:2] == "10") | (inputGroupAndCount[2:] == "10"):
            groupname = "group10"
        elif (inputGroupAndCount[:1] == "1") | (inputGroupAndCount[1:] == "1"):
            groupname = "group1"
        elif (inputGroupAndCount[:1] == "2") | (inputGroupAndCount[1:] == "2"):
            groupname = "group2"
        elif (inputGroupAndCount[:1] == "3") | (inputGroupAndCount[1:] == "3"):
            groupname = "group3"
        elif (inputGroupAndCount[:1] == "4") | (inputGroupAndCount[1:] == "4"):
            groupname = "group4"
        elif (inputGroupAndCount[:1] == "5") | (inputGroupAndCount[1:] == "5"):
            groupname = "group5"
        elif (inputGroupAndCount[:1] == "6") | (inputGroupAndCount[1:] == "6"):
            groupname = "shipments"
        elif (inputGroupAndCount[:1] == "7") | (inputGroupAndCount[1:] == "7"):
            groupname = "group_forp"
        elif (inputGroupAndCount[:1] == "8") | (inputGroupAndCount[1:] == "8"):
            groupname = "group_alco"
        elif (inputGroupAndCount[:1] == "9") | (inputGroupAndCount[1:] == "9"):
            text = input("Text:")
            file = open(outputFile, 'w')
            file.write(text)
            file.close()
            runBartender()
            main()
        elif ((inputGroupAndCount[:4] == "exit") or (inputGroupAndCount[:4] == "e") or (inputGroupAndCount[:4] == "у") or (inputGroupAndCount[:4] == "е")):
            sys.exit()
        elif (inputGroupAndCount[:1] == "d") | (inputGroupAndCount[1:] == "d"):
            bartenderFile = bartenderMineDocument("Бирки 58x60")
            subprocess.call([bartenderExec, bartenderFile])
            main()
            subprocess.call([notepadExec, settingsJsonFile])
        else:
            print("error")
            print(inputGroupAndCount)
            main()
        try:
            newPrintBars(int(input("Сколько нужно бирок?")), groupname)
            runBartender()
            main()
        except ValueError as err:
            print(err)
            main()
        main()
    while True:
        main()
    # todo open bartender



