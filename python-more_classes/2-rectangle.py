#!/usr/bin/python3
"""Define clase Rectangle."""


class Rectangle:
    """Representa rectangle."""

    def __init__(self, width=0, height=0):
        """Inicializa Rectangle.

        Args:
            width (int): el ancho de rectangle.
            height (int): el alto de rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set el ancho Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("El ancho debe ser int")
        if value < 0:
            raise ValueError("El ancho debe ser >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set el alto de Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("el alto debe ser un int")
        if value < 0:
            raise ValueError("el alto debe ser >= 0")
        self.__height = value

    def area(self):
        """Retorna el area de Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Retorna el perímetro de Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
