#!/usr/bin/python3
"""A Class Square"""


class Square:
    """Body of class square"""

    def __init__(self, size=0):
        """Initializing class square
        Size: size of class of integer type
        Exception Error:
            TypeError: if size is not integer
            ValueError: if is less tham zero
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Gess that size of square"""

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
        Estimates tha area of square
        Return: Square raised to power of 2
        """

        return (self.__size ** 2)

    def my_print(self):
        """prints out the square in #"""

        if self.__size == 0:
            print()
        for x in range(self.__size):
            print("#" * self.__size)
