# main.py
import os
from funciones import vigenere

def ejecutarVigenere(rutaArchivo, clave):
    if not os.path.exists(rutaArchivo):
        return "El archivo no existe."

    try:
        # Leer contenido según tipo de archivo
        texto = vigenere.leerArchivo(rutaArchivo)
        if not texto:
            return "El archivo está vacío o no pudo ser leído."

        # Cifrado
        cifrado = vigenere.cifrarVigenere(texto, clave)
        rutaCifrado = rutaArchivo.rsplit('.', 1)[0] + "_Vigenere.txt"
        vigenere.guardarArchivo(cifrado, rutaCifrado)

        # Descifrado
        descifrado = vigenere.descifrarVigenere(cifrado, clave)
        rutaDescifrado = rutaArchivo.rsplit('.', 1)[0] + "_Vigenere_Descifrado.txt"
        vigenere.guardarArchivo(descifrado, rutaDescifrado)

        return f"Cifrado y Descifrado Vigenère completado.\n\nCifrado: {rutaCifrado}\nDescifrado: {rutaDescifrado}"

    except Exception as e:
        return f"Error durante el proceso Vigenère: {str(e)}"
