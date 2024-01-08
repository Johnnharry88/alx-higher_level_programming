#!/usr/bin/python3
"""Defined method that check the nstance of an object"""


def is_same_class(obj, a_class):
    """Checks whetheer an object is instance ot not
    Arguments:
        obj: the object to be checked
        a_class: the class tp match with
    Return:
        Trueni if object is an instance else false
    """
    if type(obj) == a_class:
        return True
    else:
        return False
