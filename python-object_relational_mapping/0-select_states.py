#!/usr/bin/python3
#Lists all states from the database hbtn_0e_0_usa.
import MySQLdb
import sys

def list_states(username, password, db_name):
    # Conectar a la base de datos
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Crear un objeto cursor
    cursor = db.cursor()

    # Ejecutar la consulta SQL
    query = "SELECT * FROM states ORDER BY states.id;"
    cursor.execute(query)

    # Obtener y mostrar los resultados
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Cerrar la conexión
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Verificar si se proporcionaron los argumentos necesarios
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    # Obtener los argumentos
    username, password, db_name = sys.argv[1:]

    # Llamar a la función para listar estados
    list_states(username, password, db_name)

