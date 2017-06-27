#! python3
# -*- coding: utf-8 -*-
__version__ = "1.0.0"
# init (test for learning) release
__version__ = "1.0.1"
# fix misspelling
__version__ = "1.1.0"
# add file operations
__version__ = "1.1.1"
# add print functions from utils_dev
__version__ = "1.2.0"
# add path operations
__version__ = "1.2.1"
# print all obj with 'path', 'file'
__version__ = "1.2.2"
# f test_path_extend
__version__ = "1.2.3"
# test_file_create work
__version__ = "1.2.4"
# TestFileOperations bugfix
__version__ = "1.2.5alpha1"
# test test_file_wipe
__version__ = "1.2.5"
# test file_wipe workin'
__version__ = "1.2.6"
# test file_hide

from utils_dev import *
# for f in dir():
#     if f[:1].islower():
#         print(f)
#
# debug_print("path shit")
# for f in dir():
#     if "path" in f:
#         print(f)
#
# debug_print("file shit")
# for f in dir():
#     if "file" in f:
#         print(f)




import unittest
cls()

#class TestStringMethods(unittest.TestCase):
#
#    def test_upper(self):
#        self.assertEqual('foo'.upper(), 'FOO')
#
#    def test_isupper(self):
#        self.assertTrue('FOO'.isupper())
#        self.assertFalse('Foo'.isupper())
#
#    def test_split(self):
#        s = 'hello world'
#        self.assertEqual(s.split(), ['hello', 'world'])
#        # check that s.split fails when the separator is not a string
#        with self.assertRaises(TypeError):
#            s.split(2)


class TestPathOperations(unittest.TestCase):

    def test01_path_full_test(self):
        filename = "test.tst"
        self.assertEqual(path_full(filename), os.path.abspath(filename))

    if get_os() in ["macos", "linux"]:
        def test02unix_path_extend(self):
            self.assertEqual(path_extend("usr", "bin", "local"),
                             "/usr/bin/local")

    elif get_os() == "windows":
        def test02win_path_extend_smb_windows_share(self):
            self.assertEqual(path_extend(backslash, "192.168.99.91", "shares"),
                             r"\\192.168.99.91\shares")

        def test02win_path_extend_disc_c(self):
            self.assertEqual(path_extend("C:", "Users", "Test"),
                             r"C:\Users\Test")

        def test02win_path_extend_disc_c_lowercase(self):
            self.assertEqual(path_extend("c:", "users", "test", "test.tst"),
                             r"c:\users\test\test.tst")

        def test02win_path_extend_disc_s(self):
            self.assertEqual(path_extend("S:", "scripts", "UtilsUpdate"),
                             r"S:\scripts\UtilsUpdate")

        def test02win_path_extend_disc_s_lowercase(self):
            self.assertEqual(path_extend("s:", "scripts", "utilsupdate"),
                             r"s:\scripts\utilsupdate")

        def test02win_path_extend_bug(self):
            a = path_extend("C:", "Users", "Sklad_solvo", "PycharmProjects", "untitled", "utils.py")
            b = r"C:\Users\Sklad_solvo\PycharmProjects\untitled\utils.py"
            self.assertEqual(a, b)
        pass


class TestFileOperations(unittest.TestCase):
    global filename  # globalization for use filename in all tests
    filename = "test.tst"
    file_create(filename)
    global filename_backup  # globalization for use filename in all tests
    filename_backup = file_backup(filename, quiet=True)
    global filename_renamed_1st
    filename_renamed_1st = "test1.tst"
    global filename_renamed_2nd
    filename_renamed_2nd = "test2.tst"
    # create, backup, delete backup, move original, rename original,
    # wipe original, hide original,

    def test01_file_create(self):
        self.assertTrue(os.path.exists(filename))
        pass

    def test02_file_backup(self):
        self.assertTrue(os.path.exists(filename_backup))

    def test03_file_move_output_created(self):
        file_move(filename, filename_renamed_1st)
        self.assertTrue(os.path.exists(filename_renamed_1st))

    def test04_file_move_input_deleted(self):
        self.assertFalse(os.path.exists(filename))

    def test05_file_rename_output_created(self):
        file_move(filename_renamed_1st, filename_renamed_2nd)
        self.assertTrue(os.path.exists(filename_renamed_2nd))

    def test06_file_rename_input_deleted(self):
        self.assertFalse(os.path.exists(filename_renamed_1st))

    def test07_file_delete_backup(self):
        file_delete(filename_backup, quiet=True)
        self.assertFalse(os.path.exists(filename_backup))

    def test08_file_wipe_write(self):
        with open(filename_renamed_2nd, "w") as file:  # open file to write
            file.write("shit somewhere not happen")  # write to file
        with open (filename_renamed_2nd, "r") as file:  # open file to read
            string_io=file.read()  # read from file
        self.assertEqual(string_io, "shit somewhere not happen")

    def test09_file_wipe_wipe(self):
        file_wipe(filename_renamed_2nd)
        with open (filename_renamed_2nd, "r") as file:  # open file to read
            string_io=file.read()  # read from file
        self.assertEqual(string_io, "")

    def test10_file_hide_output_created(self):
        file_hide(filename_renamed_2nd)
        self.assertTrue(os.path.exists("."+filename_renamed_2nd))

    def test11_file_hide_input_deleted(self):
        self.assertFalse(os.path.exists(filename_renamed_2nd))

    def test12_file_delete(self):
        file_delete("."+filename_renamed_2nd, quiet=True)
        self.assertFalse("."+os.path.exists(filename_renamed_2nd))


#class TestIsPython3(unittest.TestCase):
#    def test_is_python3:
#		pass
#    pass







if __name__ == '__main__':
    unittest.main()
