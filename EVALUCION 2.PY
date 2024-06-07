import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import pandas as pd

conn = sqlite3.connect('Sql_data/db_personas.db')
cursor= conn.cursor()

  
fig = plt.figure(figsize = (10, 10))
 
grafico ="""
SELECT personas.profesion as profesion,AVG(Salarios.Sueldo) as sueldo_promedio
from personas
INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios
GROUP BY personas.profesion
"""

consulta = """
SELECT * 
from personas
INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios


"""
cursor.execute(consulta)

df= pd.read_sql_query(consulta,conn)
print(df)


data = pd.read_sql(grafico, conn)
plt.bar(data.profesion,data.sueldo_promedio)
plt.title("sueldo promedio por profesion")
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.34)
plt.show()

conn.close()