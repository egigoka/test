#! python3
# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append("..")
sys.path.append(".")
from str8 import *
import str8
__version__ = "0.1.3"

# todo check args typeerror

print("str8", str8, "str8.__version__", str8.__version__, "test_version", __version__)

class TestStrClassMethods(unittest.TestCase):
    def test01_to_quotes(self):  # to_quotes(some_string):  # just place input string inside "" quotes
        self.assertEqual(Str.to_quotes(""), '""')
        self.assertEqual(Str.to_quotes(123), '"123"')
        self.assertEqual(Str.to_quotes("test test"), '"test test"')
        # todo list value error

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
        self.assertEqual(Str.split_every(123456789, 3), ["123", "456", "789"])
        self.assertRaises(ValueError, Str.split_every, [12, 34, 56, 78, 90], 2)
        self.assertRaises(ValueError, Str.split_every, "somestring", 0)

    def test07_leftpad(self): # leftpad(string, leng, ch="0", rightpad=False):
        pass
        # todo check for null chars
        # todo check for all args ints input
        # todo check for null char
        # todo check for string char
        # todo check for int string char
        # todo check for usual use
        # todo check for usual use with alphabetic char

    def test08_rightpad(self):# rightpad(string, leng, ch="0"):
        pass
        # todo check for null chars
        # todo check for all args ints input
        # todo check for null char
        # todo check for string char
        # todo check for int string char
        # todo check for usual use
        # todo check for usual use with alphabetic char


    # substring(string, before, after=None, return_after_substring=False):  # return
      # d string that between "before", and "after" strings, not including
      # d those. If "return_after_substring", return typle with substring and
      # d part of string after it.
    def test09_substring(self):
        self.assertEqual(Str.substring("", ""), "")
        self.assertEqual(Str.substring(123, 1), "23")
        self.assertEqual(Str.substring("test testing test", before="testing "), "test")
        self.assertEqual(Str.substring("test testing test", before="test ", after=" test"), "testing")
        # todo check for null before arg
        # todo check for null after arg
        # todo check for null string

    # def diff_simple(string_a, string_b):  # d print all symbol differents.
      # d Not all mine code, must rewrite.
    def test10_substring(self):
        pass
        # todo just rewrite this shit

    # def input_pass(string="Password:"):  # d return string from user, securely
      # d inputed by getpass library
    def test11_substring(self):
        pass
        # todo check for null before arg
        # todo check for null after arg
        # todo check for null string

    # def input_int(message="Input integer: ", minimum=None, maximum=None, default=None, quiet=False):
      # d return integer from user with multible parameters.
    def test12_input_int(self):
        self.assertEqual(Str.get_integers(""), [])
        self.assertEqual(Str.get_integers("123    456,    789test"), [123, 456, 789])
        self.assertEqual()
    # remove_spaces(Str, string_):
    def test13_remove_spaces(self):
        self.assertEqual(Str.remove_spaces(""), "")
        self.assertEqual(Str.remove_spaces(123), "123")
        self.assertEqual(Str.remove_spaces("        1    2            3       "), " 1 2 3 ")
        self.assertEqual(Str.remove_spaces("        1    2    \n        3       "), " 1 2 \n 3 ")
    # get_words(Str, string_):
    def test14_get_words(self):
        self.assertEqual(Str.get_words("      onee towoo, three     four  "), ["onee", "towoo,", "three", "four"])
        self.assertEqual(Str.get_words(""), [])

if __name__ == '__main__':
    unittest.main()
