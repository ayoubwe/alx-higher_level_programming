#!/usr/bin/python3
"""
It contains the inherits_from function
"""


def inherits_from(obj, a_class):
    """returns true if obj, otherwise returns false"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
