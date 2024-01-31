#!/usr/bin/python3
"""
This is my module of "3-say_my-name".
This 3-say_my_name  module supplies one function, say_my_name as breakin bad tv-show.
"""


def say_my_name(first_name, last_name=""):
    """Say my name 
    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
        """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
