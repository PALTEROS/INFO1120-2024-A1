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

df= pd.read_sql_query(cosulta,conn)
print(df)

conn.close()