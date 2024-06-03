import sqlite3

conn = sqlite3.connect('Sql_data/db_personas.db')
cursor= conn.cursor()

cosulta = """
SELECT * from personas
INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios
"""
cursor.execute(cosulta)

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()