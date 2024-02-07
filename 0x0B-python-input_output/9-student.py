#!/usr/bin/python3
"""
It contains the class "Student" founction
"""


class Student:
    """first representation of a student"""
    def __init__(self, first_name, last_name, age):
        """secound initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """it should returns a dictionary representation of a Student"""
        return self.__dict__
