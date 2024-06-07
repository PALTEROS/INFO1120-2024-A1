import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import pandas as pd

conn = sqlite3.connect('Sql_data/db_personas.db')
cursor= conn.cursor()

  
fig = plt.figure(figsize = (10, 5))
 
grafico = """
SELECT personas.profesion as profesion,AVG(Salarios.Sueldo) as sueldo_promedio
from personas
INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios
GROUP BY personas.profesion
order by sueldo_promedio"""

consulta = """
SELECT * 
from personas
INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios


"""
cursor.execute(consulta)

df= pd.read_sql_query(consulta,conn)
print(df)


data = pd.read_sql(ñ, conn)
plt.bar(data.profesion,data.sueldo_promedio)
plt.title("Students enrolled in different courses")
plt.show()
conn.close()