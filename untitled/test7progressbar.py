#! python3
import time
import os
def playWav(wavName):
    if wavName[1:2] == ":":
        ###todo filenamecnt=wavName[3:]
        cnt=0
        for i in wavName:
            if i == "\\":
                filenamecnt=wavName[cnt+1:]
            cnt += 1

    else:
        filenamecnt=wavName

    filesavename = "test6tasklist.py."+filenamecnt+".vbs"
    file = open(filesavename, 'w')
    file.write('Set oVoice = CreateObject("SAPI.SpVoice")' + '\r')
    file.write('set oSpFileStream = CreateObject("SAPI.SpFileStream")' + '\r')
    file.write('oSpFileStream.Open "' + wavName + '"' + '\r')
    file.write('oVoice.SpeakStream oSpFileStream' + '\r')
    file.write('oSpFileStream.Close')
    file.close()
    os.system(filesavename)


def taskCountdown(task,countdownmin):
    os.system("cls")
    print("Press Enter to start task", task, end='')
    pause=input()
    countdown=countdownmin*60
    os.system('cls')
    print(countdown, "seconds left in task", task)
    global symcnt
    symcnt=102
    for i in range(0,symcnt):
        print(".", end="")
    print()
    for i in range(1,countdown):
        time.sleep(1)
        xi=countdown-i
        os.system('cls')
        print(xi, "seconds left in task", task)
        left=xi/(countdown/symcnt)
        left=int(left)
        gone=symcnt-left
        for i in range(0,gone):
            print('@',end="")
        for i in range(0,left):
            print('.',end='')
        print()
    print("Task", task, "ended.")
    playWav("c:\Windows\Media\Tada.wav")
    os.system('cls')

def load():
    taskCountdown("mom", 15)
    taskCountdown("tel", 5)
    taskCountdown("Python", 25)
    taskCountdown("entertaiment", 5)

def setTask():
    print("Введите задание:", end='')
    global task
    task=input()
    if task == "load":
        load()
    setCountdown()

def setCountdown():
    global task
    global countdown
    try:
        print("Введите время (мин):", end='')
        countdown=input()
        countdown=int(countdown)
        taskCountdown(task, countdown)
    except ValueError as err:
        print("Не похоже на число, старайся лучше.")
        setCountdown()
    task=""
    countdown=""

fullisinputed=False;
while True:
    try:
        ## setTask()
        #if fullisinputed==False:
        #    print("Всего -", end="")
        #    full = input()
        #    fullisinputed = True
        full=45#todo hardcode must deleted
        try:
            full
        except NameError:
            print("Всего -", end="")
            full = input()
        print("Сделано - ", end="")
        doned = input()
        try:
            full=int(full)
            doned=int(doned)
        except ValueError as err:
            print(err)
            #break
        symcnt=80
        gonePercent=(100/full)*doned
        gonePrint= (symcnt / full)*doned
        try:
            gonePrint=int(gonePrint)
            gonePercent=int(gonePercent)
        except ValueError as err:
            print(err)

        #gone=symcnt-left
        left=symcnt - gonePrint
        for i in range(0, gonePrint):
            print('@',end="")
        for i in range(0,left):
            print('.',end='')
        print("Итого сделано",gonePercent,"%")
    except:
        print("Fuck")
        break
