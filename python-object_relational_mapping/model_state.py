#!/usr/bin/python3
# Define un modelo de Estado.
# Hereda de SQLAlchemy Base y se vincula a la tabla MySQL states.

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Representa un estado para una base de datos MySQL.

    __tablename__ (str): El nombre de la tabla MySQL para almacenar Estados.
    id (sqlalchemy.Integer): El id del estado.
    name (sqlalchemy.String): El nombre del estado.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
