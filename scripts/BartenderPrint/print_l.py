#! python3
# -*- coding: utf-8 -*-
__version__ = "1.0.0"
# init release
__version__ = "1.1.0"
# many bugfixes
__version__ = "1.1.1"
# -noprint arg now opens PDF
__version__ = "1.1.1"
# -noprint arg now opens PDF in new window
__version__ = "1.2.0"
# -a4 arg now print on A4 printer
__version__ = "1.2.0"
# add python regeneration
__version__ = "1.3.0"
# added benchmark
__version__ = "1.3.1"
# moved to TeX Live

from commands7 import *
Bench.start()


class State:
    check_for_overfull_error = False
    # check_for_overfull_error = True

    tex_exists = False
    pdf_exists = False
    pdf_file = ""
    tex_file = ""
    py_file = ""
    try:
        tex_file_name = sys.argv[1]
        regen = False
        regen2 = False
        if "-r" in sys.argv:
            regen = True
            regen2 = True
        latex_engine = Path.extend("C:", "texlive", "bin", "win32", "pdflatex.exe")
        if "-xelatex" in sys.argv:
            latex_engine = Path.extend("C:", "texlive", "bin", "win32", "xelatex.exe")
        noprint = False
        if "-noprint" in sys.argv:
            noprint = True
        legacy_print = False
        if "--print-from-gui" in sys.argv:
            legacy_print = True
    except IndexError:
        raise FileNotFoundError("TeX file arg not found")

    tex_files_directory = Path.current()
    sumatra_pdf = Path.extend("C:", "Program Files", "SumatraPDF", "SumatraPDF.exe")
    printer_name = Path.extend(backslash, "192.168.99.20", "Datamax_A-4212")
    if "-a4" in sys.argv:
        printer_name = "20"
    latex_arguments = "--shell-escape"
    except_files = ["commands7.py", "generate.py", "print.py", "pycharm.py", "utils.py"]
    dir_content = []

    @classmethod
    def reload_dir(cls):
        cls.dir_content = Dir.list_of_files(cls.tex_files_directory)

    @classmethod
    def get_filenames(cls):
        cls.reload_dir()
        cls.tex_exists = False
        cls.pdf_exists = False
        cls.py_exists = False
        for filename in cls.dir_content:
            if cls.tex_file_name in filename:
                if (".pdf" in filename) and ("-pics" not in filename):
                    # debug_print("Wow! Such PDF!", filename)
                    cls.pdf_exists = True
                    cls.pdf_file = Path.full(filename)
                elif ".tex" in filename:
                    # debug_print("Many TeX code here!", filename)
                    cls.tex_exists = True
                    cls.tex_file = Path.full(filename)
                elif ".log" in filename:
                    # debug_print("Much loggish!", filename)
                    cls.tex_exists = True
                    cls.tex_file = Path.full(filename)
                elif ".py" in filename:
                    # debug_print("Excite! So Python!", filename)
                    cls.py_exists = True
                    cls.py_file = Path.full(filename)
                elif filename not in cls.except_files:
                    File.delete(path=Path.full(filename), quiet=False)


class Pdf:
    @staticmethod
    def regen_py():

        py = Path.extend("C:", "Windows", "py.exe")
        if State.legacy_print:
            Process.start(py, State.py_file, "--print-from-gui")
        else:
            Process.start(py, State.py_file)
        State.get_filenames()

    @staticmethod
    def regen_latex():
        if State.pdf_exists:
            File.delete(State.pdf_file)
        if len(State.tex_file) > 0:
            if State.check_for_overfull_error:
                for line in Console.get_output(State.latex_engine + " " + State.tex_file + " " + State.latex_arguments, quiet=True, split_lines=True):
                    if "full" in line:
                        from colorama import init
                        init()
                        cprint(line, "white", "on_red")
            else:
                # debug_print(State.latex_engine, State.tex_file, State.latex_arguments)
                Process.start(State.latex_engine, State.latex_arguments, State.tex_file)
        else:
            raise FileNotFoundError("State.tex_file is blank string")
        State.get_filenames()

    @staticmethod
    def print_():
        pass
        if not State.noprint:
            Process.start(State.sumatra_pdf, State.pdf_file, "-print-to", State.printer_name)
        else:
            Process.start(State.sumatra_pdf, State.pdf_file, new_window=True)


State.get_filenames()
if State.regen:
    if State.py_exists:
        Pdf.regen_py()
    Pdf.regen_latex()
Bench.end()
Pdf.print_()

