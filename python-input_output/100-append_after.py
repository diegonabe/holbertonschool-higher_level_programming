#!/usr/bin/python3
"""Función para insertar texto en una fila"""


def append_after(filename="", search_string="", new_string=""):
    """Inserta texto después de cada línea
    que contiene una cadena específica en un archivo.

    Args:
        filename (str): El nombre del archivo.
        search_string (str): La cadena a buscar dentro del archivo.
        new_string (str): La cadena a insertar.
    """
    texto = ""
    with open(filename) as r:
        for linea in r:
            texto += linea
            if search_string in linea:
                texto += new_string
    with open(filename, "w") as w:
        w.write(texto)
