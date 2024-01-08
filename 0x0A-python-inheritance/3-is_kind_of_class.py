#!/usr/bin/python3
"""Defied class and inherits class-checking function"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance ot an inheritd class
    Arguments:
        obj: object ot be checked.
        a_class: clas to check out
    Returns:
        True, if an object is an instance otherwise, False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
