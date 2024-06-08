nn
import sqlite3
import pandas as pd
from docx import Document

def connect_db():
    """
    Establece una conexión con la base de datos "db_personas.db" y la devuelve.
    """
    conn = sqlite3.connect('Sql_data/db_personas.db')
    return conn
def get_data(conn): "Obtiene los datos de las personas y los roles de la base de datos y los devuelve como un DataFrame de Pandas."


consulta = """
        SELECT * 
        FROM personas
        INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios
    """
    cursor = conn.cursor()
    cursor.execute(consulta)
    rows = cursor.fetchall()
    dataframe = pd.DataFrame(rows, columns=[col[0] for col in cursor.description])
    return dataframe

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
conn.close()