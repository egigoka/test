#!/usr/bin/env python3
# Copyright (c) 2008 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import os


YES = frozenset({"y", "Y", "yes", "Yes", "YES"})


def main():
    dirty = False
    items = []

    filename, items = choose_file()
    if not filename:
        print("Cancelled")
        return

    while True:
        print("\nList Keeper\n")
        print_list(items)
        choice = get_choice(items, dirty)

        if choice in "Aa":
            dirty = add_item(items, dirty)
        elif choice in "Dd":
            dirty = delete_item(items, dirty)
        elif choice in "Ss":
            dirty = save_list(filename, items)
        elif choice in "Qq":
            if (dirty and (get_string("Save unsaved changes (y/n)",
                                      "yes/no", "y") in YES)):
                save_list(filename, items, True)
            break


def choose_file():
    enter_filename = False
    print("\nList Keeper\n")
    files = [x for x in os.listdir(".") if x.endswith(".list_")]
    if not files:
        enter_filename = True
    if not enter_filename:
        print_list(files)
        index = get_integer("Specify file's number (or 0 to create "
                            "a new one)", "number", maximum=len(files),
                            allow_zero=True)
        if index == 0:
            enter_filename = True
        else:
            filename = files[index - 1]
            items = load_list(filename)
    if enter_filename:
        filename = get_string("Choose filename", "filename")
        if not filename.endswith(".list_"):
            filename += ".list_"
        items = []
    return filename, items



def print_list(items):
    if not items:
        print("-- no items are in the list_ --")
    else:
        width = 1 if len(items) < 10 else 2 if len(items) < 100 else 3
        for i, item in enumerate(items):
            print("{0:{1}}: {2}".format(i + 1, width, item))
    print()


def get_choice(items, dirty):
    while True:
        if items:
            if dirty:
                menu = "[A]dd  [D]elete  [S]ave  [Q]uit"
                valid_choices = "AaDdSsQq"
            else:
                menu = "[A]dd  [D]elete  [Q]uit"
                valid_choices = "AaDdQq"
        else:
            menu = "[A]dd  [Q]uit"
            valid_choices = "AaQq"
        choice = get_string(menu, "choice", "a")

        if choice not in valid_choices:
            print("ERROR: invalid choice--enter one of '{0}'".format(
                  valid_choices))
            input("Press Enter to continue...")
        else:
            return choice


def add_item(items, dirty):
    item = get_string("Add item", "item")
    if item:
        items.append(item)
        items.sort(key=str.lower)
        return True
    return dirty


def delete_item(items, dirty):
    index = get_integer("Delete item number (or 0 to cancel)",
                        "number", maximum=len(items),
                        allow_zero=True)
    if index != 0:
        del items[index - 1]
        return True
    return dirty


def load_list(filename):
    items = []
    fh = None
    try:
        for line in open(filename, encoding="utf8"):
            items.append(line.rstrip())
    except EnvironmentError as err:
        print("ERROR: failed to load {0}: {1}".format(filename, err))
        return []
    finally:
        if fh is not None:
            fh.close()
    return items


def save_list(filename, items, terminating=False):
    fh = None
    try:
        fh = open(filename, "w", encoding="utf8")
        fh.write("\n".join(items))
        fh.write("\n")
    except EnvironmentError as err:
        print("ERROR: failed to save {0}: {1}".format(filename, err))
        return True
    else:
        print("Saved {0} item{1} to {2}".format(len(items),
              ("s" if len(items) != 1 else ""), filename))
        if not terminating:
            input("Press Enter to continue...")
        return False
    finally:
        if fh is not None:
            fh.close()


def get_string(message, name="string", default=None,
               minimum_length=0, maximum_length=80):
    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line:
                if default is not None:
                    return default
                if minimum_length == 0:
                    return ""
                else:
                    raise ValueError("{0} may not be empty".format(
                                     name))
            if not (minimum_length <= len(line) <= maximum_length):
                raise ValueError("{0} must have at least {1} and "
                        "at most {2} characters".format(
                        name, minimum_length, maximum_length))
            return line
        except ValueError as err:
            print("ERROR", err)


def get_integer(message, name="integer", default=None, minimum=0,
                maximum=100, allow_zero=True):

    class RangeError(Exception): pass

    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            i = int(line)
            if i == 0:
                if allow_zero:
                    return i
                else:
                    raise RangeError("{0} may not be 0".format(name))
            if not (minimum <= i <= maximum):
                raise RangeError("{0} must be between {1} and {2} "
                        "inclusive{3}".format(name, minimum, maximum,
                        (" (or 0)" if allow_zero else "")))
            return i
        except RangeError as err:
            print("ERROR", err)
        except ValueError as err:
            print("ERROR {0} must be an integer".format(name))


main()
