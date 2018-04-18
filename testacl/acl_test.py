#! python3
# -*- coding: utf-8 -*-
# http://python.su/forum/topic/15531/?page=1#post-93316
import sys
sys.path.append("../..")
sys.path.append("..\..")
sys.path.append(".")
sys.path.append("..")
sys.path.append("./term")
sys.path.append(r".\term")
from commands8 import *

import win32security
import ntsecuritycon as con




FILENAME = Path.extend(Path.working(), "fuck.txt")

userx, domain, type = win32security.LookupAccountName ("", "EEgorov")
usery, domain, type = win32security.LookupAccountName ("", "MKurtukova")

sd = None
dacl = None

def renew():
    global sd
    global dacl
    sd = win32security.GetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION)
    dacl = sd.GetSecurityDescriptorDacl()  # instead of dacl = win32security.ACL()

renew()

Print.debug("userx", userx, "usery", usery, "domain", domain, "type", type, "sd", sd, "dacl", dacl, "FILENAME", FILENAME)
Print.debug("userx", userx, "usery", usery, "domain", domain, "type", type, "sd", sd, "dacl", dacl, "FILENAME", FILENAME, raw=True)

#dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_GENERIC_READ | con.FILE_GENERIC_WRITE, userx)
#dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, usery)

#sd.SetSecurityDescriptorDacl(1, dacl, 0)   # may not be necessary
#win32security.SetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION, sd)
