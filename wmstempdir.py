#! python3
# -*- coding: utf-8 -*-
if True:
    __version__ = "1.0.0"
    # init release

from commands7 import *

class State:
    pass

def get_contents_len(path):
    try:
        dir_contents = Dir.contents(path)
        print(os.path.split(path)[1], "contents", len(dir_contents), "files")
    except FileNotFoundError:
        print("Path", path, "isn't found")

while True:
    get_contents_len(Locations.wms2host)
    get_contents_len(Locations.host2wms)
    get_contents_len(Path.extend(backslash, "192.168.99.91", "errfolder"))
    time.sleep(1)