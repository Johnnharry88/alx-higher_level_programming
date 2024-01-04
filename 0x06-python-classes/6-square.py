#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
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
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('postion must be a tuple of 2 positive integers')
        if len([x for x in value if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        return (self.__size ** 2)

    def dis_position(self):
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
        print(self.dis_position(), end="")
