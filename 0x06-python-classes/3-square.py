#!/usr/bin/python3
"""Defines a  class Square"""


class Square:
    """Body of class Square"""

    def __init__(self, size=0):
        """Initializing the class Square
        Size: size of class square
        Error Exception:
            TypeError: if size is not integer
            ValueEror: if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >=0')
        self.__size = size

    def area(self):
        return (self.__size ** 2)
