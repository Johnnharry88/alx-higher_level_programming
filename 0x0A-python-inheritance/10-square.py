#!/usr/bin/python3
"""Defines Class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Body of Class square"""

    def __init__(self, size):
        """Attribts of Class Square:
        Arguments:
        size: Isze of square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
