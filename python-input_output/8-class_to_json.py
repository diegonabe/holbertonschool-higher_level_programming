#!/usr/bin/python3
"""Define una función de Python Class-to-JSON"""


def class_to_json(obj):
    """Retorna una representación en diccionario de una simple estructura de datos"""
    return obj.__dict__
