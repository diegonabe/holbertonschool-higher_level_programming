#!/usr/bin/python3
"""Define la clase Student"""


class Student:
    """Representa Student"""
    def __init__(self, first_name, last_name, age):
        """Inicializa Student
        Args:
            first_name(str): El primer nombre de Student.
            last_name(str): El apellido de Student.
            age (int): La edad de Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Obtiene una representación en dict de Student"""
        return self.__dict__

