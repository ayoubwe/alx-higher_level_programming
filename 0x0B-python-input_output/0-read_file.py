#!/usr/bin/python3
"""
It contains the read_file function
"""


def read_file(filename=""):
    """""It should reads a text file(UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
