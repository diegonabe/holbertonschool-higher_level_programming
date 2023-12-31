#!/usr/bin/python3
"""
muestra todos los valores en la tabla de estados de
 hbtn_0e_0_usa donde el nombre coincide con el argumento
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM states""")
    [print(state) for state in c.fetchall() if state[1] == sys.argv[4]]
