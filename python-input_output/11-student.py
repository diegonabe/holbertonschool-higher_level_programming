#!/usr/bin/python3
"""Define una clase Student (Estudiante)."""


class Student:
    """Representa a un estudiante."""

    def __init__(self, first_name, last_name, age):
        """Inicializa un nuevo objeto Student (Estudiante).

        Args:
            first_name (str): El primer nombre del estudiante.
            last_name (str): El apellido del estudiante.
            age (int): La edad del estudiante.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Obtiene una representación de diccionario del Student (Estudiante).

        Si attrs es una lista de cadenas, representa solo esos atributos
        incluidos en la lista.

        Args:
            attrs (list): (Opcional) Los atributos a representar.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Reemplaza todos los atributos del Student (Estudiante).

        Args:
            json (dict): Los pares clave/valor para reemplazar atributos.
        """
        for k, v in json.items():
            setattr(self, k, v)
