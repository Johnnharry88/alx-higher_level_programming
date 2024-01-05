#!/usr/bin/python3
"""Defines a Locked class"""


class LockedClass:
    """
    Only allws an instane of attribute called first_name
    """

    __slots__ = ["first_name"]
