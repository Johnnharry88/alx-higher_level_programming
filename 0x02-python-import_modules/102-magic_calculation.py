#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        alx = add(a, b)
        for sch in range(4, 6):
            g = add(alx, sch)
        return g
    else:
        c = sub(a, b)
        return c
