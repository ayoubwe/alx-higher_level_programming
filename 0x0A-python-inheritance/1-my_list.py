#!/usr/bin/python3
"""
The conten of MyList class
"""


class MyList(list):
    """The subclass of list"""
    def __init__(self):
        """initializes"""
        super().__init__()

    def print_sorted(self):
        """the sorted list"""
        print(sorted(self))
