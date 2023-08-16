#! python3
# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append("..")
sys.path.append(".")
from commands import module9
import commands
__version__ = "0.0.1"

module_name = ""

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
#            s.split(2
#    def test_exception(self):
#         self.assertRaises(ValueError, Str.split_every, [12, 34, 56, 78, 90], 2) # yes, arguments after func

print("{module_name}", eval("{module_name}"), "{module_name}.__version__", eval("{module_name}.__version__"), "test_version", __version__)


if __name__ == '__main__':
    unittest.main()
