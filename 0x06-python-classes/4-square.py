#!/usr/bin/python3
"""Defines a Clas Square"""


class Square:
    """Body of Class Square"""

    def __init__(self, size=0):
        """Initializing the class square
        Size: size of the square defined
        Exception Error:
        TypeError: if size is not an integer
        ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        """Gets the size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Estimates the area of the square
        Return: square of size
        """

        return (self.__size ** 2)
