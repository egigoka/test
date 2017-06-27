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

from utils_dev import *
for f in dir(utils_dev):
    if f[:1].islower()
        print(f)
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

class TestFileOperations(unittest.TestCase):

    def file_backup_test(self):
        file_backup()
        self.assertTrue()

    def file_create_test(self):
        pass

    def file_delete_test(self):
        pass

    def file_hide_test(self):
        pass

    def file_move_test(self):
        pass

    def file_rename_test(self):
        pass

    def file_wipe_test(self):
        pass


if __name__ == '__main__':
    unittest.main()
