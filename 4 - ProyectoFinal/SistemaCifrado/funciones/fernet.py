# funciones/fernet.py
import os
from cryptography.fernet import Fernet
from PyPDF2 import PdfReader, PdfWriter
from docx import Document

def generarClave(rutaDestino):
    clave = Fernet.generate_key()
    with open(rutaDestino, 'wb') as archivoClave:
        archivoClave.write(clave)
    return clave

def cargarClave(ruta):
    with open(ruta, 'rb') as archivo:
        return archivo.read()

def leerContenido(ruta):
    extension = os.path.splitext(ruta)[1].lower()
    if extension == '.txt':
        with open(ruta, 'r', encoding='utf-8') as f:
            return f.read()
    elif extension == '.pdf':
        reader = PdfReader(ruta)
        texto = ""
        for pagina in reader.pages:
            texto += pagina.extract_text() or ""
        return texto
    elif extension == '.docx':
        doc = Document(ruta)
        return "\n".join(p.text for p in doc.paragraphs)
    else:
        raise ValueError("Tipo de archivo no soportado para lectura")

def escribirContenido(ruta, contenido):
    extension = os.path.splitext(ruta)[1].lower()
    if extension == '.txt':
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(contenido)
    elif extension == '.pdf':
        writer = PdfWriter()
        writer.add_blank_page(width=72 * 8.5, height=72 * 11)
        with open(ruta, 'wb') as f:
            writer.write(f)  # PDF vacío como placeholder (texto no editable en PDF plano)
    elif extension == '.docx':
        doc = Document()
        doc.add_paragraph(contenido)
        doc.save(ruta)
    else:
        raise ValueError("Tipo de archivo no soportado para escritura")

def cifrarArchivo(rutaArchivo, clave):
    fernet = Fernet(clave)
    texto = leerContenido(rutaArchivo)
    datosCifrados = fernet.encrypt(texto.encode('utf-8'))
    rutaSalida = rutaArchivo.replace('.', '_Fernet.')
    with open(rutaSalida, 'wb') as f:
        f.write(datosCifrados)
    return rutaSalida

def descifrarArchivo(rutaArchivo, clave):
    fernet = Fernet(clave)
    with open(rutaArchivo, 'rb') as f:
        datosCifrados = f.read()
    datos = fernet.decrypt(datosCifrados).decode('utf-8')
    rutaSalida = rutaArchivo.replace('_Fernet.', '_Descifrado.')
    escribirContenido(rutaSalida, datos)
    return rutaSalida