#!/usr/bin/python3
"""Defines Class zRectangle"""


class Rectangle:
    """Body of class rectsngle"""
    
    def __init__(self, width=0, height=0):
        """Initializing the class rectangle
        Arguments:
        height: stands for heigth of revtangle
        width: stands for width of rectangle
        Exception Error:
            TypeError: if size is not an integer
            ValurError: if size is les than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Obtains the attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the atrribute width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """obtains the attribute height"""
        return self-__height

    @height.setter
    def height(self, value):
        if value < 0:
            return ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value

    def area(self):
        """Calclates and returns area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """calculates and returns the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))
