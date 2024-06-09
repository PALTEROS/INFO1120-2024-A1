import matplotlib.pyplot as plt
import numpy as np
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

DataFrame= pd.read_sql_query(cosulta,conn)
print(DataFrame)

grafico_a ="""
SELECT personas.profesion as profesion,AVG(Salarios.Sueldo) as sueldo_promedio
from personas
INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios
GROUP BY profesion
"""
grafico_b="""
SELECT personas.profesion as profesion,
round(COUNT(rut) * 100 / (SELECT COUNT(profesion) FROM personas)) AS porcentaje
from personas
GROUP BY profesion
ORDER BY porcentaje
"""
  
grafico_c="""
SELECT personas.nacionalidad as nacionalidad,count(personas.rut) as numero_de_profesionales
from personas
GROUP BY nacionalidad
ORDER BY numero_de_profesionales DESC
"""



plt.subplots()
data_a = pd.read_sql(grafico_a, conn)
plt.bar(data_a.profesion,data_a.sueldo_promedio, color = "skyblue")
plt.title("sueldo promedio por profesion")
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.35)
plt.grid(True,linestyle=":")

plt.subplots()
data_b = pd.read_sql(grafico_b, conn)
plt.pie(data_b.porcentaje,labels=data_b.profesion, autopct='%1.1f%%')
plt.title("distribuicion de profesiones")


plt.subplots()
data_c = pd.read_sql(grafico_c, conn)
plt.bar(data_c.nacionalidad, data_c.numero_de_profesionales, color="skyblue")
plt.title("conteo de profesionales por nacionalidad")
plt.xticks(rotation=45)
plt.grid(True,linestyle=":")

plt.show()

conn.close()