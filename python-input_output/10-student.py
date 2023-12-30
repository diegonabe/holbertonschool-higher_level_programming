#!/usr/bin/python3
"""Define Student."""


class Student:
    """Representa student."""

    def __init__(self, first_name, last_name, age):
        """Inicializa Student.

        Args:
            first_name (str): Nombre de student.
            last_name (str): Apellido de student.
            age (int): Edad de student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Obtiene una representación del diccionario de Student

        Si attrs es una lista de cadenas, representa solo esos atributos
        incluido en la lista.

        Argumentos:
            attrs (lista): (Opcional) Los atributos a representar.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
