#!/usr/bin/python3
"""Defined a function that adds attributes to object"""


def add_attribute(obj, att, value):
    """Adds new attribute to obj"""

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setatttr(obj, att, value)
