#! python3
# -*- coding: utf-8 -*-

from utils import *

notepadExecName = "notepad++.exe"
notepadFolder = r"C:\Program Files (x86)\Notepad++"
notepadExec = path_extend(notepadFolder, notepadExecName)

log_file_1 = path_extend(r"\\192.168.99.91", "shares", "scripts",
                                 "bartenderprint", "bartender.log")
log_file_2 = path_extend(r"\\192.168.99.91", "shares", "scripts",
                                 "bartenderprint", "bartender.log_new")

openInNewWindow(notepadExec, log_file_1)
openInCurrentWindow(notepadExec, log_file_2)


start_cnt_bars = 58500

start_line = 119

log_1 = open(log_file_1, "r")
log_2 = open(log_file_2, "w")
cnt_line = 0
new_cnt_bars = start_cnt_bars
for line in log_1:
    cnt_line += 1
    if cnt_line >= start_line:
        #print(getIntegers(line))
        new_cnt_bars = new_cnt_bars - getIntegers(line)[6]
        renewed_line = line.rstrip(newline) + r" /" + str(new_cnt_bars) + newline
        print("renewed_line =" + str(renewed_line), end = "")
        log_2.write(renewed_line)



