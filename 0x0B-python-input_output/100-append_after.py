#!/usr/bin/python3
"""Defines a text-file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string"""
    with open(filename, mode="r+", encoding="utf-8") as x:
        text = ""
        for line in x:
            text = text + line
            if search_string in line:
                text = text + new_string
        x.seek(0)
        x.write(text)
