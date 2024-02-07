#!/usr/bin/python3
"""
It contains the class BaseGeometry and subclass Rectangle
"""


class BaseGeometry:
    """The class with public instance methods area"""
    def area(self):
        """It raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """The validates that value if is an integer more than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """The representation of a rectangle"""
    def __init__(self, width, height):
        """The instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """the returns fo the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """the string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
