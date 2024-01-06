#!/usr/bin/python3
"""Defines a Class Rectangle"""


class Rectangle:
    """Body of class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing the class rectangle
        Arguments:
        width: stands for the width of the rectangle
        height: stands for the rectangle height
        Error flag:
        TypeError: if size is not an integer
        Valueerror: if size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Obtains the width attributes"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the attributes of the width"""
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        self.__width = value

    @property
    def height(self):
        """Gets the height atributes"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height attributes"""
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("widht must be an integer")
        self.__height = value

    def area(self):
        """Calculates and returns area of rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Calculates and retunrs the perimeter of rectangle"""
        if slef.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """Displays the perimeter of the rectangle with special characters"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        obj = ""
        for x in range(self.__height):
            for y in range(self.__width):
                obj = obj + "#"
            if x < self.__height - 1:
                obj = obj + "\n"
        return (obj)

    def __repr__(self):
        """Returns string representation of rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
