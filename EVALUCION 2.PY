import sqlite3
import pandas as pd
from docx import Document
import os

def connect_db(db_path):
    """
    Establece una conexion con la base de datos y la devuelve.
    """
    print(f"Intentando abrir la base de datos en: {db_path}")
    if os.path.exists(db_path):
        print("El archivo de la base de datos existe.")
    else:
        print("El archivo de la base de datos no existe. Verifique la ruta.")
        raise FileNotFoundError(f"Archivo de base de datos no encontrado en la ruta: {db_path}")
    conn = sqlite3.connect(db_path)
    return conn

def generar_contrato(persona, template_path, output_path):
    """
    Genera un contrato en Word para una persona especifica utilizando una plantilla.
    """
    doc = Document(template_path)
    for para in doc.paragraphs:
        if 'NOMBRE' in para.text:
            para.text = para.text.replace('NOMBRE', persona['nombre_completo'])
        if 'RUT' in para.text:
            para.text = para.text.replace('RUT', persona['rut'])
        if 'ROL' in para.text:
            para.text = para.text.replace('ROL', persona['rol'])
        if 'SUELDO' in para.text:
            para.text = para.text.replace('SUELDO', str(persona['sueldo']))
    
    output_file = f"{output_path}/{persona['nombre_completo'].replace(' ', '_')}_contrato.docx"
    doc.save(output_file)
    print(f"Contrato guardado como {output_file}")

def BusquedaSing(conn, template_path, output_path):
    while True:
        print('Desea realizar una busqueda por:')
        print('1. Rut')
        print('2. Nombre Completo')
        eleccion = int(input('Por favor ingrese el numero de su seleccion: '))

        if eleccion == 1:
            rut = input('Ingrese el rut de la persona: ')
            query = "SELECT * FROM personas INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios WHERE personas.rut = ?"
            res = pd.read_sql_query(query, conn, params=(rut,))
            print(res)
            if not res.empty:
                generar_contrato(res.iloc[0], template_path, output_path)
            break
        elif eleccion == 2:
            nombre = input('Ingrese el Nombre completo de la persona: ')
            query = "SELECT * FROM personas INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios WHERE personas.nombre_completo = ?"
            res = pd.read_sql_query(query, conn, params=(nombre,))
            print(res)
            if not res.empty:
                generar_contrato(res.iloc[0], template_path, output_path)
            break
        else:
            print('Opcion no valida, vuelva a intentar.')

def menu():
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Obtiene el directorio actual del script
    print(f"Directorio base: {base_dir}")
    subdir_path = os.path.join(base_dir, 'Evaluación 2')
    print(f"Directorio de subruta: {subdir_path}")
    
    db_path = os.path.join(subdir_path, 'Sql_data', 'db_personas.db')
    print(f"Ruta del archivo de base de datos: {db_path}")
    
    template_path = os.path.join(subdir_path, 'plantilla_word', 'template.docx')  # Ajustar según el nombre del archivo
    print(f"Ruta del archivo de plantilla: {template_path}")
    
    output_path = os.path.join(subdir_path, 'contrato_ejemplo')  # Directorio donde se guardaran los contratos generados
    print(f"Ruta del directorio de salida: {output_path}")
    
    os.makedirs(output_path, exist_ok=True)
    
    try:
        conn = connect_db(db_path)
    except FileNotFoundError as e:
        print(e)
        return
    
    while True:
        print('Que tipo de busqueda desea realizar?: ')
        print('1. Busqueda singular (1 persona)')
        filtro = int(input('Ingrese el numero de su eleccion: '))

        if filtro == 1:
            BusquedaSing(conn, template_path, output_path)
            break
        else:
            print('Opcion no valida, vuelva a intentar.')
    
    conn.close()

menu()

