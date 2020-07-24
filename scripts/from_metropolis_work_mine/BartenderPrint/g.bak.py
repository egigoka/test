#! python3
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "..")
sys.path.insert(0, "../..")
sys.path.insert(0, "..\..")
from commands7 import *  # mine commands

__codegened_latex__ = Path.extend(Path.current(), "generate_l.tex")
__logfile__ = Path.extend(Path.current(), "log", "generate_l.txt")

class State:
    check_for_overfull_error = False
    # check_for_overfull_error = True
    legacy_print = False
    if "--print-from-gui" in sys.argv:
        legacy_print = True

class Contents():

    disable = "%"
    lnewline = backslash*2 + newline
    lnewparagraph = backslash + "par" + newline


    @staticmethod
    def document_class(size, type):
        string = "\documentclass[" + str(size) + "pt]{" + type + "}" + newline
        return string

    @staticmethod
    def cyrillic_support(babel="english,russian"):
        string = r"\usepackage{ifxetex}  % For work both with pdflatex and xelatex" + newline
        string += "\ifxetex" + newline
        string += "    %% xelatex" + newline
        string += r"    \usepackage{polyglossia}  % Multi-language support" + newline
        string += "    \setdefaultlanguage[spelling=modern]{russian}  % Main language of document" + newline
        string += "    \setotherlanguage{english}  % Second language of document" + newline
        string += "    \defaultfontfeatures{Ligatures={TeX}}  % Fonts properties" + newline
        string += "    \setmainfont[Ligatures={TeX}]{CMU Serif}  % Default font of document" + newline
        string += "    \setsansfont{CMU Sans Serif}  % Font without serifs" + newline
        string += "    \setmonofont{CMU Typewriter Text}  % Mono font" + newline
        string += "\else" + newline
        string += "    %% pdflatex" + newline
        string += r"    \usepackage{cmap}  % Search russian words thrue pdf" + newline
        string += r"    \usepackage[T2A]{fontenc}  % Inner font coding" + newline
        string += r"    \usepackage[utf8]{inputenc}  % Coding of source" + newline
        string += r"    \usepackage[" + babel + "]{babel}  % Russian words support for babel" + newline
        string += r"\fi" + newline
        string += r"    \usepackage{soulutf8}" + newline
        return string

    @staticmethod
    def geometry(*args):
        if len(args) == 0:
            args = ["%paper=a4paper", "paperwidth=58mm", "paperheight=59mm", "top=3mm", "bottom=3mm", "right=3mm",
                    "left=3mm", "%heightrounded", "showframe", "%margin=0.5mm"]
        string = r"\usepackage{geometry}" + newline
        string += "    \geometry" + newline
        string += "        {" + newline
        for arg in args[:-1]:
            string += "        " + arg + "," + newline
        string += "        " + args[-1] + "}" + newline
        return string

    @staticmethod
    def show_bold_frame():
        string = r"\usepackage{showframe} % показывает рамки?" + newline
        return string

    @staticmethod
    def enable_barcodes():
        string = r"\usepackage[bottom]{footmisc}  % Footnotes?" + newline
        string += r"\usepackage{pst-barcode,pstricks-add} % package for barcodes, use with auto-pst-pdf!" + newline
        string += r"\usepackage{auto-pst-pdf} % use with pdflatex only with arg --shell-escape!" + newline
        return string

    @staticmethod
    def tolerance(tolerance):
        string = r"\tolerance=" + str(tolerance) + " % extending spaces between words not so wide." + newline
        return string

    @staticmethod
    def sloppy():
        string = "\sloppy % maximum extending spaces between words. USE VERY CAREFULLY!" + newline
        return string

    @staticmethod
    def paragraph_indent(parindent):
        string = "\setlength\parindent{" + parindent + "} % paragraph width" + newline
        return string

    @staticmethod
    def change_font(font="\sfdefault"):
        string = r"\renewcommand{\familydefault}{" + font + "} % change font" + newline
        return string

    @staticmethod
    def change_size_of_unit(size):
        string = r"\psset{unit=" + str(size) + "} % change size of unit (idk what is that)" + newline
        return string

    @staticmethod
    def begin(what, arguments = False):
        string = r"\begin{" + what + "}"
        if arguments:
            string += arguments
        string += newline
        return string

    @staticmethod
    def bad_centering_of_all():
        string = r"\center % bad centering of all" + newline
        return string

    @staticmethod
    def define(variable, value):
        string = backslash + "def" + backslash + str(variable) + "{" + str(value) + "}" + newline
        return string

    @staticmethod
    def no_indent():
        string = r"\noindent  % disabling indentation" + newline
        return string

    @staticmethod
    def to_inches(value_in_mm):
        in_inches = str(int(value_in_mm) / 25.38)  # 25.3 give "Overfull \hbox (0.60028pt too wide) in paragraph at lines __--__" error#################################################
        if State.check_for_overfull_error:
            plog(__logfile__, "value_in_mm " + str(value_in_mm) + " in_inches " + in_inches, quiet=True)
        return in_inches#[:6]

    @classmethod
    def barcode(cls, textvar, width, height, type):
        string = r"\psbarcode{" + backslash + textvar + "}{width=" + cls.to_inches(width) +\
                 " height=" + cls.to_inches(height)
        if type == "ean13":
            string += "includetext guardwhitespace"
        string += "}{" + type + "}" + newline
        return string

    @staticmethod
    def textbox(textvar, type):  # type can be   centered   and s t r e t c h e d
        string = r"\makebox[\textwidth][" + type[:1] + r"]{\textbf{" + backslash + textvar +\
                 "}}  % box with text" + newline
        return string

    @staticmethod
    def end(what, arguments=False):
        string = r"\end{" + what + "}"
        if arguments:
            string += arguments
        string += newline
        return string

