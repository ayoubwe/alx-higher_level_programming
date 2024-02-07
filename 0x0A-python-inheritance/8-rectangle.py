#!/usr/bin/python3
"""
It contains the class BaseGeometry and subclass rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The representation of a rectangle"""
    def __init__(self, width, height):
        """The instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
