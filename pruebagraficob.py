import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import pandas as pd

conn = sqlite3.connect('Sql_data/db_personas.db')
cursor= conn.cursor()

  
fig = plt.figure(figsize = (10, 10))
 
graficob="""
SELECT personas.profesion as profesion,
round(COUNT(rut) * 100 / (SELECT COUNT(profesion) FROM personas)) AS porcentaje
from personas
GROUP BY profesion
"""

fig, ax = plt.subplots()
data = pd.read_sql(graficob, conn)
ax.pie(data.porcentaje,labels=data.profesion, autopct='%1.1f%%')
plt.title("sueldo promedio por profesion")
plt.show()

conn.close()