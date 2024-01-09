#!/usr/bin/python3
"""Module defines a function that converts lists and dict to strngs
using json model"""
import json


def to_json_string(my_obj):
    """Returns the string representation using
    json model of list and dict"""
    j = json.dumps(my_obj)
    return j
