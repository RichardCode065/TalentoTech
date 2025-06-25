"""
mainFernet.py - Módulo principal para ejecutar el cifrado y descifrado usando Fernet.
Soporta archivos de texto (.txt), documentos Word (.docx) y PDF (.pdf).
Registra errores en un archivo de log y asegura las carpetas necesarias.
"""

# Importación de librerías
import os
import logging
from funciones import fernet  # Módulo personalizado con las funciones de Fernet

# Crear las carpetas necesarias si no existen
os.makedirs("logs", exist_ok=True)
os.makedirs("claves", exist_ok=True)

# Configuración del sistema de logging
logging.basicConfig(
    filename='logs/error.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def cifrarFernet(rutaArchivo):
    """
    Cifra un archivo usando Fernet, generando una clave si es necesario.

    Parámetros:
        rutaArchivo (str): Ruta del archivo original a cifrar.

    Retorna:
        str: Ruta del archivo cifrado o mensaje de error.
    """
    rutaClave = "claves/clave.key"

    if not os.path.exists(rutaArchivo):
        mensaje = "El archivo a cifrar no existe."
        logging.error(mensaje)
        return mensaje

    try:
        clave = (
            fernet.cargarClave(rutaClave)
            if os.path.exists(rutaClave)
            else fernet.generarClave(rutaClave)
        )

        rutaCifrado = rutaArchivo.rsplit('.', 1)[0] + "_Fernet.cif"
        fernet.cifrarArchivo(rutaArchivo, clave, rutaCifrado)

        return f"✅ Cifrado Fernet completado.\n📄 Archivo cifrado: {rutaCifrado}"

    except Exception as error:
        logging.error(f"Error durante el cifrado Fernet: {str(error)}")
        return "❌ Error durante el cifrado. Revisa 'logs/error.log'."

def descifrarFernet(rutaCifrado):
    """
    Descifra un archivo cifrado con Fernet (.cif) y lo reconstruye en su formato original.

    Parámetros:
        rutaCifrado (str): Ruta del archivo cifrado (.cif).

    Retorna:
        str: Ruta del archivo descifrado o mensaje de error.
    """
    rutaClave = "claves/clave.key"

    if not os.path.exists(rutaCifrado):
        mensaje = "❌ El archivo cifrado no existe."
        logging.error(mensaje)
        return mensaje

    try:
        clave = fernet.cargarClave(rutaClave)

        # Extraer base: quitar "_Fernet.cif"
        baseSinExtension = rutaCifrado.rsplit("_Fernet.cif", 1)[0]

        # Recuperar extensión original
        extensionOriginal = os.path.splitext(baseSinExtension)[1]
        rutaDescifrado = baseSinExtension + "_Fernet_Descifrado" + extensionOriginal

        fernet.descifrarArchivo(rutaCifrado, clave, rutaDescifrado)

        return f"✅ Descifrado Fernet completado.\n📄 Archivo descifrado: {rutaDescifrado}"

    except Exception as error:
        logging.error(f"Error durante el descifrado Fernet: {str(error)}")
        return "❌ Error durante el descifrado. Revisa 'logs/error.log'."

def ejecutarFernet(rutaArchivo):
    """
    Ejecuta cifrado y descifrado completo de un archivo usando Fernet.

    Parámetros:
        rutaArchivo (str): Ruta del archivo original.

    Retorna:
        str: Resumen del proceso o mensaje de error.
    """
    mensaje1 = cifrarFernet(rutaArchivo)

    # Recuperar nombre del archivo cifrado
    rutaCifrada = rutaArchivo.rsplit('.', 1)[0] + "_Fernet.cif"

    mensaje2 = descifrarFernet(rutaCifrada)
    return f"{mensaje1}\n{mensaje2}"
