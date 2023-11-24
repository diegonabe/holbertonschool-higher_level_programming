#!/usr/bin/python3
"""Define la función lookup"""


def lookup(obj):
    """Retorna una lista de los atributos disponibles de obj"""
    return (dir(obj))
