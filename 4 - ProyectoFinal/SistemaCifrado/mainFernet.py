# mainFernet.py
import os
from funciones import fernet

def ejecutarFernet(rutaArchivo):
    rutaClave = "claves/clave.key"
    os.makedirs("claves", exist_ok=True)

    try:
        # Verificar si la clave existe, si no, generar una nueva
        if not os.path.exists(rutaClave):
            clave = fernet.generarClave(rutaClave)
        else:
            clave = fernet.cargarClave(rutaClave)

        if not os.path.exists(rutaArchivo):
            return "El archivo a cifrar no existe."

        # Cifrar archivo
        rutaCifrado = fernet.cifrarArchivo(rutaArchivo, clave)

        # Descifrar archivo
        rutaDescifrado = fernet.descifrarArchivo(rutaCifrado, clave)

        return f"Cifrado y Descifrado Fernet completado.\n\nCifrado: {rutaCifrado}\nDescifrado: {rutaDescifrado}"

    except Exception as e:
        return f"Error durante el proceso Fernet: {str(e)}"
