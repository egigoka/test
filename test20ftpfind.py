#! python3
import os, time, sys

#init
browserFile = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
browserFile = "chrome.exe"
browserFile = r"C:\Users\Sklad_solvo\AppData\Local\CentBrowser\Application\chrome.exe"
mask = "192.168.99."
cnt = 0

def browserOpen(cnt):
    command = browserFile + ' ftp://' + mask + str(cnt)
    print(command)
    os.system(command)
    time.sleep(2)

if __name__ == '__main__':
    while cnt < 256:
        browserOpen(cnt)
        cnt += 1
    else:
        sys.exit()