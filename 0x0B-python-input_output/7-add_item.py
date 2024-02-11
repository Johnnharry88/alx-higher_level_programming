#!/usr/bin/python3
"""Function to save and load"""

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_items.json'

try:
    json_list = load_from_json_file(filename)
except:
    json_list = []
    for x in argv[1:]:
        json_list.append(x)

    save_to_json_file(json_list, filename)