class Page():
    @staticmethod
    def set_58_60_geometry(showframe=False):
        showframe_arg = "%showframe"
        if showframe:
            showframe_arg = "showframe"
        Codegen.add_line(Contents.geometry("paperwidth=58mm",
                                           "paperheight=59mm",
                                           showframe_arg,
                                           "top=3mm",
                                           "bottom=3mm",
                                           "right=3mm",
                                           "left=3mm"
                                           ))
    @staticmethod
    def createpage_58_60(bar_text, second_line=None, barcode_type="code128"):
        class CurrentPage():
            width = 52
            height = 52
            height_of_5860_text = 9  # mm     not enough 8    10 no problem

            symbols_in_line = 13
            lines_max = 4
            total_second_line_symbols = symbols_in_line * (lines_max - 1)
            if second_line:
                second_line_crop = second_line[:total_second_line_symbols]
                text_lines = Str.split_every(second_line_crop, symbols_in_line)
                free_height = height - height_of_5860_text * (len(text_lines)+1)

            else:
                free_height = height - height_of_5860_text
        numerals = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "el", "twe"]

        # start of page
        Codegen.add_line(Contents.define("bartext", bar_text))
        if second_line:
            cnt = 0
            for line in CurrentPage.text_lines:
                cnt += 1
                Codegen.add_line(Contents.define("textadditional"+numerals[cnt], line))  # define new line of text
        Codegen.add_line(Contents.no_indent())
        Codegen.add_line(Contents.begin("pspicture", "%(0,0)(10,10) % idk what is that, size doesn't changing"))
        # plog(__logfile__, "CurrentPage.free_height = "+str(CurrentPage.free_height))
        Codegen.add_line(Contents.barcode("bartext", CurrentPage.width, CurrentPage.free_height, barcode_type))
        Codegen.add_line(Contents.end("pspicture"))
        # Codegen.add_line(Contents.lnewline)
        Codegen.add_line(Contents.lnewparagraph)
        # Codegen.add_line(Contents.disable)
        # Codegen.add_line(Contents.begin("minipage", r"[c][3mm][c]{\textwidth}"))
        Codegen.add_line(Contents.no_indent())
        Codegen.add_line(Contents.textbox("bartext", "centered"))
        if second_line:
            cnt = 0
            for line in CurrentPage.text_lines:
                cnt += 1
                Codegen.add_line(Contents.lnewline)
                Codegen.add_line(Contents.no_indent())
                Codegen.add_line(Contents.textbox("textadditional"+numerals[cnt], "centered"))
        Codegen.add_line(Contents.lnewparagraph)
        # Codegen.add_line(Contents.disable)
        # Codegen.add_line(Contents.end("minipage"))
        # end of page

