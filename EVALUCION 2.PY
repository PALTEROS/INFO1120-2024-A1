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
"""
  
grafico_c="""
SELECT personas.nacionalidad as nacionalidad,count(personas.rut) as numero_de_profesionales
from personas
GROUP BY nacionalidad
"""

def BusquedaSing(conn):
    while True:
        print('Desea realizar una busqueda por:')
        print('1. Rut')
        print('2. Nombre Completo')
        eleccion = int(input('Por favor ingrese el numero de su seleccion: '))

        if eleccion == 1:
            rut = str(input('Ingrese el rut de la persona: '))
            query = f"SELECT * FROM personas INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios WHERE personas.rut = ?"
            res = pd.read_sql_query(query, conn,params=(rut,))
            print(res)
            break
        elif eleccion == 2:
            nombre = str(input('Ingrese el Nombre completo de la persona: '))
            query = f"SELECT * FROM personas INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios WHERE personas.nombre_completo = ?"
            res = pd.read_sql_query(query, conn,params=(nombre,))
            print(res)
            break

def BusquedaGrup(conn):
    while True:
        print('Desea realizar una busqueda por: ')
        print('1.Sueldo' "\n" '2.Rol' "\n" '3.Nacionalidad' "\n" '4.Profesion')
        eleccion = int(input('Ingrese el numero de su eleccion: '))

        if eleccion == 1:
            sueldo = int(input('Ingrese el sueldo de la persona: '))
            query = f'SELECT * FROM personas INNER JOIN Salarios ON persona.id_rol = Salarios.id_salarios WHERE Salarios.Sueldo = ?'
            res = pd.read_sql_query(query, conn,params=(sueldo,))
            print(res)
            break
        elif eleccion == 2:
            rol = str(input('Ingresa el rol de la persona: '))
            query =f'SELECT * FROM personas INNER JOIN Salarios ON persona.id_rol = Salarios.id_salarios WHERE Salarios.Rol = ?'
            res = pd.read_sql_query(query,conn,params=(rol,))
            print(res)
            break
        elif eleccion == 3:
            nacionalidad = str(input('Ingrese la nacionalidad de la persona: '))
            query = f"SELECT * FROM personas INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios WHERE personas.Nacionalidad = ?"
            res = pd.read_sql_query(query,conn, params=(nacionalidad,))
            print(res)
            break
        elif eleccion == 4:
            profesion = str(input('Ingresa la profesion de la persona: '))
            query = f'SELECT * FROM personas INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios WHERE personas.profesion = ?'
            res = pd.read_sql_query(query,conn,params=(profesion,))
            print(res)
            break
        else:
            print('Opcion no valida vuelva a intentar ')

def menu():
    while True:
        print('Que tipo de busqueda desea ralizar: ')
        print('1. Busqueda singla (1 persona)')
        print('2. Busqueda por grupo (Varias personas)')
        filtro = int(input('Ingresa el numero de tu eleccion: '))

        if filtro == 1:
            BusquedaSing(conn)
            break
        if filtro == 2:
            BusquedaGrup(conn)
            break
        else:
            print('opcion no valida vuelva a intentar')

menu()
#-------------------------------------------------------------------------------------------------
############################################
#las estadisticas se ponen despues de apretar todas las opciones asi que hay que ordenarlo bien
#por ahora lo voy a dejar todo comentado
#############################################
#plt.subplots()
#data = pd.read_sql(grafico_a, conn)
#plt.bar(data.profesion,data.sueldo_promedio)
#plt.title("sueldo promedio por profesion")
#plt.xticks(rotation=45)
#plt.subplots_adjust(bottom=0.35)


#plt.subplots()
#data = pd.read_sql(grafico_b, conn)
#plt.pie(data.porcentaje,labels=data.profesion, autopct='%1.1f%%')
#plt.title("distribuicion de profesiones")

#plt.subplots()
#data = pd.read_sql(grafico_c, conn)
#plt.bar(data.nacionalidad,data.numero_de_profesionales)
#plt.title("conteo de profesionales por nacionalidad")
#plt.xticks(rotation=45)

#plt.show()
#-----------------------------------------------------------------------------------------------------
conn.close()