#!/usr/bin/python3
def weight_average(my_list=[]):
    y = len(my_list)
    if not isinstance(my_list, list) or y == 0:
        return 0
    else:
        alx = 0
        xty = 0
        for x in my_list:
            alx = alx + (x[0] * x[1])
            xty = xty + (x[1])
            ans = alx / xty
        return ans
