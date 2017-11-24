#! python3
# -*- coding: utf-8 -*-
# mine commands
import sys
sys.path.append("../..")
sys.path.append("..\..")
sys.path.append(".")
sys.path.append("..")
sys.path.append("./term")
sys.path.append(r".\term")
from commands7 import *

mine_import("paramiko")
import paramiko
import getpass



host = "192.168.99.9"
username = "root"
password = Str.input_pass("pass 4 " + str(host) + ": ")

Ssh.get_avg_load_lin(host, username, password)