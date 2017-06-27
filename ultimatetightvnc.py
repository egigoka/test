#! python3
# -*- coding: utf-8 -*-
from utils import path_extend, backslash
from current_paths import share
# code simplification???
ip = "ip"
licences = "!Проверка лицензий"
groups_dir = "Группы"
# 99.247 88.221 - СБ левый s.gultyaev
# 98.246 93.100 - СБ правый
# 98.214 - оператор видеонета в РИО
# 98.244 - 10 group
# 98.211 - alco
# 98.218 - 3 group
# 98.193 - холодильник

def get_sticker(group, img = "sticker.jpg"):
    path_extend(share, licences, groups_dir, args, img)



# todo "C:\Program Files (x86)\TightVNC\vncviewer.exe" -

# todo implement change_ip.py in system32
# todo bat to exe with admin rights to change_ip.py

# todo ip of all pc's and passwords

groups_params = {}

groups_params_add(ip, sticker = None, programs_img = None, ):
    try:
        sticker = getsticker()
    except:
        pass


ips_groups = {
              "Холодильник":{ip:"192.168.98.193", }
                             #"windows_sticker":},

              }

# for name in ips_groups.items():
#     print(name, ip)
