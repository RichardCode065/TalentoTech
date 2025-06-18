import os
import logging
from funciones import vigenere  # Importa el módulo que contiene las funciones relacionadas con el algoritmo Vigenère

# Asegurar que exista la carpeta de logs para registrar posibles errores
os.makedirs("logs", exist_ok=True)

# Configuración básica del sistema de logging
logging.basicConfig(
    filename='logs/error.log',             # Archivo donde se almacenarán los errores
    level=logging.ERROR,                   # Nivel de severidad de los mensajes que se registrarán (solo errores)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato del mensaje de error
)

def ejecutarVigenere(rutaArchivo, clave):
    """ Ejecuta el proceso de cifrado y descifrado Vigenère sobre un archivo.
    Parámetros:
        rutaArchivo (str): Ruta del archivo a cifrar/descifrar.
        clave (str): Clave utilizada para el cifrado Vigenère.
    Retorna:
        str: Mensaje con los resultados o los errores del proceso.
    """

    # Validar si la ruta del archivo existe
    if not os.path.exists(rutaArchivo):
        mensaje = "El archivo no existe."
        logging.error(mensaje)  # Registrar el error en el log
        return mensaje

    try:
        # Obtener la extensión del archivo (.txt, .pdf, .docx)
        ext = os.path.splitext(rutaArchivo)[1].lower()

        # Leer el contenido del archivo dependiendo del tipo
        texto = vigenere.leerArchivo(rutaArchivo)
        if not texto:
            mensaje = "El archivo está vacío o no pudo ser leído."
            logging.error(mensaje)
            return mensaje

        # Cifrado con Vigenère
        cifrado = vigenere.cifrarVigenere(texto, clave)
        rutaCifrado = rutaArchivo.rsplit('.', 1)[0] + "_Vigenere" + ext  # Ruta para guardar el archivo cifrado
        vigenere.guardarArchivo(cifrado, rutaCifrado)

        # Descifrado para verificación
        descifrado = vigenere.descifrarVigenere(cifrado, clave)
        rutaDescifrado = rutaArchivo.rsplit('.', 1)[0] + "_Vigenere_Descifrado" + ext  # Ruta para guardar el descifrado
        vigenere.guardarArchivo(descifrado, rutaDescifrado)

        # Retorna un mensaje exitoso con las rutas de los archivos generados
        return (
            "✅ Proceso Vigenère completado con éxito.\n"
            f"Archivo cifrado: {rutaCifrado}\n"
            f"Archivo descifrado: {rutaDescifrado}"
        )

    except Exception as e:
        # Captura cualquier error inesperado, lo registra en el log y muestra un mensaje general al usuario
        logging.error(f"Error durante el proceso Vigenère: {str(e)}")
        return "Ha ocurrido un error. Revisa el archivo 'logs/error.log' para más detalles."