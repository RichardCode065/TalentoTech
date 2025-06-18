" Módulo de cifrado y descifrado de archivos usando Vigenere. Soporta archivos .txt, .pdf y .docx."
" Incluye funciones para lectura, cifrado y descifrado de contenido. "

# Importacion de librerias
import os
import docx
from PyPDF2 import PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def leerArchivo(ruta):
    "Lee archivo de texto, PDF o Word (.docx) y devuelve su contenido como texto."

    ext = os.path.splitext(ruta)[1].lower()
    if ext == '.txt':
        with open(ruta, 'r', encoding='utf-8') as f:
            return f.read()
    elif ext == '.pdf':
        reader = PdfReader(ruta)
        texto = ""
        for pagina in reader.pages:
            texto += pagina.extract_text() or ""
        return texto
    elif ext == '.docx':
        doc = docx.Document(ruta)
        return "\n".join([p.text for p in doc.paragraphs])
    else:
        raise ValueError("Formato de archivo no soportado")

def guardarArchivo(texto, ruta):
    "Guarda texto en .txt, .pdf o .docx según la extensión de la ruta."

    ext = os.path.splitext(ruta)[1].lower()

    if ext == '.txt':
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(texto)

    elif ext == '.pdf':
        c = canvas.Canvas(ruta, pagesize=letter)
        width, height = letter
        y = height - 40  # margen superior

        for linea in texto.split('\n'):
            c.drawString(40, y, linea[:100])  # cortar línea si es muy larga
            y -= 15
            if y < 40:
                c.showPage()
                y = height - 40
        c.save()

    elif ext == '.docx':
        doc = docx.Document()
        for linea in texto.split('\n'):
            doc.add_paragraph(linea)
        doc.save(ruta)

    else:
        raise ValueError("Formato de archivo no soportado")

def cifrarVigenere(texto, clave):
    "Aplica el cifrado Vigenère a un texto plano usando la clave proporcionada."

    resultado = ""
    clave = clave.upper()
    indice_clave = 0

    for letra in texto:
        if letra.isalpha():
            offset = 65 if letra.isupper() else 97
            k = ord(clave[indice_clave % len(clave)]) - 65
            nueva_letra = chr((ord(letra) - offset + k) % 26 + offset)
            resultado += nueva_letra
            indice_clave += 1
        else:
            resultado += letra
    return resultado

def descifrarVigenere(texto, clave):
    "Descifra un texto cifrado con Vigenère usando la clave original."

    resultado = ""
    clave = clave.upper()
    indice_clave = 0

    for letra in texto:
        if letra.isalpha():
            offset = 65 if letra.isupper() else 97
            k = ord(clave[indice_clave % len(clave)]) - 65
            nueva_letra = chr((ord(letra) - offset - k) % 26 + offset)
            resultado += nueva_letra
            indice_clave += 1
        else:
            resultado += letra
    return resultado