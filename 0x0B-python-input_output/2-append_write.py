#!/usr/bin/python3
"""
It contains the append_write function
"""


def append_write(filename="", text=""):
    """It should returns the number of chars appended"""
    with open(filename, 'a', encoding='utf=8') as f
        return f.write(text)
