#!/usr/bin/python3
"""Define una función string-to-JSON."""
import json


def to_json_string(my_obj):
    """Retorna la  JSON de un objeto tipo string."""
    return json.dumps(my_obj)
