#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Body of derived Class using BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a new rectangle"""
        
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """retruns the string representation of a rectangle"""
        xty = "[" + str(self.__class__.__name__) + "]"
        xty = xty + str(self.__width) + "/" + str(self.__height)
        return xty
