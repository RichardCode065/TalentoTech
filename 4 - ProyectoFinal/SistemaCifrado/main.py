"""
main.py - Módulo principal para ejecutar el cifrado y descifrado con el algoritmo Vigenère.
Incluye registro de errores, validación de clave y soporte para archivos .txt, .pdf y .docx.
"""

import os
import logging
from funciones import vigenere  # Módulo con funciones de cifrado Vigenère

# Crear carpeta de logs si no existe
os.makedirs("logs", exist_ok=True)

# Configurar logging
logging.basicConfig(
    filename='logs/error.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def claveValida(clave):
    """
    Valida que la clave esté compuesta solo por letras (mayúsculas o minúsculas).

    Parámetros:
        clave (str): Clave ingresada por el usuario.

    Retorna:
        bool: True si es válida, False si contiene caracteres no permitidos.
    """
    return clave.isalpha()

def cifrarVigenere(rutaArchivo, clave):
    """
    Cifra un archivo con el algoritmo Vigenère.

    Parámetros:
        rutaArchivo (str): Ruta del archivo de entrada.
        clave (str): Clave de cifrado.

    Retorna:
        str: Mensaje con la ruta del archivo cifrado o error.
    """
    if not os.path.exists(rutaArchivo):
        mensaje = "❌ El archivo no existe."
        logging.error(mensaje)
        return mensaje

    if not claveValida(clave):
        mensaje = "❌ La clave debe contener solo letras (A-Z, a-z), sin espacios ni símbolos."
        logging.error(mensaje)
        return mensaje

    try:
        texto = vigenere.leerArchivo(rutaArchivo)
        if not texto.strip():
            mensaje = "⚠️ El archivo está vacío o no pudo ser leído."
            logging.error(mensaje)
            return mensaje

        cifrado = vigenere.cifrarVigenere(texto, clave)
        extension = os.path.splitext(rutaArchivo)[1].lower()
        rutaCifrado = rutaArchivo.rsplit('.', 1)[0] + "_Vigenere" + extension
        vigenere.guardarArchivo(cifrado, rutaCifrado)

        return f"✅ Cifrado Vigenère completado.\n📄 Archivo cifrado: {rutaCifrado}"

    except Exception as e:
        logging.error(f"❌ Error durante el cifrado Vigenère: {str(e)}")
        return "❌ Error durante el cifrado. Revisa el archivo 'logs/error.log'."

def descifrarVigenere(rutaArchivo, clave):
    """
    Descifra un archivo cifrado con Vigenère.

    Parámetros:
        rutaArchivo (str): Ruta del archivo cifrado.
        clave (str): Clave usada para el cifrado original.

    Retorna:
        str: Mensaje con la ruta del archivo descifrado o error.
    """
    if not os.path.exists(rutaArchivo):
        mensaje = "❌ El archivo no existe."
        logging.error(mensaje)
        return mensaje

    if not claveValida(clave):
        mensaje = "❌ La clave debe contener solo letras (A-Z, a-z), sin espacios ni símbolos."
        logging.error(mensaje)
        return mensaje

    try:
        texto = vigenere.leerArchivo(rutaArchivo)
        if not texto.strip():
            mensaje = "⚠️ El archivo está vacío o no pudo ser leído."
            logging.error(mensaje)
            return mensaje

        descifrado = vigenere.descifrarVigenere(texto, clave)
        extension = os.path.splitext(rutaArchivo)[1].lower()
        rutaDescifrado = rutaArchivo.rsplit('.', 1)[0] + "_Vigenere_Descifrado" + extension
        vigenere.guardarArchivo(descifrado, rutaDescifrado)

        return f"✅ Descifrado Vigenère completado.\n📄 Archivo descifrado: {rutaDescifrado}"

    except Exception as e:
        logging.error(f"❌ Error durante el descifrado Vigenère: {str(e)}")
        return "❌ Error durante el descifrado. Revisa el archivo 'logs/error.log'."

def ejecutarVigenere(rutaArchivo, clave):
    """
    Ejecuta cifrado y descifrado completo de un archivo con Vigenère.

    Parámetros:
        rutaArchivo (str): Ruta del archivo de entrada.
        clave (str): Clave de cifrado.

    Retorna:
        str: Mensaje con rutas de archivos cifrado y descifrado o error.
    """
    if not os.path.exists(rutaArchivo):
        mensaje = "❌ El archivo no existe."
        logging.error(mensaje)
        return mensaje

    if not claveValida(clave):
        mensaje = "❌ La clave debe contener solo letras (A-Z, a-z), sin espacios ni símbolos."
        logging.error(mensaje)
        return mensaje

    try:
        texto = vigenere.leerArchivo(rutaArchivo)
        if not texto.strip():
            mensaje = "⚠️ El archivo está vacío o no pudo ser leído."
            logging.error(mensaje)
            return mensaje

        cifrado = vigenere.cifrarVigenere(texto, clave)
        extension = os.path.splitext(rutaArchivo)[1].lower()
        rutaCifrado = rutaArchivo.rsplit('.', 1)[0] + "_Vigenere" + extension
        vigenere.guardarArchivo(cifrado, rutaCifrado)

        descifrado = vigenere.descifrarVigenere(cifrado, clave)
        rutaDescifrado = rutaArchivo.rsplit('.', 1)[0] + "_Vigenere_Descifrado" + extension
        vigenere.guardarArchivo(descifrado, rutaDescifrado)

        return (
            "✅ Proceso Vigenère completado con éxito.\n"
            f"📄 Archivo cifrado: {rutaCifrado}\n"
            f"📄 Archivo descifrado: {rutaDescifrado}"
        )

    except Exception as e:
        logging.error(f"❌ Error durante el proceso Vigenère: {str(e)}")
        return "❌ Ha ocurrido un error. Revisa el archivo 'logs/error.log'."
