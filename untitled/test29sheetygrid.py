#! python3
# -*- coding: utf-8 -*-

from commands7 import *

rows = input_int("rows:")
columns = input_int("columns:")

rows_cnt = rows
while rows_cnt > 0:
    rows_cnt += -1
    columns_cnt = columns
    while columns_cnt > 0:
        columns_cnt += -1
        print(Str.rightpad(str([rows-rows_cnt, columns-columns_cnt]), 9, " "), end="")
    print()
