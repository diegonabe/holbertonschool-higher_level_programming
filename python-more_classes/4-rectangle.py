#!/usr/bin/python3
"""Define class Rectangle."""


class Rectangle:
    """Representa rectangle."""

    def __init__(self, width=0, height=0):
        """Inicializa Rectangle.

        Args:
            width (int): El ancho de rectangle.
            height (int): El alto de rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set el ancho de Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width debe ser integer")
        if value < 0:
            raise ValueError("width debe ser >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set el alto de Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height debe ser integer")
        if value < 0:
            raise ValueError("height debe ser >= 0")
        self.__height = value

    def area(self):
        """Retorna el área de Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Retorna el perímetro de Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Retorna la presentación impresa de Rectangle.

        Representa el rectángulo con el caracter #.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Retorna la representación string de Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
