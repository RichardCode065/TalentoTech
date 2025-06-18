" Módulo de cifrado y descifrado de archivos usando Fernet. Soporta archivos .txt, .pdf y .docx."
" Incluye funciones para lectura, escritura, cifrado y descifrado de contenido. "

# Importacion de librerias
import os
import docx
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from docx import Document
from cryptography.fernet import Fernet
from PyPDF2 import PdfReader

def generarClave(rutaDestino): 
    "Genera una clave Fernet y la guarda en un archivo."

    clave = Fernet.generate_key()
    with open(rutaDestino, 'wb') as archivoClave:
        archivoClave.write(clave)
    return clave

def cargarClave(ruta):
    "Carga una clave Fernet desde un archivo."

    with open(ruta, 'rb') as archivo:
        return archivo.read()

def leerContenido(ruta):
    "Lee el contenido de un archivo según su extensión. Soporta .txt, .pdf y .docx."

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
    "Lee el contenido de un archivo según su extensión. Soporta .txt, .pdf y .docx."
   
    extension = os.path.splitext(ruta)[1].lower()

    if extension == '.txt':
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(contenido)

    elif extension == '.pdf':
        c = canvas.Canvas(ruta, pagesize=letter)
        width, height = letter
        y = height - 40  # margen superior

        for linea in contenido.split('\n'):
            c.drawString(40, y, linea[:100])  # corta la línea si es muy larga
            y -= 15  # espacio entre líneas
            if y < 40:  # salto de página
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


def cifrarArchivo(rutaArchivo, clave, rutaSalida):
    "Cifra el contenido de un archivo con Fernet y lo guarda como binario."

    fernet = Fernet(clave)
    texto = leerContenido(rutaArchivo)
    datosCifrados = fernet.encrypt(texto.encode('utf-8'))
    with open(rutaSalida, 'wb') as f:
        f.write(datosCifrados)
    return rutaSalida

def descifrarArchivo(rutaArchivoCifrado, clave, rutaSalida):
    "Descifra un archivo cifrado con Fernet y escribe el contenido descifrado."

    fernet = Fernet(clave)
    with open(rutaArchivoCifrado, 'rb') as f:
        datosCifrados = f.read()
    datos = fernet.decrypt(datosCifrados).decode('utf-8')
    escribirContenido(rutaSalida, datos)
    return rutaSalida