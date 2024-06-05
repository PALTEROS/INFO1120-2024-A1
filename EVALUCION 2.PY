import sqlite3
import pandas as pd


conn = sqlite3.connect('Sql_data/db_personas.db')
cursor= conn.cursor()

cosulta = """
SELECT * 
from personas
INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios
"""
cursor.execute(cosulta)
rows = cursor.fetchall()

for row in rows:
    print(row)

DataFrame= pd.read_sql_query(cosulta,conn)
print(DataFrame)

filtro = int(input('Que tipo de Busqueda deseas realizar: '))
print('1. Busqueda singular (1 persona)')
print('2. Busuqeda por grupos (Varias personas)')

conn.close()