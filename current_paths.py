#! python3
# -*- coding: utf-8 -*-
from utils import path_extend, backslash
share = path_extend(backslash, "192.168.99.91", "shares")
documents_dir = path_extend("C:", "Users", "Sklad_solvo")
pycharm_projects = path_extend(documents_dir, "PycharmProjects", "untitled")