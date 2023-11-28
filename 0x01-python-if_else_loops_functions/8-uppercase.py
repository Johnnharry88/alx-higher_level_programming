#!/usr/bin/python3
def uppercase(str):
    for convert in str:
        if ord(convert) >= ord('a') and ord(convert) <= ord('z'):
            hold = chr(ord(convert) - 32)
        else:
            hold = convert
        print("{:s}".format(hold), end="")
    print()

