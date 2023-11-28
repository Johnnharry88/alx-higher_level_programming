#!/usr/bin/python3
def uppercase(str):
    for convert in str:
        if ord(convert) >= ord('a') and ord(convert) <= ord('z'):
            convert = chr(ord(convert) - 32)
        print("{:s}".format(convert), end="")
    print()

