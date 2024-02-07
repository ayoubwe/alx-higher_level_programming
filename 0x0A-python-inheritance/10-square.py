#!/usr/bin/python3
"""
It contains the class BaseGeometry and subclass rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The representation of a square"""
    def __init__(self, size):
        """the instantiation of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"It returns the area of the square"""
        return self.__size ** 2
