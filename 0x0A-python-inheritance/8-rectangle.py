#!/usr/bin/python3
"""Define a derived Class taking from Base Geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeomery


class Rectangle(BaseGeometry):
    """Bpdy of Derived Class"""

    def __init__(self, width, height):
        """iniitalize a Rectangle.
        Arguments:
            width: width of rectangle
            height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
