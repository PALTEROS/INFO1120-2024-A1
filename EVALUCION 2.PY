import sqlite3
import pandas as pd

def conecBD():
    return sqlite3.connect('Sql_data/db_personas.db')

def gen_cons():
    conn = conecBD()
    consulta = """
    SELECT * 
    from personas
    INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios
    """
    DataFrame= pd.read_sql_query(consulta,conn)
    print(DataFrame)
    conn.close()


def BusquedaSing():
    conn = conecBD()
    while True:
        print('Desea realizar una busqueda por:')
        print('1. Rut')
        print('2. Nombre Completo')
        try:
            eleccion = int(input('Por favor ingrese el numero de su seleccion: '))

            if eleccion == 1:
                rut = str(input('Ingrese el rut de la persona: '))
                query = f"SELECT * FROM personas INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios WHERE personas.rut = ?"
                res = pd.read_sql_query(query, conn,params=(rut,))
                print(res)
                break
            elif eleccion == 2:
                nombre = input('Ingrese el Nombre completo de la persona: ').strip().lower()
                query = f"SELECT * FROM personas INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios WHERE personas.nombre_completo = ?"
                res = pd.read_sql_query(query, conn,params=(nombre,))
                print(res)
                break
        except ValueError:
            print('Ingrese un numero valido')
    conn.close()     

def BusquedaGrup():
    conn = conecBD()
    while True:
        print('Desea realizar una busqueda por: ')
        print('1.Sueldo' "\n" '2.Rol' "\n" '3.Nacionalidad' "\n" '4.Profesion')
        try:
            eleccion = int(input('Ingrese el numero de su eleccion: '))

            if eleccion == 1:
                sueldo = int(input('Ingrese el sueldo de la persona: '))
                query = f'SELECT * FROM personas INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios WHERE Salarios.Sueldo = ?'
                res = pd.read_sql_query(query, conn,params=(sueldo,))
                print(res)
                break
            elif eleccion == 2:
                rol = input('Ingresa el rol de la persona: ').strip().capitalize()
                query =f'SELECT * FROM personas INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios WHERE Salarios.Rol = ?'
                res = pd.read_sql_query(query,conn,params=(rol,))
                print(res)
                break
            elif eleccion == 3:
                nacionalidad = input('Ingrese la nacionalidad de la persona: ').strip().capitalize()
                query = f"SELECT * FROM personas INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios WHERE personas.Nacionalidad = ?"
                res = pd.read_sql_query(query,conn, params=(nacionalidad,))
                print(res)
                break
            elif eleccion == 4:
                profesion = input('Ingresa la profesion de la persona: ').strip().lower()
                query = f'SELECT * FROM personas INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios WHERE personas.profesion = ?'
                res = pd.read_sql_query(query,conn,params=(profesion,))
                print(res)
                break
            else:
                print('Opcion no valida vuelva a intentar ')
        except ValueError:
            print('Ingrese un numero valido')
    conn.close()

def menu():
    conn = conecBD()
    try:
        while True:
            print('Que tipo de busqueda desea ralizar: ')
            print('1. Busqueda singular (1 persona)')
            print('2. Busqueda por grupo (Varias personas)')
            try:
                filtro = int(input('Ingresa el numero de tu eleccion: '))

                if filtro == 1:
                    BusquedaSing()
                    break
                elif filtro == 2:
                    BusquedaGrup()
                    break
                else:
                 print('opcion no valida vuelva a intentar')
            except ValueError:
             print('Ingrese un numero valido')
    finally:
        conn.close()

while True:
    menu()
    repito = input('Desea realizar otra consulta Si/No: ').strip().lower()

    if repito != "si":
        print('Nos vemo')
        break