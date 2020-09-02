from commands import *
import sys


class Logger:
    def __init__(self, filename, rewrite=False):
        self.filename = filename
        if rewrite:
            File.wipe(filename)

    def plog(self, *args, sep=" "):
        Windows.fix_unicode_encode_error()
        Print(*args, sep=sep)
        args_strs = List.to_strings(args)
        File.write(self.filename, sep.join(args_strs))


logger = Logger(r"C:\Users\eegorov\Desktop\del.log", rewrite=True)

file1 = r"C:\Users\eegorov\Desktop\1p.csv"
file2 = r"C:\Users\eegorov\Desktop\2p.csv"

lines1 = Str.nl(File.read(file1))
lines2 = Str.nl(File.read(file2))

uuid = '"ouwdghgmizbnfpfvc6dar5io7i","'


def check_line(line):
    if len(line) <= len(uuid):
        return False
    uuid_line = line[1:len(uuid) - 3]
    if '"' in uuid_line:
        return False
    if line[0] == uuid[0] and line[len(uuid) - 3:len(uuid)] == uuid[len(uuid) - 3:len(uuid)]:
        return True
    return False


def rewrite_lines(lines, output_file):
    File.wipe(output_file)
    for cnt, line in enumerate(lines):
        if line.startswith('"UUID",'):
            line = Str.substring(line, 'UUID",')
            File.write(output_file, f"{line}")
            Print.colored(line, "red")
        elif check_line(line):
            Print.colored(line, "green")
            File.write(output_file, f"{newline}{line[len(uuid)-1:]}")
        else:
            File.write(output_file, f" {line}")
            Print.colored(line, "red")


#newfile1 = r"C:\Users\eegorov\Desktop\1p_better.csv"
#newfile2 = r"C:\Users\eegorov\Desktop\2p_better.csv"

#rewrite_lines(lines1, newfile1)
#rewrite_lines(lines2, newfile2)

#newlines1 = Str.nl(File.read(newfile1))
#newlines2 = Str.nl(File.read(newfile2))

#for line in newlines1:
#    if line not in newlines2:
#        print(line)

a = File.read(r"C:\Users\eegorov\Desktop\1p_other_people.csv")

File.write(r"C:\Users\eegorov\Desktop\1p_other_people_2.csv", a.replace('"",', ''))

