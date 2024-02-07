#!/usr/bin/python3
"""
It contains the class MyInt
"""


class MyInt(int):
    """ The rebel version of an integer"""
    def __new__(cls, *args, **kwargs):
        """create a new instance"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is now !="""
        return int(self) == other
