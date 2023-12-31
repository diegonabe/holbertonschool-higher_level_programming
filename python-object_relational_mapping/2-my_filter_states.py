#!/usr/bin/python3
""" Toma un argumento
    y muestra todos los valores
    en la tabla de estados de
    hbtn_0e_0_usa donde el nombre coincide con el argumento
     Uso: ./2-my_filter_states.py <nombre de usuario de MySQL>
                                    <contraseña de MySQL>
                                    <nombre de la base de datos>
                                    <nombre del estado a buscar>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM states
                WHERE name LIKE BINARY '{}'
                ORDER BY states.id ASC""".format(sys.argv[4]).strip("'"))
    [print(state) for state in c.fetchall()]
