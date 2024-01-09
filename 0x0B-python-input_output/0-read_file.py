#!/usr/bin/python3
""""Module contains a function that reads atext file """


def read_file(filename=""):
    """Displays the content of textfile"""
    with open(filename, encoding="utf-8") as x:
        print(x.read(), end="")
