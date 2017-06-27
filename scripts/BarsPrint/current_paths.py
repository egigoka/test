#! python3
# -*- coding: utf-8 -*-
__version__ = "1.3.0"
from utils import path_extend

share = path_extend("S:")
shares = share

scripts_folder = path_extend(share, "scripts")
scripts_dir = scripts_folder

documents_dir = path_extend("C:", "Users", "Sklad_solvo")

pycharm_projects = path_extend(documents_dir, "PycharmProjects", "untitled")

notepad_plus_plus_exec_name = "notepad++.exe"
notepad_plus_plus_dir = path_extend("C:", "Program Files", "Notepad++")
notepad_plus_plus_exec = path_extend(notepad_plus_plus_dir, notepad_plus_plus_exec_name)

notepad_exec = "notepad"

py = "py"
pyw = "pyw"
