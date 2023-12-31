#!/usr/bin/python3
"""
Define un modelo de estado que contiene la definición de la clase
 State y una instancia Base = declarative_base()
"""
from lib2to3.pytree import Base
from sre_parse import State
from unicodedata import name
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    Hereda de Base
    Se vincula a la tabla MySQL states
    Atributo de clase id que representa una columna
     de un entero único generado automáticamente, no puede
      ser nulo y es una clave primaria
    Atributo de clase name que representa una columna
     de una cadena con un máximo de 128 caracteres y
      no puede ser nulo
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
