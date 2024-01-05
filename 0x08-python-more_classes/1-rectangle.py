#!/usr/bin/python3
"""Defines Class Rectangle"""


class Rectangle:
    """Body of class Rechtangle"""
    def __init__(self, width=0, height=0):
        """"Initializing the class Rectangle
        Args:
        width: width of th rectangle
        height: holding height of rectangle
        Exception Error:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retirieves attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves attribute of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets attributes of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
