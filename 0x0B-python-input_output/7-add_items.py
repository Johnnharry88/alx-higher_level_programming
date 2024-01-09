#!/usr/bin/python3
"""Function to save and load"""

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_items.json'
my_list = []
try:
    my_list = load_from_json_file(filename)
except Exception:
    save_to_json_file(my_list, filename)

arglen = len(argv)
if arglen > 1:
    for x in range(1, arglen):
        my_list.append(argv[x])
    save_to_json_file(my_list, filename)
