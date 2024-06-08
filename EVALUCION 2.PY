from docx import Document
from docx.shared import Inches
import pandas as pd
import os
import sqlite3

def connect_db(db_path):
    """
    Establece una conexión con la base de datos y la devuelve.
    """
    print(f"Intentando abrir la base de datos en: {db_path}")
    if os.path.exists(db_path):
        print("El archivo de la base de datos existe.")
    else:
        print("El archivo de la base de datos no existe. Verifique la ruta.")
        raise FileNotFoundError(f"Archivo de base de datos no encontrado en la ruta: {db_path}")
    try:
        conn = sqlite3.connect(db_path)
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        raise
    return conn

def generar_contrato_con_imagenes(persona, template_path, output_path, images_path):
    """
    Genera un contrato en Word para una persona específica utilizando una plantilla e incluye imágenes.
    """
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Archivo de plantilla no encontrado en la ruta: {template_path}")

    doc = Document(template_path)
    placeholders = {
    'NOMBRE': persona['nombre_completo'],
    'RUT': persona['rut'],
    'ROL': persona['Rol'],
    'SUELDO': str(persona['Sueldo']),
    'FECHA_INGRESO': persona['fecha_ingreso'],
    'NACIONALIDAD': persona['nacionalidad'],
    'PROFESION': persona['profesion'],
    'FECHA_NACIMIENTO': persona['fecha_de_nacimiento'],
    'DOMICILIO': persona['residencia'],  # Cambia 'domicilio' a 'residencia'
}

    # Reemplazo de placeholders con la información de la persona
    for para in doc.paragraphs:
        for placeholder, value in placeholders.items():
            if placeholder in para.text:
                para.text = para.text.replace(placeholder, value)
    
    # Inserción de imágenes específicas
    header_section = doc.sections[0].header
    header_paragraph = header_section.paragraphs[0]
    header_paragraph.text = ""
    header_paragraph.add_run().add_picture(os.path.join(images_path, 'header.png'), width=Inches(6))

    footer_section = doc.sections[0].footer
    footer_paragraph = footer_section.paragraphs[0]
    footer_paragraph.text = ""
    footer_paragraph.add_run().add_picture(os.path.join(images_path, 'foother.png'), width=Inches(6))

    for para in doc.paragraphs:
        if 'LOGO' in para.text:
            para.text = para.text.replace('LOGO', '')
            para.add_run().add_picture(os.path.join(images_path, 'logo.png'), width=Inches(2))
        if 'FIRMA' in para.text:
            para.text = para.text.replace('FIRMA', '')
            para.add_run().add_picture(os.path.join(images_path, 'firma.png'), width=Inches(2))

    os.makedirs(output_path, exist_ok=True)
    output_file = os.path.join(output_path, f"{persona['nombre_completo'].replace(' ', '_')}_contrato.docx")
    doc.save(output_file)
    print(f"Contrato guardado como {output_file}")

def busqueda_persona(conn, template_path, output_path, images_path):
    while True:
        print('Desea realizar una búsqueda por:')
        print('1. RUT')
        print('2. Nombre Completo')
        try:
            eleccion = int(input('Por favor ingrese el número de su selección: '))
        except ValueError:
            print("Debe ingresar un número.")
            continue

        if eleccion == 1:
            rut = input('Ingrese el RUT de la persona: ')
            query = "SELECT personas.*, Salarios.Rol, Salarios.Sueldo FROM personas INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios WHERE personas.rut = ?"
            res = pd.read_sql_query(query, conn, params=(rut,))
            if not res.empty:
                generar_contrato_con_imagenes(res.iloc[0], template_path, output_path, images_path)
            else:
                print("No se encontró ninguna persona con ese RUT.")
            break
        elif eleccion == 2:
            nombre = input('Ingrese el nombre completo de la persona: ')
            query = "SELECT personas.*, Salarios.Rol, Salarios.Sueldo FROM personas INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios WHERE personas.nombre_completo = ?"
            res = pd.read_sql_query(query, conn, params=(nombre,))
            if not res.empty:
                generar_contrato_con_imagenes(res.iloc[0], template_path, output_path, images_path)
            else:
                print("No se encontró ninguna persona con ese nombre.")
            break
        else:
            print('Opción no válida, vuelva a intentar.')

def menu():
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Obtiene el directorio actual del script
    subdir_path = os.path.join(base_dir, 'Evaluación 2')
    
    db_path = os.path.join(subdir_path, 'Sql_data', 'db_personas.db')
    template_path = os.path.join(subdir_path, 'plantilla_word', 'template.docx')  # Ajustar según el nombre del archivo
    output_path = os.path.join(subdir_path, 'contrato_ejemplo')  # Directorio donde se guardarán los contratos generados
    images_path = os.path.join(subdir_path, 'imagenes')  # Directorio donde están las imágenes
    
    os.makedirs(output_path, exist_ok=True)
    
    try:
        conn = connect_db(db_path)
    except FileNotFoundError as e:
        print(e)
        return
    
    while True:
        print('¿Qué tipo de búsqueda desea realizar?: ')
        print('1. Búsqueda singular (1 persona)')
        try:
            filtro = int(input('Ingrese el número de su elección: '))
        except ValueError:
            print("Debe ingresar un número.")
            continue

        if filtro == 1:
            busqueda_persona(conn, template_path, output_path, images_path)
            break
        else:
            print('Opción no válida, vuelva a intentar.')
    
    conn.close()

# Ejecutar menú principal
menu()

