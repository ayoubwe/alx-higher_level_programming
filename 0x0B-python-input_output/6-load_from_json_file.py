#!/usr/bin/python3
"""
It contains the load_from_json_file function
"""

import json


def load_from_json_file(filename):
    """It creates an object from "JSON file" """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
