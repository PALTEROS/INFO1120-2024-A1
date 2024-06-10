<<<<<<< HEAD
=======
from docx import Document
from docx.shared import Pt
from docx.shared import Inches
import pandas as pd
>>>>>>> ac685e44d52aa7d22b20be6c9f708cf5d705d426
import os
from docx import Document
from docx.shared import Pt, Cm, Mm
import pandas as pd
import sqlite3

def example_contract(date: str, rol: str, address: str, rut: str, full_name: str, nationality: str, birth_date: str, profession: str, salary: str, output_path: str):
    document = Document()
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

def example_contract(date: str, rol: str, address: str, rut: str, full_name: str, nationality: str, birth_date: str, profession: str, salary: str) -> str:
    document = Document()

    # Configuración de parámetros del documento
    font = document.styles['Normal'].font
    font.name = 'Book Antiqua'
    sections = document.sections
    for section in sections:
<<<<<<< HEAD
        section.page_height = Cm(35.56)
        section.page_width = Cm(21.59)
        section.top_margin = Cm(0.5)
        section.bottom_margin = Cm(1.27)
        section.left_margin = Cm(1.27)
        section.right_margin = Cm(1.27)
        section.header_distance = Mm(12.7)
        section.footer_distance = Mm(12.7)

    # Encabezado del documento (imagen header.png)
    header = document.sections[0].header
    paragraph = header.paragraphs[0]
    run = paragraph.add_run()
    run.add_picture('imagenes/header.png')

    # Logo (imagen logo.png)
    document.add_picture('imagenes/logo.png')

    # Título del contrato
    h = document.add_paragraph('')
    h.add_run('CONTRATO DE PRESTACIÓN DE SERVICIOS A HONORARIOS\n').bold = True
    h.alignment = 1
    font.size = Pt(10)
    h.add_run('............................................................................................................................................................................................................................. ').bold = True

    # Contenido del contrato
    p = document.add_paragraph(f'En Temuco, a {str(date)}, entre la Corporación de Innovación y Desarrollo Tecnológico, Rut 78.898.766-4, representada por su Director General don(a) Roberto Gomez Bolainas, Cédula de Identidad Nº 10.678.990-2, ambos domiciliados en Caupolican 455 de esta ciudad, en adelante la “Corporación” y  {full_name}, de nacionalidad {nationality}, de profesión {profession}, nacido el {birth_date}, con domicilio en {address}, Cédula de Identidad N° {rut}, en adelante, el “Prestador de Servicios”, se ha convenido el siguiente contrato de prestación de servicios a honorarios: \n')
    font.size = Pt(8)
    p1 = document.add_paragraph('')
    p1.add_run('PRIMERO        :').bold = True
    p1.add_run('En el marco del acuerdo de servicios profesionales fechado el 11 de noviembre de 2020, establecido entre la Agencia Nacional de Estándares Educativos y la Corporación de Innovación y Desarrollo Tecnológico , y ratificado según la Resolución Exenta N°603 del 23 de noviembre de 2020, la Corporación encarga los servicios profesionales del Prestador de Servicios, para que ejecute la siguiente tarea en el proyecto "Evaluación de competencias específicas y metodologías de aprendizaje artificial 2020, ID 67703-20-JJ90."')
    p1.add_run('\n SEGUNDO        :').bold = True
    p1.add_run('El rol a desempeñar es de '+rol+'.')
    p1.add_run('\n TERCERO        :').bold = True
    p1.add_run('El plazo para la realización de la prestación de servicios encomendada será el '+str(date))
    p1.add_run('\n CUARTO        :').bold = True
    p1.add_run('Por el servicio profesional efectivamente realizado, se pagara un monto bruto variable, el cual corresponderá a cada rol dentro de la empresa capacitación, de acuerdo al siguiente detalle: ')
    table = document.add_table(rows=2, cols=2)
    table.alignment = 1
    hdr_cells0 = table.rows[0].cells
    hdr_cells0[0].text='Rol'
    hdr_cells0[1].text='Monto Bruto'
    hdr_cells = table.rows[1].cells
    hdr_cells[0].text = rol
    hdr_cells[1].text= salary
    p1.add_run('\n QUINTO        :').bold = True
    p1.add_run('El Prestador de Servicios acepta el encargo y las condiciones precedentes.')
    p1.add_run('\n SEXTO        :').bold = True
    p1.add_run(
        'El Prestador de Servicios está obligado a mantener la confidencialidad de todos los materiales utilizados, conforme al Acuerdo de Confidencialidad previamente establecido.')
    p1.add_run('\n En comprobante, previa lectura y ratificación, las partes firman.  ').bold = True

    # Firmas (modificado para incluir imagen de firma)
    table = document.add_table(rows=2, cols=2)
    table.alignment = 1
    hdr_cells0 = table.rows[0].cells[1].add_paragraph()
    r = hdr_cells0.add_run()
    r.add_picture('imagenes/firma.png')
    hdr_cells = table.rows[1].cells
    hdr_cells[0].text = '-----------------------------------------------------------\nEL PRESTADOR DE SERVICIOS'
    hdr_cells[1].text = '-----------------------------------------------------------\np. LA CORPORACION'

    # Pie de página (imagen footer1.png)
    footer = document.sections[0].footer
    paragraph = footer.paragraphs[0]
    run = paragraph.add_run('Caupolican 0455, Temuco, Chile, www.corpoindet.cl\n')
    run.add_picture("imagenes/footer1.png")

    # Guardar el documento
    document.save(f'{full_name}.docx')
