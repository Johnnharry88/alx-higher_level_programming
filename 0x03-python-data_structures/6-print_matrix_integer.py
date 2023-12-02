#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    a = len(matrix)
    
    for x in range(a):
        b = len(matrix[x])
        for y in range(b):
            print("{:d}".format(matrix[x][y]), end=" ")
        print ("")
