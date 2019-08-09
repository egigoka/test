import pyautogui
from commands import *

__version__ = "0.0.2"

servers = ['eggg-2012', 'eggg-2012-na2', 'eggg-2019-na3', 'eggg-2008na4',
           'eggg-dc1', 'spb-qc203v']


def main():
    Time.sleep(5)
    pyautogui.typewrite(f't 20' + newline)
    for s in servers:
        pyautogui.typewrite(f'ping {s}' + newline)
        Time.sleep(0.1)
    pyautogui.typewrite("ipconfig"+newline)
    Time.sleep(0.1)


if __name__ == "__main__":
    main()