=======
        section.page_height = Inches(11)
        section.page_width = Inches(8.5)
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # Encabezado del documento
    header_section = document.sections[0].header
    header_paragraph = header_section.paragraphs[0]
    header_paragraph.text = ""
    header_paragraph.add_run().add_picture('imagenes/header.png', width=Inches(6))

    # Contenido del contrato
    p = document.add_paragraph(f'En Temuco, a {str(date)}, entre la Corporación de Innovación y Desarrollo Tecnológico, Rut 78.898.766-4, representada por su Director General don(a) Roberto Gomez Bolainas, Cédula de Identidad Nº 10.678.990-2, ambos domiciliados en Caupolican 455 de esta ciudad, en adelante la “Corporación” y {full_name}, de nacionalidad {nationality}, de profesión {profession}, nacido el {birth_date}, con domicilio en {address}, Cédula de Identidad N° {rut}, en adelante, el “Prestador de Servicios”, se ha convenido el siguiente contrato de prestación de servicios a honorarios: \n')
    font.size = Pt(8)
    p1 = document.add_paragraph('')
    p1.add_run('PRIMERO        :').bold = True
    p1.add_run('En el marco del acuerdo de servicios profesionales fechado el 11 de noviembre de 2020, establecido entre la Agencia Nacional de Estándares Educativos y la Corporación de Innovación y Desarrollo Tecnológico , y ratificado según la Resolución Exenta N°603 del 23 de noviembre de 2020, la Corporación encarga los servicios profesionales del Prestador de Servicios, para que ejecute la siguiente tarea en el proyecto "Evaluación de competencias específicas y metodologías de aprendizaje artificial 2020, ID 67703-20-JJ90."')
    p1.add_run('\n SEGUNDO        :').bold = True
    p1.add_run('El rol a desempeñar es de ' + rol + '.')
    p1.add_run('\n TERCERO        :').bold = True
    p1.add_run('El plazo para la realización de la prestación de servicios encomendada será el ' + str(date))
    p1.add_run('\n CUARTO        :').bold = True
    p1.add_run('Por el servicio profesional efectivamente realizado, se pagará un monto bruto variable, el cual corresponderá a cada rol dentro de la empresa capacitación, de acuerdo al siguiente detalle: ')
    table = document.add_table(rows=2, cols=2)
    table.alignment = 1
    hdr_cells0 = table.rows[0].cells
    hdr_cells0[0].text = 'Rol'
    hdr_cells0[1].text = 'Monto Bruto'
    hdr_cells = table.rows[1].cells
    hdr_cells[0].text = rol
    hdr_cells[1].text = salary
    p1.add_run('\n QUINTO        :').bold = True
    p1.add_run('El Prestador de Servicios acepta el encargo y las condiciones precedentes.')
    p1.add_run('\n SEXTO        :').bold = True
    p1.add_run(
        'El Prestador de Servicios está obligado a mantener la confidencialidad de todos los materiales utilizados, conforme al Acuerdo de Confidencialidad previamente establecido.')
    p1.add_run('\n En comprobante, previa lectura y ratificación, las partes firman.  ').bold = True

    # Pie de página
    footer_section = document.sections[0].footer
    footer_paragraph = footer_section.paragraphs[0]
    footer_paragraph.text = ""
    footer_paragraph.add_run('Caupolican 0455, Temuco, Chile, www.corpoindet.cl').bold = True
    footer_paragraph.add_run().add_picture('imagenes/footer1.png', width=Inches(6))

    # Guardar el documento
    os.makedirs("contratos", exist_ok=True)
    output_file = os.path.join("contratos", f"{full_name.replace(' ', '_')}_contrato.docx")
    document.save(output_file)
    print(f"Contrato guardado como {output_file}")
