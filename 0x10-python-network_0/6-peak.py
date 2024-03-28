#!/usr/bin/python3
""" finds a peak in a list of unsored integers"""


def find_peak(list_of_integers):
    """Returns Peak of list_of _integers)"""
    x = len(list_of_integers)
    n_x = x
    mid_x = x // 2

    if x == 0:
        return None

    while True:
        n_x = n_x // 2
        if (mid_x < x - 1 and
                list_of_integers[mid_x] < list_of_integers[mid_x + 1]):
            if n_x // 2 == 0:
                n_x = 2
            mid_x = mid_x + n_x // 2
        elif n_x > 0 and list_of_integers[mid_x] < list_of_integers[mid_x - 1]:
            if n_x // 2 == 0:
                n_x = 2
            mid_x = mid_x - n_x // 2
        else:
            return list_of_integers[mid_x]
