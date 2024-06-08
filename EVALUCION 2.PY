import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import pandas as pd

conn = sqlite3.connect('Sql_data/db_personas.db')
cursor= conn.cursor()

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
"""
  
grafico_c="""
SELECT personas.nacionalidad as nacionalidad,count(personas.rut) as numero_de_profesionales
from personas
GROUP BY nacionalidad
"""



plt.subplots()
data = pd.read_sql(grafico_a, conn)
plt.bar(data.profesion,data.sueldo_promedio)
plt.title("sueldo promedio por profesion")
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.35)


plt.subplots()
data = pd.read_sql(grafico_b, conn)
plt.pie(data.porcentaje,labels=data.profesion, autopct='%1.1f%%')
plt.title("distribuicion de profesiones")

plt.subplots()
data = pd.read_sql(grafico_c, conn)
plt.bar(data.nacionalidad,data.numero_de_profesionales)
plt.title("conteo de profesionales por nacionalidad")
plt.xticks(rotation=45)

plt.show()

conn.close()