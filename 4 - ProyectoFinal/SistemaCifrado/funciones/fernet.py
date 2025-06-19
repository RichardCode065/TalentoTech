"""
fernet.py - Módulo de cifrado y descifrado de archivos usando Fernet.
Soporta archivos .txt, .pdf y .docx.
Incluye funciones para generación/carga de claves, lectura/escritura de archivos,
y operaciones de cifrado y descifrado.
"""


import os
import docx
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from docx import Document
from cryptography.fernet import Fernet
from PyPDF2 import PdfReader

def generarClave(rutaDestino):
    """
    Genera una clave Fernet y la guarda en un archivo.
    Parámetros:
        rutaDestino (str): Ruta donde se guardará la clave generada.
    Retorna:
        bytes: Clave generada.
    """
    clave = Fernet.generate_key()
    with open(rutaDestino, 'wb') as archivoClave:
        archivoClave.write(clave)
    return clave

def cargarClave(ruta):
    """
    Carga una clave Fernet desde un archivo.
    Parámetros:
        ruta (str): Ruta del archivo que contiene la clave.
    Retorna:
        bytes: Clave cargada.
    """
    with open(ruta, 'rb') as archivo:
        return archivo.read()

def leerContenido(ruta):
    """
    Lee el contenido de un archivo según su tipo.
    Soporta archivos .txt, .pdf y .docx.
    Parámetros:
        ruta (str): Ruta del archivo a leer.
    Retorna:
        str: Contenido del archivo como texto plano.
    """
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
    """
    Escribe texto plano en un archivo según su extensión.
    Soporta archivos .txt, .pdf y .docx.
    Parámetros:
        ruta (str): Ruta del archivo a escribir.
        contenido (str): Texto plano a escribir.
    """
    extension = os.path.splitext(ruta)[1].lower()

    if extension == '.txt':
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(contenido)
    elif extension == '.pdf':
        c = canvas.Canvas(ruta, pagesize=letter)
        width, height = letter
        y = height - 40
        for linea in contenido.split('\n'):
            c.drawString(40, y, linea[:100])
            y -= 15
            if y < 40:
                c.showPage()
                y = height - 40
        c.save()
    elif extension == '.docx':
        doc = Document()
        for linea in contenido.split('\n'):
            doc.add_paragraph(linea)
        doc.save(ruta)
    else:
        raise ValueError("Tipo de archivo no soportado para escritura")

def cifrarArchivo(rutaEntrada, clave, rutaSalida):
    """
    Cifra el contenido de un archivo y lo guarda como binario.
    Parámetros:
        rutaEntrada (str): Ruta del archivo original.
        clave (bytes): Clave Fernet para cifrado.
        rutaSalida (str): Ruta del archivo cifrado.
    Retorna:
        str: Ruta del archivo cifrado.
    """
    fernet = Fernet(clave)
    texto = leerContenido(rutaEntrada)
    datosCifrados = fernet.encrypt(texto.encode('utf-8'))
    with open(rutaSalida, 'wb') as f:
        f.write(datosCifrados)
    return rutaSalida

def descifrarArchivo(rutaEntrada, clave, rutaSalida):
    """
    Descifra un archivo binario cifrado con Fernet.
    Parámetros:
        rutaEntrada (str): Ruta del archivo cifrado (.bin).
        clave (bytes): Clave Fernet para descifrado.
        rutaSalida (str): Ruta para guardar el archivo descifrado.
    Retorna:
        str: Ruta del archivo descifrado.
    """
    fernet = Fernet(clave)
    with open(rutaEntrada, 'rb') as f:
        datosCifrados = f.read()
    datos = fernet.decrypt(datosCifrados).decode('utf-8')
    escribirContenido(rutaSalida, datos)
    return rutaSalida
