#!/usr/bin/python3
"""Defines a baseGeometry Class"""


class BaseGeometry:
    """ Defined the bdy of class Base Geometry"""
    def area(self):
        """IMehtod not implemenented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if value is an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < = 0:
            raise ValueError("{} must be greater than 0".format(name))
