#!/usr/bin/python3
"""Module defines Pascal Triangle function"""


def pascal_triangle(n):
    """Body of Function of size n"""
    if n <= 0:
        return []

    xty = [[1]]
    while len(xty) != n:
        x = xty[-1]
        ram = [1]
        for j in range(len(x) - 1):
            ram.append(x[j] + x[j + 1])
        ram.append(1)
        xty.append(ram)
    return xty
