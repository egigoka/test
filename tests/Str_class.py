#! python3
# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append("..")
sys.path.append(".")
from str8 import *
import str8
__version__ = "0.0.28"


print("str8", str8, "str8.__version__", str8.__version__, "test_version", __version__)

class TestStrClassMethods(unittest.TestCase):
    def test01_to_quotes(self):  # to_quotes(some_string):  # just place input string inside "" quotes
        self.assertEqual(Str.to_quotes(""), '""')
        self.assertEqual(Str.to_quotes(123), '"123"')
        self.assertEqual(Str.to_quotes("test test"), '"test test"')

    def test02_to_quotes_2(self):  # to_quotes_2(some_string):  # place input string inside '' quotes
        self.assertEqual(Str.to_quotes_2(""), "''")
        self.assertEqual(Str.to_quotes_2(123), "'123'")
        self.assertEqual(Str.to_quotes_2("test test"), "'test test'")

    def test03_get_integers(self): # get_integers(string):  # return list of integers from string, !!!floating not supported!!!
        self.assertEqual(Str.get_integers(123), [123])
        self.assertEqual(Str.get_integers("123"), [123])
        self.assertEqual(Str.get_integers("123 456"), [123, 456])
        self.assertEqual(Str.get_integers("1pen2pineapple3apple4pen"), [1, 2, 3, 4])

    def test04_newlines_to_strings(self):
        self.assertEqual(Str.newlines_to_strings("""
        """), ["","        "])
        self.assertEqual(Str.newlines_to_strings("""
"""), ["",""])
        self.assertEqual(Str.newlines_to_strings(""), [""])
        self.assertEqual(Str.newlines_to_strings("""word1, 
        word2, 
        word3
"""), ["word1, ", "        word2, ", "        word3", ""])

    def test05_nl(self):
        self.assertEqual(Str.nl("""word1, 
        word2, 
        word3
"""), ["word1, ", "        word2, ", "        word3", ""])

    def test06_split_every(self):
        self.assertEqual(Str.split_every("1234567890", 3), ["123", "456", "789", "0"])
        self.assertRaises(ValueError, Str.split_every, [12, 34, 56, 78, 90], 2)
    # split_every(string, chars):  # split string every
    # leftpad(string, leng, ch="0", rightpad=False):  # return string with
      # d added characters to left side. If string longer — return original string
    # rightpad(cls, string, leng, ch="0"):  # return string with added
      # d characters to right side. If string longer — return original string
    # substring(string, before, after=None, return_after_substring=False):  # return
      # d string that between "before", and "after" strings, not including
      # d those. If "return_after_substring", return typle with substring and
      # d part of string after it.
    # def diff_simple(string_a, string_b):  # d print all symbol differents.
      # d Not all mine code, must rewrite.
    # def input_pass(string="Password:"):  # d return string from user, securely
      # d inputed by getpass library
    # def input_int(message="Input integer: ", minimum=None, maximum=None, default=None, quiet=False):
      # d return integer from user with multible parameters.
    # remove_spaces(Str, string_):
    # get_words(Str, string_):
    # def strip_end(text, suffix):  # return string without suffix, if string end with it.

if __name__ == '__main__':
    unittest.main()
