#!/usr/bin/python3
"""Moudles contains function that adds argumsts to
python list"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_items.json")
    except FileNotFOundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_from_file(items, "add-items.json")
