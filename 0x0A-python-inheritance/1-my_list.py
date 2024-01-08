#!/usr/bin/python3
"""Defines inherited list class"""


class MyList(list):
    """Sorted printing for the built in list class"""
    def print_sorted(self):
        """Displays a list in ascending order"""
        print(sorted(self))
