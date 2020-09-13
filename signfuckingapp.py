from commands import *

CODESIGN_SERT_NUMBER = "57B47CMXRR"

OS.system(f"sudo xattr -lr {Bash.argument_escape(sys.argv[1])}", verbose=True)
OS.system(f"sudo xattr -cr {Bash.argument_escape(sys.argv[1])}", verbose=True)
OS.system(f"sudo codesign -f -s {CODESIGN_SERT_NUMBER} {Bash.argument_escape(OS.args[1])}", verbose=True)