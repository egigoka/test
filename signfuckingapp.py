from commands import *

print("reading_config")
# config
CODESIGN_SERT_NUMBER = "57B47CMXRR"
SKIPPED_EXTENSIONS = '''
.plist
.icns
.pdf
.png
.ini
.txt
.js
.xml
.ttf
.otf
.tiff
.mp4
.html
.css
.json
.rtf
.wav
.svg
.gif
.markdown
.log
.jpg
.xhtml
.webp
.conf
.less
.zip
.csv
.config
.lang
'''
SKIPPED_EXTENSIONS = Str.nl(SKIPPED_EXTENSIONS)
SKIPPED_EXTENSIONS = List.remove_empty_strings(SKIPPED_EXTENSIONS)
# config END

print("reading arguments")
# args
if len(OS.args) < 2 :
    print(r'''usage:
python3 signfuckingapp.py <path to app> <arguments>

example:
python3 signfuckingapp.py /Applications/Microsoft\ Excel.app

additional arguments:
--sign-all - sign all and every file in .app except those, that extensions are listed in SKIPPED_EXTENSIONS in this 
script
-y - skip user interaction''')
    OS.exit(0)
SIGN_ALL = "--sign-all" in OS.args
WITHOUT_CONFIRMATION = "-y" in OS.args
# args END


def sign_file(path):
    if File.get_extension(path) not in SKIPPED_EXTENSIONS:
        escaped_path = Bash.argument_escape(path)
        OS.system(f"sudo xattr -lr {escaped_path}", verbose=True)
        OS.system(f"sudo xattr -cr {escaped_path}", verbose=True)
        OS.system(f"sudo chmod +x {escaped_path}", verbose=True)
        OS.system(f"sudo codesign -f -s {CODESIGN_SERT_NUMBER} {escaped_path}", verbose=True)


def add_file_thread(path):
    t.add(sign_file, name=f"signing {path}", args=[path])


def sign(path):
    if File.exist(path):
        add_file_thread(path)
    if path.endswith(".app") and not SIGN_ALL:
        add_file_thread(path)
        path_to_executables = Path.combine(path, "Contents", "MacOS")
        print(Dir.list_of_entries(path_to_executables))
        sign(path_to_executables)
    elif Dir.exist(path):
        confirmed = WITHOUT_CONFIRMATION
        if not confirmed:
            confirmed = CLI.get_y_n(f"Sign everything in {path}")
        if confirmed:
            for something in Dir.list_of_entries(path):
                something_path = Path.combine(path, something)
                sign(something_path)


print("starting")
t = Threading(verbose=True)
print("adding threads info")
sign(OS.args[1])
print("staring threads")
t.start(wait_for_keyboard_interrupt=True)