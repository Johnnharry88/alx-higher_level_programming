#!/usr/bin/python3
def max_integer(my_list=[]):
    a = len(my_list)
    if a == 0:
        return None
    peak = my_list[0]
    for x in range(a):
        if my_list[x] > peak:
            peak = my_list[x]
    return peak
