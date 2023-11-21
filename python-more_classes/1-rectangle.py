#!/usr/bin/python3
"""Defines la clase Rectangle"""


class Rectangle:
    """Representa rectangle."""

    def __init__(self, width=0, height=0):
        """Inicializa Rectangle.

        Args:
            width (int): El ancho de rectangle.
            height (int): La altura de rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Obtiene el ancho de rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width debe ser int")
        if value < 0:
            raise ValueError("width debe ser >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set el ancho de rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height debe ser int")
        if value < 0:
            raise ValueError("height debe ser >= 0")
        self.__height = value
