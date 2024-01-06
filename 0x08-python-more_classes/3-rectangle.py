#!/usr/bin/python3
"""Defines A Class Rectange"""


class Rectangle:
    """Body of class Rectangle"""

    def __init__(self, width=0, height=0):
        """Inintializing the class rectangle
        Arguments:
        width :stands for the width of rectagle
        height: ssstands for height of rectanle
        Exception Error:
        TypeError: if size is not an integer
        ValueError: if size is less than zeero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """obtains width atributes"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the attributs of width"""
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """Obtains that attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value

    def area(self):
        """Extimates the area of a rectangle"""
        x = (self.__height * self.__width)
        return x

    def perimeter(self):
        """Returns the perimenter of rectangle"""
        if  self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__width *2) + (self.__height * 2))
    
    def __str__(self) -> str:
        """outputs diagram of rectangle defined for an obkject"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        obj = ""
        for x in range(self.__height):
            for y in range(self.__width):
                obj = obj + "#"
            if x < self.__height - 1:
                obj = obj + "\n"
        return (obj)
