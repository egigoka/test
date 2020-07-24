#! python3
# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append("..")
sys.path.append(".")
from commands8 import *
__version__ = "0.0.1"

class TestFileOperations(unittest.TestCase):
    global filename  # globalization for use filename in all tests
    filename = "test.tst"
    File.create(filename)
    global filename_backup  # globalization for use filename in all tests
    filename_backup = File.backup(filename, quiet=True)
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
        File.move(filename, filename_renamed_1st)
        self.assertTrue(os.path.exists(filename_renamed_1st))

    def test04_file_move_input_deleted(self):
        self.assertFalse(os.path.exists(filename))

    def test05_file_rename_output_created(self):
        File.rename(filename_renamed_1st, filename_renamed_2nd)
        self.assertTrue(os.path.exists(filename_renamed_2nd))

    def test06_file_rename_input_deleted(self):
        self.assertFalse(os.path.exists(filename_renamed_1st))

    def test07_file_delete_backup(self):
        File.delete(filename_backup, quiet=True)
        self.assertFalse(os.path.exists(filename_backup))

    def test08_file_wipe_write(self):
        with open(filename_renamed_2nd, "w") as file:  # open file to write
            file.write("shit somewhere not happen")  # write to file
        with open (filename_renamed_2nd, "r") as file:  # open file to read
            string_io=file.read()  # read from file
        self.assertEqual(string_io, "shit somewhere not happen")

    def test09_file_wipe_wipe(self):
        File.wipe(filename_renamed_2nd)
        with open (filename_renamed_2nd, "r") as file:  # open file to read
            string_io=file.read()  # read from file
        self.assertEqual(string_io, "")

    def test10_file_hide_output_created(self):
        File.hide(filename_renamed_2nd)
        self.assertTrue(os.path.exists("."+filename_renamed_2nd))

    def test11_file_hide_input_deleted(self):
        self.assertFalse(os.path.exists(filename_renamed_2nd))

    def test12_file_delete(self):
        File.delete("."+filename_renamed_2nd, quiet=True)
        self.assertFalse(os.path.exists("."+filename_renamed_2nd))

if __name__ == '__main__':
    unittest.main()
