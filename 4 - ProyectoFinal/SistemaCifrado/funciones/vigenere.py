import os
import docx
from PyPDF2 import PdfReader, PdfWriter

def leerArchivo(ruta):
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
    ext = os.path.splitext(ruta)[1].lower()
    if ext == '.txt':
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(texto)
    elif ext == '.pdf':
        writer = PdfWriter()
        writer.add_blank_page(width=72 * 8.5, height=72 * 11)
        raise NotImplementedError("Guardar PDF no está implementado completamente.")
    elif ext == '.docx':
        doc = docx.Document()
        for linea in texto.split('\n'):
            doc.add_paragraph(linea)
        doc.save(ruta)
    else:
        raise ValueError("Formato de archivo no soportado")

def cifrarVigenere(texto, clave):
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
