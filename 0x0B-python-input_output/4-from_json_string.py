#!/usr/bin/python3
"""Module holds Json function"""
import json


def from_json_string(my_str):
    """Function returns Python object representatio  of JSON sting"""
    xty = json.loads(my_str)
    return xty
