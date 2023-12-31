#!/usr/bin/python3
""" Filtra states y crea una lista con los que empiezan con N (upper N)
 de la database hbtn_0e_0_usa
 Uso: ./1-filter_states.py <mysql username>
                            <mysql password>
                            <database name>"""

import sys
from unicodedata import name
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]