#! python3
# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append("..")
sys.path.append(".")
from commands8 import *
import commands8
__version__ = "3.0.3"


print("commands8", commands8, "commands8.__version__", commands8.__version__, "test_version", __version__)

class TestPathOperations(unittest.TestCase):

    def test01_path_full_test(self):
        filename = "test.tst"
        self.assertEqual(Path.full(filename), os.path.abspath(filename))

    if OS.name in ["macos", "linux"]:
        def test02_unix_path_extend(self):
            self.assertEqual(Path.extend("usr", "bin", "local"),
                             "/usr/bin/local")

    elif OS.name == "windows":
        def test02_win_path_extend_smb_windows_share(self):
            self.assertEqual(Path.extend(backslash, "192.168.99.91", "shares"),
                             r"\\192.168.99.91\shares")

        def test02_win_path_extend_disc_c(self):
            self.assertEqual(Path.extend("C:", "Users", "Test"),
                             r"C:\Users\Test")

        def test02_win_path_extend_disc_c_lowercase(self):
            self.assertEqual(Path.extend("c:", "users", "test", "test.tst"),
                             r"c:\users\test\test.tst")

        def test02_win_path_extend_disc_s(self):
            self.assertEqual(Path.extend("S:", "scripts", "UtilsUpdate"),
                             r"S:\scripts\UtilsUpdate")

        def test02_win_path_extend_disc_s_lowercase(self):
            self.assertEqual(Path.extend("s:", "scripts", "utilsupdate"),
                             r"s:\scripts\utilsupdate")

        def test02_win_path_extend_bug(self):
            a = Path.extend("C:", "Users", "Sklad_solvo", "PycharmProjects", "untitled", "utils.py")
            b = r"C:\Users\Sklad_solvo\PycharmProjects\untitled\utils.py"
            self.assertEqual(a, b)
        pass

    ### todo check for . and .. in windows paths
    ### todo check for spaces in path1


if __name__ == '__main__':
    unittest.main()
