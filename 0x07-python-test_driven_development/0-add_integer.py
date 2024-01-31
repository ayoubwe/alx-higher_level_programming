#!/usr/bin/python3
"""
This is my module of "0-add_integer".
This module supplies one function add_integer(a, b).
"""


def add_integer(a, b):
    """Return two numbers."""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer #number")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer #number")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
