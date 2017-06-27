#! python3
# -*- coding: utf-8 -*-

# it doesn't work!!!!

import datetime
from utils import *
from current_paths import *

# 7za.exe a -tzip -ssw -mx7 -r0 -x@exclusions.txt full_path_for_the_archive working_dir


slepki = path_extend(documents_dir, "Downloads", "Слепки", dottedtime())  # sorry for that
documents_dir_copy = path_extend(documents_dir, "copy")
dir_create(documents_dir_copy)

dir_create(slepki)

file_types_from_documents_dir = [
    "*.bat"
    "*.py"
    "*.exe"
]
for file_type in file_types_from_documents_dir:
    command = "copy " + documents_dir + file_type + " " + documents_dir_copy + backslash
    print(command)
    #os.system(command)

folders = [
           share,
           pycharm_projects
           ]

for folder in folders:
    command = "copy " + folder + " " + documents_dir_copy + backslash
    print(command)
    #os.system(command)

def open_explorer(folder):
    os.system("explorer " + folder)

open_explorer(share)
open_explorer(pycharm_projects)
open_explorer(documents_dir)
open_explorer(slepki)
