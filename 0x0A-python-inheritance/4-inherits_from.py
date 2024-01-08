#!/usr/bin/python3
"""Defined an inherited class function"""


def inherits_from(obj, a_class):
    """Checks out if an object is na inherited instane  of a classL
    Arguments:
        obj: the object to be checked
        a_class: the class to check out for the object
    Returns:
        True if obj is inherited instnce otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        False
