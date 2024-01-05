#!/usr/bin/python3
"""CDefining Class Square"""


class Square:
    """Body of class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes clas Square
        Size: length of s side of a square
        Positon: Postion of Square to be defined

        """
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """The property of the lengthofthe side of a square
        Exception Error:
        TypeError: if size is not integer
        ValueError: if size is less than 0
        """

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >=0 0')
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """Initializes the position of Square
        Value: value of tuple of two psotitive integers
        Exception Error:
            TypeError: if value is not a tuple or integer in tuple
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('postion must be a tuple of 2 positive integers')
        if len([x for x in value if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """calculate the area of a Square
        Returns: vlaue of area Calculated
        """

        return (self.__size ** 2)

    def dis_position(self):
        """Returns the position in space"""

        xty = ""
        if self.size == 0:
            return "\n"
        for a in range(self.position[1]):
            xty = xty + "\n"
        for a in range(self.size):
            for x in range(self.position[0]):
                xty = xty + " "
            for y in range(self.size):
                xty = xty + "#"
            xty = xty + "\n"
        return xty

    def my_print(self):
        """Displays the square in position to standard output"""

        `print(self.dis_position(), end="")
