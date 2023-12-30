#!/usr/bin/python3
"""Define una función J-SON a objeto"""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string."""
    return json.loads(my_str)
