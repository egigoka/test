#! python3
# -*- coding: utf-8 -*-
# http://python.su/forum/topic/15531/?page=1#post-93316
from const8 import *

__version__ = "0.1.0"
class Str:
    @staticmethod
    def to_quotes(some_string):  # just place input string inside "" quotes
        return '"' + str(some_string) + '"'

    @staticmethod
    def to_quotes_2(some_string):  # place input string inside '' quotes
        return "'" + str(some_string) + "'"

    @staticmethod
    def get_integers(string):  # return list of integers from string, !!!floating not supported!!!
      # todo add support for floating numbers, it will be cool!
        integer_found = False
        integers = []
        current_integer = 0
        negative = False
        for symbol in str(string) + " ":  # in exception some processing, meh :(
            try:
                if symbol in ['-', '—']:
                    negative = True
                    continue
                int(symbol)
                current_integer = current_integer*10 + int(symbol)
                integer_found = True
            except ValueError:
                if integer_found:
                    if negative:
                        current_integer = -current_integer
                    integers = integers + [current_integer]
                    current_integer = 0
                    integer_found = False
                negative = False
        return integers

    @staticmethod
    def newlines_to_strings(string, quiet=False):  # split long string with line
      # d breaks to separate strings in list
        if string:
            string = str(string)
            strings = string.split(newline2)
            if len(strings) == 1:
                strings = strings[0].split(newline)
            return strings
        else:
            raise TypeError("None can't be splitted")

    @classmethod
    def nl(cls, string):  # alias to newline
        return cls.newlines_to_strings(string=string)

    @staticmethod
    def split_every(string, chars):  # split string every
        import re
        chars = int(chars)
        output_lines = []
        char_exists = "."
        char_can_be_exists = ".?"
        regexp = char_exists + char_can_be_exists*(chars-1)
        for line in re.findall(regexp, str(string)):  # todo can I just return this list?
            output_lines += [line]
        return output_lines

    @staticmethod
    def leftpad(string, leng, ch="0", rightpad=False):  # return string with
      # d added characters to left side. If string longer — return original string
        string = str(string)
        if len(string) >= leng:
            return string
        strOfCh = str(ch) * leng
        string_output = strOfCh[len(string):leng] + string
        if rightpad:
            string_output = string + strOfCh[len(string):leng]
        return string_output

    @classmethod
    def rightpad(cls, string, leng, ch="0"):  # return string with added
      # d characters to right side. If string longer — return original string
        return cls.leftpad(string, leng, ch=ch, rightpad=True)

    @staticmethod
    def substring(string, before, after=None, return_after_substring=False):  # return
      # d string that between "before", and "after" strings, not including
      # d those. If "return_after_substring", return typle with substring and
      # d part of string after it.
        startfrom = string.find(before)
        if startfrom != -1:
            startfrom = string.find(before) + len(before)
        else:
            startfrom = 0
        if (after) or (after == ""):
            end_at = string[startfrom:].find(after)
            if end_at != -1:
                end_at = startfrom + string[startfrom:].find(after)
                substring = string[startfrom:end_at]
                after_substring = string[end_at:]
            else:
                substring = string[startfrom:]
                after_substring = ""
        else:
            substring = string[startfrom:]
        if return_after_substring:
            #try:
            #    after_substring
            #except UnboundLocalError:
            #    Print.debug("string", string,
            #                "before", before,
            #                "after", after,
            #                "return_after_substring", return_after_substring,
            #                "substring", substring,
            #                "after_substring", "UnboundLocalError: local variable 'after_substring' referenced before assignment")
            return substring, after_substring
        return substring

    @staticmethod
    def diff_simple(string_a, string_b):  # d print all symbol differents.
      # d Not all mine code, must rewrite.
      # todo rewrite this shit.
        import difflib

        strings = [(string_a, string_b)]  # for furthurer support for unlimited srtings

        for a, b in strings:
            print('{} => {}'.format(a, b))
            for i, s in enumerate(difflib.ndiff(a, b)):
                if s[0] == ' ':
                    continue
                elif s[0] == '-':
                    print(u'Delete "{}" from position {}'.format(s[-1], i))
                elif s[0] == '+':
                    print(u'Add "{}" to position {}'.format(s[-1], i))
            print()

    @staticmethod
    def input_pass(string="Password:"):  # d return string from user, securely
      # d inputed by getpass library
        import getpass
        return getpass.getpass(string)

    @staticmethod
    def input_int(message="Input integer: ", minimum=None, maximum=None, default=None, quiet=False):
      # d return integer from user with multible parameters.
        output_int = "jabla fitta"
        if default:
            message = "(Enter = " + str(default) + ")"
        while output_int == "jabla fitta":  # цикл, пока не получит итоговое число
            integer = input(message)
            if integer != "":
                try:
                    integer = Str.get_integers(integer)[0]
                except IndexError:
                    print("Это не число")
                    continue
            elif default and integer != "":
                output_int = default
            elif integer == "":
                print("Это не число")
                raise ValueError
            if minimum:
                if int < minimum:
                    print("Число должно быть больше", minimum)
                    raise ValueError
            if maximum:
                if int > maximum:
                    print("Число должно быть меньше", maximum)
                    raise ValueError
            output_int = integer
            break
        if not quiet:
            print("Итоговое число:", output_int)
        return output_int


    @classmethod
    def remove_spaces(Str, string_):
        return ' '.join(string_.split())  # at least, it's fast https://stackoverflow.com/questions/2077897/substitute-multiple-whitespace-with-single-whitespace-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

    @classmethod
    def get_words(Str, string_):
        return Str.remove_spaces(string_).split(" ")
