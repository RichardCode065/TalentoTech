"""
main.py - Módulo principal para ejecutar el cifrado y descifrado Vigenère.
Incluye registro de errores y manejo de archivos .txt, .pdf y .docx.
"""

import os
import logging
from funciones import vigenere  # Importa el módulo que contiene las funciones del algoritmo Vigenère

# Crear carpeta de logs si no existe
os.makedirs("logs", exist_ok=True)

# Configurar el sistema de logging para registrar errores
logging.basicConfig(
    filename='logs/error.log',  # Archivo de registro
    level=logging.ERROR,        # Solo errores serán registrados
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def cifrarVigenere(rutaArchivo, clave):
    """
    Cifra un archivo utilizando el algoritmo Vigenère.

    Parámetros:
        rutaArchivo (str): Ruta del archivo a cifrar.
        clave (str): Clave de cifrado tipo texto.

    Retorna:
        str: Mensaje con la ruta del archivo cifrado o error.
    """
    if not os.path.exists(rutaArchivo):
        mensaje = "El archivo no existe."
        logging.error(mensaje)
        return mensaje

    try:
        extension = os.path.splitext(rutaArchivo)[1].lower()
        texto = vigenere.leerArchivo(rutaArchivo)

        if not texto:
            mensaje = "El archivo está vacío o no pudo ser leído."
            logging.error(mensaje)
            return mensaje

        cifrado = vigenere.cifrarVigenere(texto, clave)
        rutaCifrado = rutaArchivo.rsplit('.', 1)[0] + "_Vigenere" + extension
        vigenere.guardarArchivo(cifrado, rutaCifrado)

        return f"✅ Cifrado Vigenère completado.\nArchivo cifrado: {rutaCifrado}"

    except Exception as e:
        logging.error(f"Error durante el cifrado Vigenère: {str(e)}")
        return "❌ Error durante el cifrado. Revisa el archivo 'logs/error.log'."

def descifrarVigenere(rutaArchivo, clave):
    """
    Descifra un archivo previamente cifrado con el algoritmo Vigenère.

    Parámetros:
        rutaArchivo (str): Ruta del archivo cifrado.
        clave (str): Clave de cifrado tipo texto.

    Retorna:
        str: Mensaje con la ruta del archivo descifrado o error.
    """
    if not os.path.exists(rutaArchivo):
        mensaje = "El archivo no existe."
        logging.error(mensaje)
        return mensaje

    try:
        extension = os.path.splitext(rutaArchivo)[1].lower()
        texto = vigenere.leerArchivo(rutaArchivo)

        if not texto:
            mensaje = "El archivo está vacío o no pudo ser leído."
            logging.error(mensaje)
            return mensaje

        descifrado = vigenere.descifrarVigenere(texto, clave)
        rutaDescifrado = rutaArchivo.rsplit('.', 1)[0] + "_Vigenere_Descifrado" + extension
        vigenere.guardarArchivo(descifrado, rutaDescifrado)

        return f"✅ Descifrado Vigenère completado.\nArchivo descifrado: {rutaDescifrado}"

    except Exception as e:
        logging.error(f"Error durante el descifrado Vigenère: {str(e)}")
        return "❌ Error durante el descifrado. Revisa el archivo 'logs/error.log'."

def ejecutarVigenere(rutaArchivo, clave):
    """
    Ejecuta el proceso completo de cifrado y descifrado usando el algoritmo Vigenère.

    Parámetros:
        rutaArchivo (str): Ruta del archivo a procesar.
        clave (str): Clave de cifrado tipo texto.

    Retorna:
        str: Mensaje con los resultados o un error.
    """
    if not os.path.exists(rutaArchivo):
        mensaje = "El archivo no existe."
        logging.error(mensaje)
        return mensaje

    try:
        extension = os.path.splitext(rutaArchivo)[1].lower()
        texto = vigenere.leerArchivo(rutaArchivo)

        if not texto:
            mensaje = "El archivo está vacío o no pudo ser leído."
            logging.error(mensaje)
            return mensaje

        cifrado = vigenere.cifrarVigenere(texto, clave)
        rutaCifrado = rutaArchivo.rsplit('.', 1)[0] + "_Vigenere" + extension
        vigenere.guardarArchivo(cifrado, rutaCifrado)

        descifrado = vigenere.descifrarVigenere(cifrado, clave)
        rutaDescifrado = rutaArchivo.rsplit('.', 1)[0] + "_Vigenere_Descifrado" + extension
        vigenere.guardarArchivo(descifrado, rutaDescifrado)

        return (
            "✅ Proceso Vigenère completado con éxito.\n"
            f"Archivo cifrado: {rutaCifrado}\n"
            f"Archivo descifrado: {rutaDescifrado}"
        )

    except Exception as e:
        logging.error(f"Error durante el proceso Vigenère: {str(e)}")
        return "Ha ocurrido un error. Revisa el archivo 'logs/error.log' para más detalles."