#Importacion de librerias
import os
import logging
from funciones import fernet  # Importa el módulo que contiene las funciones para cifrado Fernet

# Crear las carpetas necesarias si no existen
os.makedirs("logs", exist_ok=True)     # Carpeta para logs de errores
os.makedirs("claves", exist_ok=True)   # Carpeta para almacenar la clave generada

# Configuración del sistema de logging
logging.basicConfig(
    filename='logs/error.log',                  # Archivo donde se guardarán los errores
    level=logging.ERROR,                        # Nivel: solo se guardarán errores
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato del mensaje
)

def ejecutarFernet(rutaArchivo):
    """ Ejecuta el proceso de cifrado y descifrado usando Fernet sobre un archivo dado.
    Parámetros:
        rutaArchivo (str): Ruta al archivo original que se desea cifrar.
    Retorna:
        str: Mensaje informativo con rutas de los archivos generados o errores encontrados.
    """

    rutaClave = "claves/clave.key"  # Ruta donde se guarda o carga la clave de cifrado

    try:
        # Validar que el archivo de entrada exista
        if not os.path.exists(rutaArchivo):
            mensaje = "El archivo a cifrar no existe."
            logging.error(mensaje)
            return mensaje

        # Verificar si ya existe una clave Fernet. Si no, generarla.
        if os.path.exists(rutaClave):
            clave = fernet.cargarClave(rutaClave)  # Cargar clave existente
        else:
            clave = fernet.generarClave(rutaClave)  # Generar nueva clave y guardarla

        # Cifrar el archivo (se guarda como binario con extensión .cif)
        rutaCifrado = rutaArchivo.rsplit('.', 1)[0] + "_Fernet.cif"
        fernet.cifrarArchivo(rutaArchivo, clave, rutaCifrado)

        # Descifrar el archivo cifrado y reconstruirlo en su formato original
        extension_original = os.path.splitext(rutaArchivo)[1].lower()
        rutaDescifrado = rutaArchivo.rsplit('.', 1)[0] + "_Fernet_Descifrado" + extension_original
        fernet.descifrarArchivo(rutaCifrado, clave, rutaDescifrado)

        # Retornar mensaje exitoso con rutas de los archivos cifrado y descifrado
        return (
            "✅ Proceso Fernet completado con éxito.\n"
            f" Archivo cifrado: {rutaCifrado}\n"
            f" Archivo descifrado: {rutaDescifrado}"
        )

    except Exception as e:
        # En caso de error inesperado, registrarlo y devolver un mensaje genérico
        logging.error(f"Error durante el proceso Fernet: {str(e)}")
        return "Ha ocurrido un error. Revisa el archivo 'logs/error.log' para más detalles."
