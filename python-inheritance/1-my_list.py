#!/usr/bin/python3
"""Define una clase heredada"""


class MyList(list):
    """Implementa la función print_sorted"""

    def print_sorted(self):
        """Imprime la lista en orden ascendente"""
        print(sorted(self))
