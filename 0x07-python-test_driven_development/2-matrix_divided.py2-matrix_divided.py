#!/usr/bin/python3
"""
My module of  2-matrix_divided supplies one function, matrix_divided.
"""


def matrix_divided(matrix, div):
    """Divides all elements by div"""
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix ")
    size = None
    for l in matrix:
        if type(l) is not list:
            raise TypeError(
                "matrix must be a matrix")
        if size is None:
            size = len(l)
        elif size != len(l):
            raise TypeError("Each row must have the same size")
        for i in l:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix  of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a a number or integer")
    if div == 0:
        raise ZeroDivisionError("division by 0")
    return [[round(i / div, 2) for i in l] for l in matrix]
