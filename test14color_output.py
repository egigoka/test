#! python3

# Colorama 0.3.7 example https://pypi.python.org/pypi/colorama
import sys
from colorama import init
init()

from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

print('\033[31m' + 'some red text')
print('\033[30m') # and reset to default color

from colorama import init
from termcolor import colored

# use Colorama to make Termcolor work on Windows too
init()

# then use Termcolor for all colored text output
#print(colored('Hello, World!', 'green', 'on_red'))


from colorama import init, AnsiToWin32
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream

# Python 2
print >>stream, Fore.BLUE + 'blue text on stderr'

# Python 3
print(Fore.BLUE + 'blue text on stderr', file=stream)




# Termcolor 1.1.0 example https://pypi.python.org/pypi/termcolor
import sys
from termcolor import colored, cprint

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)
cprint('Hello, World!', 'green', 'on_red')

print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
print_red_on_cyan('Hello, World!')
print_red_on_cyan('Hello, Universe!')

for i in range(10):
    cprint(i, 'magenta', end=' ')

cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)