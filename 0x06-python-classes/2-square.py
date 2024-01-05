#!/usr/bin/python3
""" Module that defines class Square"""


class Square:
    """Body of Class Square"""
    def __init__(self, size=0):
        """Initializes class Square
        Size: the size of square of int
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
