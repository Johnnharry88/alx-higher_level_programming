#!/usr/bin/python3
"""Module defines a function that reads JSON file"""
import json


def load_from_json_file(filename):
    """Creats a python object from a JSON string file"""
    with open(filename) as x:
        xty = json.load(x)
        return xty
