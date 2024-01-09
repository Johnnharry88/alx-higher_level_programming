#!/usr/bin/python3
"""Module contains JAON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """Retunrs a text file written suing Json model"""
    with open(filename, "w") as x:
        a = json.dump(my_obj, x)
        return a
