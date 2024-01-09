#!/usr/bin/python3
"""Module defines class-Json function"""


def class_to_json(obj):
    """Returns a dictionary of data struture"""
    return obj.__dict__