#Codegen.debug = True

Codegen.start(file_path=__codegened_latex__)

Codegen.add_line(Contents.document_class(20, "extreport"))

Page.set_58_60_geometry(showframe=False)
Codegen.add_line(Contents.cyrillic_support())

# Codegen.add_line(Contents.disable)
# Codegen.add_line(Contents.show_bold_frame())
Codegen.add_line(Contents.enable_barcodes())

# Codegen.add_line(Contents.disable)
# Codegen.add_line(Contents.tolerance(10000))
Codegen.add_line(Contents.sloppy())
# Codegen.add_line(Contents.disable)
# Codegen.add_line(Contents.paragraph_indent("1mm"))
Codegen.add_line(Contents.change_font())
# Codegen.add_line(Contents.disable)
# Codegen.add_line(Contents.change_size_of_unit("1in"))

Codegen.add_line(Contents.begin("document"))
# Codegen.add_line(Contents.disable)
# Codegen.add_line(Contents.bad_centering_of_all())

####
# output =0
# while output<100:
#     output+=1
#     Page.createpage_58_60(output, "длинная-длиная-длинная-длинная-длинная-длинная-длинная-длинная строка")
# Page.createpage_58_60("test")
if State.legacy_print:
    with open(Path.extend(backslash, "192.168.99.91", "shares", "scripts", "BartenderPrint", "Bartender Documents", "Бирки_output.txt")) as file:
            # line = file.readline()
        for line in file:
            line = line.rstrip(newline)
            Page.createpage_58_60(line)
else:
    pass
    cnt = 0
    count = 1
    while cnt < count:
        cnt += 1
        # Page.createpage_58_60("TR02", "2 группа конечная")
        # Page.createpage_58_60("TR03", "конечная 3 группа")
        # Page.createpage_58_60("TR03", "конечная 3 группа")
        # Page.createpage_58_60("TR03", "конечная 3 группа")
        # Page.createpage_58_60("TR04", "конечная 4 группа")
        # Page.createpage_58_60("TR04", "конечная 4 группа")
        # Page.createpage_58_60("TR04", "конечная 4 группа")
        # Page.createpage_58_60("TR05", "конечная 5 группа")
        # Page.createpage_58_60("TR05", "конечная 5 группа")
        # Page.createpage_58_60("TR05", "конечная 5 группа")
        Page.createpage_58_60("TR07-01", "8 группа транзитная")
        Page.createpage_58_60("TR07-01")
        Page.createpage_58_60("TR07-01", "длинная-длинная-длинная-длинная-длинная-длинная строка")
        Page.createpage_58_60("TR07-01", "1234567890123456789012345678901234567890123456789012345678901234567890123end")
        # Page.createpage_58_60("TR08", "8 группа конечная")
        # Page.createpage_58_60("2", "запрос работы", barcode_type="code39")
        # Page.createpage_58_60("2", "запрос работы", barcode_type="code39")
        # Page.createpage_58_60("2", "запрос работы", barcode_type="code39")
        # Page.createpage_58_60("2B502522", "на D12")
        # Page.createpage_58_60("2B502523", "на TR02")
        # Page.createpage_58_60("TRN-01-01", "транзит 1 группа")
        # Page.createpage_58_60("TR02-01", "транзит 2 группа")
        # Page.createpage_58_60("D12", "12 ворота")


    # Page.createpage_58_60("00560906533","Косовских Дмитрий карщик")

Codegen.add_line(Contents.end("document"))

# todo cls INDENT oprion
