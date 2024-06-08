import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import pandas as pd

conn = sqlite3.connect('Sql_data/db_personas.db')
cursor= conn.cursor()

  
fig = plt.figure(figsize = (10, 10))
 
graficoc="""
SELECT personas.nacionalidad as nacionalidad,count(personas.rut) as numero_de_profesionales
from personas
GROUP BY nacionalidad
"""
data = pd.read_sql(graficoc, conn)
plt.bar(data.nacionalidad,data.numero_de_profesionales)
plt.title("sueldo promedio por profesion")
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.34)
plt.show()

conn.close()