# mainFernet.py
from funciones import fernet
import os

def main():
    rutaArchivo = "documentos/texto.txt"
    rutaClave = "claves/clave.key"

    # Verificar si existe la clave, si no se genera
    if not os.path.exists(rutaClave):
        print("Clave no encontrada, generando nueva...")
        os.makedirs("claves", exist_ok=True)
        clave = fernet.generarClave(rutaClave)
    else:
        clave = fernet.cargarClave(rutaClave)

    if not os.path.exists(rutaArchivo):
        print("El archivo a cifrar no existe.")
        return

    rutaCifrado = fernet.cifrarArchivo(rutaArchivo, clave)
    print(f"Archivo cifrado: {rutaCifrado}")

    ruta_descifrado = fernet.descifrar_archivo(rutaCifrado, clave)
    print(f"Archivo descifrado: {ruta_descifrado}")

if __name__ == "__main__":
    main()
