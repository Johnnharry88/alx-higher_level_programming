#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    x = list(map((lambda row: list(map((lambda a: a ** 2), row))), matrix))
    return x
