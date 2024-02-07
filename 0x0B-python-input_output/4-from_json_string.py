#!/usr/bin/python3
"""
It contains the from_json_string function
"""

import json


def from_json_string(my_str):
    """It should returns an object represented by a JSON string"""
    return json.loads(my_str)
