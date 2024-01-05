#!/usr/bin/python3
def magic_string():
    magic_string.xty = getattr(magic_string, 'xty', 0) + 1
    return ", ".join(["BestSchool" for z in range(magic_string.xty)])
