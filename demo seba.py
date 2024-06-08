import sqlite3
import pandas as pd
from docx import Document

def connect_db():
    """
    Establece una conexión con la base de datos "db_personas.db" y la devuelve.
    """
    conn = sqlite3.connect('Sql_data/db_personas.db')
    return conn

def get_data(conn):
    """
    Obtiene los datos de las personas y los roles de la base de datos y los devuelve como un DataFrame de Pandas.
    """
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

def BusquedaSing(conn):
    while True:
        print('Desea realizar una búsqueda por:')
        print('1. Rut')
        print('2. Nombre Completo')
        eleccion = int(input('Por favor ingrese el número de su selección: '))

        if eleccion == 1:
            rut = input('Ingrese el rut de la persona: ')
            query = "SELECT * FROM personas INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios WHERE personas.rut = ?"
            res = pd.read_sql_query(query, conn, params=(rut,))
            print(res)
            break
        elif eleccion == 2:
            nombre = input('Ingrese el Nombre completo de la persona: ')
            query = "SELECT * FROM personas INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios WHERE personas.nombre_completo = ?"
            res = pd.read_sql_query(query, conn, params=(nombre,))
            print(res)
            break
        else:
            print('Opción no válida, vuelva a intentar.')

def BusquedaGrup(conn):
    while True:
        print('Desea realizar una búsqueda por: ')
        print('1. Sueldo')
        print('2. Rol')
        print('3. Nacionalidad')
        print('4. Profesión')
        eleccion = int(input('Ingrese el número de su elección: '))

        if eleccion == 1:
            sueldo = int(input('Ingrese el sueldo de la persona: '))
            query = "SELECT * FROM personas INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios WHERE Salarios.sueldo = ?"
            res = pd.read_sql_query(query, conn, params=(sueldo,))
            print(res)
            break
        elif eleccion == 2:
            rol = input('Ingrese el rol de la persona: ')
            query = "SELECT * FROM personas INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios WHERE Salarios.rol = ?"
            res = pd.read_sql_query(query, conn, params=(rol,))
            print(res)
            break
        elif eleccion == 3:
            nacionalidad = input('Ingrese la nacionalidad de la persona: ')
            query = "SELECT * FROM personas INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios WHERE personas.nacionalidad = ?"
            res = pd.read_sql_query(query, conn, params=(nacionalidad,))
            print(res)
            break
        elif eleccion == 4:
            profesion = input('Ingrese la profesión de la persona: ')
            query = "SELECT * FROM personas INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios WHERE personas.profesion = ?"
            res = pd.read_sql_query(query, conn, params=(profesion,))
            print(res)
            break
        else:
            print('Opción no válida, vuelva a intentar.')

def menu():
    conn = connect_db()
    while True:
        print('¿Qué tipo de búsqueda desea realizar?: ')
        print('1. Búsqueda singular (1 persona)')
        print('2. Búsqueda por grupo (Varias personas)')
        filtro = int(input('Ingrese el número de su elección: '))

        if filtro == 1:
            BusquedaSing(conn)
            break
        elif filtro == 2:
            BusquedaGrup(conn)
            break
        else:
            print('Opción no válida, vuelva a intentar.')
    conn.close()

menu()

