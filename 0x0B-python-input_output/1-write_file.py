#!/usr/bin/python3
"""
It contains the function "wrtie_file"
"""


def write_file(filename="", text=""):
    """It returns the number of chars written to "filename" from "text" """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