>>>>>>> ac685e44d52aa7d22b20be6c9f708cf5d705d426

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
                persona = res.iloc[0].to_dict()
                example_contract(date=persona['fecha_ingreso'],
                                 rol=persona['Rol'],
                                 address=persona['residencia'],
                                 rut=persona['rut'],
                                 full_name=persona['nombre_completo'],
                                 nationality=persona['nacionalidad'],
                                 birth_date=persona['fecha_de_nacimiento'],
                                 profession=persona['profesion'],
                                 salary=str(persona['Sueldo']))
            else:
                print("No se encontró ninguna persona con ese RUT.")
            break
        elif eleccion == 2:
            nombre = input('Ingrese el nombre completo de la persona: ')
            query = "SELECT personas.*, Salarios.Rol, Salarios.Sueldo FROM personas INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios WHERE personas.nombre_completo = ?"
            res = pd.read_sql_query(query, conn, params=(nombre,))
            if not res.empty:
                persona = res.iloc[0].to_dict()
                example_contract(date=persona['fecha_ingreso'],
                                 rol=persona['Rol'],
                                 address=persona['residencia'],
                                 rut=persona['rut'],
                                 full_name=persona['nombre_completo'],
                                 nationality=persona['nacionalidad'],
                                 birth_date=persona['fecha_de_nacimiento'],
                                 profession=persona['profesion'],
                                 salary=str(persona['Sueldo']))
            else:
                print("No se encontró ninguna persona con ese nombre.")
            break
        else:
            print('Opción no válida, vuelva a intentar.')

def generar_contratos_rango(conn, start, end, output_path, template_path, images_path):
    df = pd.read_sql_query("SELECT personas.*, Salarios.Rol, Salarios.Sueldo FROM personas INNER JOIN Salarios ON personas.id_rol = Salarios.id_salarios", conn)
    print("Columnas disponibles en el DataFrame:", df.columns)
    sub_df = df.iloc[start:end]
    for index, row in sub_df.iterrows():
        example_contract(date=row['fecha_ingreso'],
                         rol=row['Rol'],
                         address=row['residencia'],
                         rut=row['rut'],
                         full_name=row['nombre_completo'],
                         nationality=row['nacionalidad'],
                         birth_date=row['fecha_de_nacimiento'],
                         profession=row['profesion'],
                         salary=str(row['Sueldo']))

def menu():
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Obtiene el directorio actual del script
    subdir_path = os.path.join(base_dir, 'Evaluación 2')
    
    db_path = os.path.join(subdir_path, 'Sql_data', 'db_personas.db')
<<<<<<< HEAD
    template_path = os.path.join(subdir_path, 'plantilla_word', 'template.docx')  
    output_path = os.path.join(subdir_path, 'contrato_ejemplo') 
    images_path = os.path.join(subdir_path, 'imagenes')  
=======
    template_path = os.path.join(subdir_path, 'plantilla_word', 'template.docx')  # Ajustar según el nombre del archivo
    output_path = os.path.join(subdir_path, 'contratos')  # Directorio donde se guardarán los contratos generados
    images_path = os.path.join(subdir_path, 'imagenes')  # Directorio donde están las imágenes
>>>>>>> ac685e44d52aa7d22b20be6c9f708cf5d705d426
    
    os.makedirs(output_path, exist_ok=True)
    
    try:
        conn = connect_db(db_path)
    except FileNotFoundError as e:
        print(e)
        return
    
    while True:
        print('¿Qué tipo de búsqueda desea realizar?: ')
        print('1. Búsqueda singular (1 persona)')
        print('2. Generar contratos para un rango de personas')
        try:
            filtro = int(input('Ingrese el número de su elección: '))
        except ValueError:
            print("Debe ingresar un número.")
            continue

        if filtro == 1:
            busqueda_persona(conn, template_path, output_path, images_path)
            break
        elif filtro == 2:
            start = int(input('Ingrese el índice de inicio: '))
            end = int(input('Ingrese el índice de fin: '))
            generar_contratos_rango(conn, start, end, output_path, template_path, images_path)
            break
        else:
            print('Opción no válida, vuelva a intentar.')
    
    conn.close()

# Ejecutar menú principal
<<<<<<< HEAD
menu()
=======
menu()
>>>>>>> ac685e44d52aa7d22b20be6c9f708cf5d705d426
