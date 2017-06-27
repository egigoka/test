#! python3
# -*- coding: utf-8 -*-

import unittest, shutil, os


class TestFileOperations(unittest.TestCase):
    global filename, filename_renamed_1st, filename_renamed_2nd
    # globalization for use filename in all tests
    filename = "test.tst"
    with open(filename, 'a'):  # open file and close after
        os.utime(filename, None)  # changes time of file modification
    filename_renamed_1st = "test1.tst"
    filename_renamed_2nd = "test1.tst"

    def test01_file_move_output_created(self):
        shutil.move(filename, filename_renamed_1st)
        self.assertTrue(os.path.exists(filename_renamed_1st))

    def test02_file_move_input_deleted(self):
        self.assertFalse(os.path.exists(filename))

    def test03_file_rename_output_created(self):
        shutil.move(filename_renamed_1st, filename_renamed_2nd)
        self.assertTrue(os.path.exists(filename_renamed_2nd))

    def test04_file_rename_input_deleted(self):
        self.assertFalse(os.path.exists(filename_renamed_1st))


if __name__ == '__main__':
    unittest.main()
