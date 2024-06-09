import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import pandas as pd


conn = sqlite3.connect('Sql_data/db_personas.db')
cursor= conn.cursor()

grafico_a ="""
SELECT personas.profesion as profesion,AVG(Salarios.Sueldo) as sueldo_promedio from personas
INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios
GROUP BY profesion
"""
grafico_b="""
SELECT personas.profesion as profesion, round(COUNT(rut) * 100 / (SELECT COUNT(profesion) FROM personas)) AS porcentaje from personas
GROUP BY profesion
""" 
grafico_c="""
SELECT personas.nacionalidad as nacionalidad,count(personas.rut) as numero_de_profesionales from personas
GROUP BY nacionalidad
ORDER BY numero_de_profesionales DESC
"""

cosulta = """
SELECT * 
from personas
INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios
"""
cursor.execute(cosulta)
rows = cursor.fetchall()

DataFrame= pd.read_sql_query(cosulta,conn)
print(DataFrame)



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
            
def plot_a():
    plt.subplots()
    data_a = pd.read_sql(grafico_a, conn)
    plt.bar(data_a.profesion,data_a.sueldo_promedio, color = "skyblue")
    plt.title("sueldo promedio por profesion")
    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=0.35)
    plt.grid(True,linestyle=":")

def plot_b():
    plt.subplots()
    data_b = pd.read_sql(grafico_b, conn)
    plt.pie(data_b.porcentaje,labels=data_b.profesion, autopct='%1.1f%%')
    plt.title("distribuicion de profesiones")


def plot_c():
    plt.subplots()
    data_c = pd.read_sql(grafico_c, conn)
    plt.bar(data_c.nacionalidad, data_c.numero_de_profesionales, color="skyblue")
    plt.title("conteo de profesionales por nacionalidad")
    plt.xticks(rotation=45)
    plt.grid(True,linestyle=":")


            
def opciones_graf():
    while True:
        print("Que grafico desea ver")
        print('1.sueldo promedio por profesion' "\n" '2.distribuicion de profesiones' "\n" '3.conteo de profesionales por nacionalidad' "\n" '4.todos')
        resp = int(input('Ingrese el numero de su eleccion: '))
        if resp == 1:
            plot_a()
            break
        elif resp == 2:
            plot_b()
            break
        elif resp == 3:
            plot_c()
            break
        elif resp == 4:
            plot_a()
            plot_b()
            plot_c()
            break
        else:
            print('Opcion no valida vuelva a intentar ')

def menu():
    while True:
        print('1.Busqueda singular (1 persona)' "\n" '2.Busqueda por grupo (Varias personas)' "\n" '3.mostrar graficos')
        filtro = int(input('Ingresa el numero de tu eleccion: '))

        if filtro == 1:
            BusquedaSing(conn)
            break
        if filtro == 2:
            BusquedaGrup(conn)
            break
        if filtro == 3:
            opciones_graf()
            break
        else:
            print('opcion no valida vuelva a intentar')

menu()
plt.show()
conn.close()