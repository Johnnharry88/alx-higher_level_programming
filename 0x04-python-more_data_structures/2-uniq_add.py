#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    alx = set(my_list)
    for a in alx:
        res = res + a
    return (res)
