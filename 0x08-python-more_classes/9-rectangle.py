#!/usr/bin/python3
"""Defines a Class Rectangle"""


class Rectangle:
    """Body of class Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
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
                try:
                    obj = obj + str(self.print_symbol)
                except Exception:
                    obj = obj + type(self).print_symbol
            if x < self.__height - 1:
                obj = obj + "\n"
        return (obj)

    def __repr__(self):
        """Retunrs the string representation of rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """displays message for deleted objects"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return (Rectangle(size, size))
