#!/usr/bin/python3
"""Moudles contaisn a file-writting function"""


def write_file(filename="", text=""):
    """writes a string fomrat in utf-e encoding """
    with open(filename, "w", encoding="utf-8") as a:
        return a.write(text)
