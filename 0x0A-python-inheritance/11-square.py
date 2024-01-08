#!/usr/bin/python3
"""Defines a rectangle sub class square"""
Rectangle = __import__('9-rectangle').Rectangle


class square(Rectangle):
    """Body of Class Square"""

    def __init__(self, size):
        """Initializes a new aquare"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
