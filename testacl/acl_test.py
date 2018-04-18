#! python3
# -*- coding: utf-8 -*-
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
import pywintypes
import uuid
import win32net

verbose_delete = True
debug_verbose = False
print_errors_while_creating_users = False

try:
    filename = Path.full(sys.argv[1])
except FileNotFoundError:
    filename = Path.extend(Path.commands8(), "testacl", "text.txt")
except IndexError:
    filename = Path.extend(Path.commands8(), "testacl", "text.txt")


while not os.path.isfile(filename):
    filename = input("Enter filename: ")


users = {}
sd = None
dacl = None
backupjsonfile = filename+"_bak.json"
userscreatedjsonfile = Path.extend(Path.working(), "userscreated.json")

def dirify(object):
    for subobj in dir(object):
        if "__" not in subobj:
            print(subobj)

def add_user(username):  # deprecated, return infro about user to "users" list
    try:
        win32security.LookupAccountName("", username)
    except pywintypes.error as e:
        print(e,"",end="")  # print error and space
        print("user", username, "not found")
        return
    global users
    users[username] = {}
    users[username]["sid_obj"], users[username]["domain"], users[username]["type"] = win32security.LookupAccountName ("", username)


def renew():
    global sd
    global dacl
    SECURITY_DESCRIPTOR = win32security.GetFileSecurity(filename, win32security.DACL_SECURITY_INFORMATION)
    DACL = SECURITY_DESCRIPTOR.GetSecurityDescriptorDacl()  # instead of dacl = win32security.ACL()
    sd = SECURITY_DESCRIPTOR
    dacl = DACL
renew()


def ace_count():
    renew()
    return dacl.GetAceCount()


def save_dacl():
    sd.SetSecurityDescriptorDacl(1, dacl, 0)  # may not be necessary
    win32security.SetFileSecurity(filename, win32security.DACL_SECURITY_INFORMATION, sd)


def flush_acl():
    if debug_verbose: print("file", filename, "has", ace_count(), "ACE's before flush")
    for i in Int.from_to(1, ace_count()):
        if verbose_delete:
            tempace = dacl.GetAce(0)
            print(tempace[2], "is removing now...")
        dacl.DeleteAce(0)
    save_dacl()
    renew()
    if debug_verbose: print("file", filename, "have", ace_count(), "ACE's now")

def create_user():
    while True:
        try:
            username = "User_" + Random.string(11)
            password = Random.string(14)
            err = Console.get_output("net user " + username + " " + password + " /ADD")
            if "The command completed successfully." in err:
                userscreated = Json.load(userscreatedjsonfile, quiet=True)
                userscreated[username] = password
                Json.save(userscreatedjsonfile, userscreated, quiet=True)
                return username
            else:
                if print_errors_while_creating_users: print(err)
        except subprocess.CalledProcessError as err:
            if print_errors_while_creating_users: print(err)
            return create_user()


def sid_to_username(sid):
    SID_object = win32security.ConvertStringSidToSid(sid)
    return win32security.LookupAccountSid(None, SID_object)
    pass


def remove_all_created_users():  # remove only users from json file
    for user in Json.load(userscreatedjsonfile):
        os.system("net user " + user + " /DELETE")
        time.sleep(0.1)
    File.backup(userscreatedjsonfile)
    Json.save(userscreatedjsonfile, {})


def remove_all_created_users_2(filename):  # deprecated
    for line in Str.nl(File.read(filename)):
        username = Str.substring(line, before="User_", after="    ")
        os.system("net user User_" + username + " /DELETE")
        time.sleep(0.1)
    File.backup(userscreatedjsonfile)
    Json.save(userscreatedjsonfile, {})


def remove_all_created_users_3():  # remove all users with Users_ prefix
    for line in Str.nl(Console.get_output("wmic useraccount")):
        username = Str.substring(line, before="User_", after="    ")
        os.system("net user User_" + username + " /DELETE")
        time.sleep(0.1)
    File.backup(userscreatedjsonfile)
    Json.save(userscreatedjsonfile, {})


def count_of_users():
    a = Console.get_output("wmic username")
    a = Str.nl(a)
    print(len(a))

print(newline, "file", filename, "has", ace_count(), "ACE's", newline)

if CLI.get_y_n("Save ACEs"):
    json_string = {}
    for i in Int.from_to(0, ace_count()-1):
        i = str(i)
        json_string[i] = {}
        tempace = dacl.GetAce(int(i))
        json_string[i]["0"] = 1
        json_string[i]["1"] = tempace[1]
        json_string[i]["2"] = win32security.ConvertSidToStringSid(tempace[2])
        Print.rewrite(CLI.wait_update(quiet=True), "Saving", tempace[2])
    Print.rewrite(" "*Console.width())
    if debug_verbose: Print.debug(json_string)
    Json.save(backupjsonfile, json_string, quiet=debug_verbose)
    json_string = Json.load(backupjsonfile, quiet=debug_verbose)
    if debug_verbose: print("file", filename, "have", ace_count(), "ACE's")
    if debug_verbose: print("backup file", backupjsonfile, "have", len(json_string), "ACE's")

if ace_count() == 0:
    print("DACL already clean")
else:
    if CLI.get_y_n("flush ACL"):
        flush_acl()

cnt = 0
# if ace_count() == 0:
if CLI.get_y_n("Flood ACL"):
    try:
        while True:
            if cnt%5 == 0:
                Print.rewrite(CLI.wait_update(quiet=True) + str(cnt))
            level = 1
            binary_mask = 2032127
            username = create_user()
            SID_object = win32security.LookupAccountName("", username)[0]
            dacl.AddAccessAllowedAce(level, binary_mask, SID_object)
            save_dacl()
            cnt += 1
            #print(cnt)
    except pywintypes.error as err:
        Print.debug(err, "max count of ACE's is", ace_count())
# else:
    # print("flood test isn't check good if you didn't flush DACL")

if CLI.get_y_n("Restore ACEs"):
    json_string = Json.load(backupjsonfile, quiet=debug_verbose)
    if debug_verbose: print("file", filename, "has", ace_count(), "ACE's before restore")
    if debug_verbose: print("backup file", backupjsonfile, "have", len(json_string), "ACE's")
    for int_, ace in Dict.iterable(json_string):
        dacl.AddAccessAllowedAce(json_string[int_]["0"], json_string[int_]["1"], win32security.ConvertStringSidToSid(json_string[int_]["2"]))
        Print.rewrite(CLI.wait_update(quiet=True), "Restoring", json_string[int_]["2"])
    Print.rewrite(" "*Console.width())
    save_dacl()
    if debug_verbose: print("file", filename, "have", ace_count(), "ACE's now")

if CLI.get_y_n("Delete all users created by this sctipt"):
    remove_all_created_users()
if CLI.get_y_n("Delete all users with 'User_' prefix"):
    remove_all_created_users_3()






#dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_GENERIC_READ | con.FILE_GENERIC_WRITE, userx)
#dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, usery)



# https://stackoverflow.com/questions/12168110/setting-folder-permissions-in-windows-using-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa