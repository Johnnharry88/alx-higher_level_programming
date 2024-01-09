#!/usr/bin/python3
"""Module that contains a function that apppends a file"""


def append_write(filename="", text=""):
    """Function appends file exits otherwise creats a new text file"""
    with open(filename, "a", encoding="utf-8") as j:
        keep = j.write(text)
        return keep
