#!/usr/bin/python3
def upper(str):
    for convert in str:
        if ord(convert) >= ord('a') and ord(convert) <= ord('z'):
            convert = chr(ord(convert) - (30 + 2))
        print("{:s}".format(convert), end="")
        print()
