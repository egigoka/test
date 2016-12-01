#! python3
import sys, os, win_unicode_console
from utils import createdirs, createfile, savejson, loadjson

# init
win_unicode_console.enable()
scriptsFolder = "C:\scripts"
scriptsSubFolderName = "BarTenderPrint"
scriptsSubFolder = scriptsFolder + "\ "[:1] + scriptsSubFolderName # "C:\scripts\BarTenderPrint"
bartenderFolder = "C:\Program Files (x86)\Seagull\Bartender Suite"
bartenderExecName = "bartend.exe"
bartenderExec = bartenderFolder + "\ "[:1] + bartenderExecName # "C:\Program Files (x86)\Seagull\Bartender Suite\bartend.exe"
settingsJsonName = "settings.json"
settingsJsonFile = scriptsSubFolder + "\ "[:1] + settingsJsonName # "C:\scripts\BarTenderPrint\settings.json"
outputFileName = "output.txt"
outputFile = scriptsSubFolder + "\ "[:1] + outputFileName # "C:\scripts\BarTenderPrint\output.txt"
createdirs(scriptsFolder)
createdirs(scriptsSubFolder)
createfile(settingsJsonFile)
jsonStringInMemory = loadjson(settingsJsonFile)
savejson(settingsJsonFile, jsonStringInMemory)

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


def runBarTender(database, type = "kompl",size = "58*60"):
    if type == "kompl" and size == "58*60":
        bartenderFile = "Бирки 58x60.btw"
    os.system()



if __name__ == '__main__':
    def main():
        inputGroupAndCount = input("Введите номер группы (1,2,3,4,5) или 'exit' для выхода: ")
        if (inputGroupAndCount[:2] == "10") | (inputGroupAndCount[2:] == "10"):
            groupname = "group10"
        elif (inputGroupAndCount[:1] == "1") | (inputGroupAndCount[1:] == "1"):
            groupname = "group2"
        elif (inputGroupAndCount[:1] == "1") | (inputGroupAndCount[1:] == "1"):
            groupname = "group1"
        elif (inputGroupAndCount[:1] == "1") | (inputGroupAndCount[1:] == "1"):
            groupname = "group1"
        elif (inputGroupAndCount[:1] == "1") | (inputGroupAndCount[1:] == "1"):
            groupname = "group1"

        elif ((inputGroupAndCount[:4] == "exit") or (inputGroupAndCount[:4] == "e") or (inputGroupAndCount[:4] == "у")):
            sys.exit()
        else:
            print("error")
            print(inputGroupAndCount)
            main()
        try:
            cntBars = int(input("Сколько нужно бирок?"))
        except ValueError as err:
            print(err)
            main()
        newPrintBars(cntBars, groupname)
        runBartender()

    while True:
        main()
    # todo func generate nums
    # todo open bartender

    os.system("taskkill /f /im bartend.exe")

