
'''Colors class:reset all colors with colors.reset; two
sub classes fg for foreground
and bg for background; use as colors.subclass.colorname.
i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable,
underline, reverse, strike through,
and invisible work with the main class i.e. colors.bold'''
colors={"reset": '\033[0m',
    "bold": '\033[01m',
    "disable": '\033[02m',
    "underline": '\033[04m',
    "reverse": '\033[07m',
    "strikethrough": '\033[09m',
    "invisible": '\033[08m'
}
fg = {
    "black": '\033[30m',
    "red": '\033[31m',
    "green": '\033[32m',
    "yellow": '\033[33m',
    "blue": '\033[34m',
    "purple": '\033[35m',
    "cyan": '\033[36m',
    "white": '\033[37m',
    
    "lightblack": '\033[90m',
    "lightred": '\033[91m',
    "lightgreen": '\033[92m',
    "lightyellow": '\033[93m',
    "lightblue": '\033[94m',
    "lightpurple": '\033[95m',
    "lightcyan": '\033[96m',
    "lightwhite": '\033[37m'
}
bg = {
    "black": '\033[40m',
    "red": '\033[41m',
    "green": '\033[42m',
    "yellow": '\033[43m',
    "blue": '\033[44m',
    "purple": '\033[45m',
    "cyan": '\033[46m',
    "white": '\033[47m',
    
    "lightblack": '\033[100m',
    "lightred": '\033[101m',
    "lightgreen": '\033[102m',
    "lightyellow": '\033[103m',
    "lightblue": '\033[104m',
    "lightpurple": '\033[105m',
    "lightcyan": '\033[106m',
    "lightwhite": '\033[107m'
}

for fn, f in fg.items():
    for bn, b in bg.items():
        if fn == bn:
            continue
        print(f,b, f"{fn} on {bn}", colors["reset"], sep = "")
