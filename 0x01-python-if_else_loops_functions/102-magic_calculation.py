#!/usr/bin/python3
def magic_clacuation(a, b, c):
    if a < b:
        return c
    elif b < c:
        return a + b
    return (a * b) - c

