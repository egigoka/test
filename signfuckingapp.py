from commands import *

CODESIGN_SERT_NUMBER = "57B47CMXRR"

def sign_file(path):
    escaped_path = Bash.argument_escape(path)
    OS.system(f"sudo xattr -lr {escaped_path}", verbose=True)
    OS.system(f"sudo xattr -cr {escaped_path}", verbose=True)
    OS.system(f"sudo chmod +x {escaped_path}", verbose=True)
    OS.system(f"sudo codesign -f -s {CODESIGN_SERT_NUMBER} {escaped_path}", verbose=True)


def sign(path):
    if File.exist(path):
        sign_file(path)
    if path.endswith(".app"):
        sign_file(path)
        path_to_executables = Path.combine(path, "Contents", "MacOS")
        print(Dir.list_of_entries(path_to_executables))
        sign(path_to_executables)
    elif Dir.exist(path):
        if CLI.get_y_n(f"Sign everything in {path}?"):
            for something in Dir.list_of_entries(path):
                something_path = Path.combine(path, something)
                sign(something_path)


sign(OS.args[1])