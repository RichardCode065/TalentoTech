
from cryptography.fernet import Fernet
import os

# ------------------------
# Funciones de Seguridad
# ------------------------

def generarClave(carpeta="./"):
    "Genera una clave simétrica y la guarda en un archivo."
    clave = Fernet.generate_key()
    ruta = os.path.join(carpeta, "claveSimetrica.key")
    with open(ruta, "wb") as archivo:
        archivo.write(clave)
    print(f"Clave generada y guardada en: {ruta}")
    return ruta

def cargarClave(ruta="claveSimetrica.key"):
    "Carga una clave simétrica desde un archivo."
    if not os.path.exists(ruta):
        raise FileNotFoundError("No se encontró el archivo de clave.")
    with open(ruta, "rb") as archivo:
        return archivo.read()

def cifrarMensaje(mensaje, clave):
    "Cifra un mensaje en texto plano usando la clave dada."
    fernet = Fernet(clave)
    return fernet.encrypt(mensaje.encode())

def descifrarMensaje(mensaje_cifrado, clave):
    "Descifra un mensaje previamente cifrado."
    fernet = Fernet(clave)
    return fernet.decrypt(mensaje_cifrado).decode()

# ------------------------
# Menú Principal
# ------------------------

def menu():
    while True:
        print("\n---- SISTEMA DE CIFRADO SIMÉTRICO (FERNET) ----")
        print("1. Generar nueva clave")
        print("2. Cifrar un mensaje")
        print("3. Descifrar mensaje desde archivo")
        print("4. Salir")

        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            generarClave()
        
        elif opcion == "2":
            try:
                clave = cargarClave()
                mensaje = input("\nEscribe el mensaje que deseas cifrar:\n> ")
                mensajeCifrado = cifrarMensaje(mensaje, clave)

                with open("mensajeCifrado.txt", "wb") as file:
                    file.write(mensajeCifrado)
                
                print(f"\nMensaje cifrado guardado en 'mensajeCifrado.txt'")
                print(f"Resultado (base64): {mensajeCifrado.decode()}")

            except Exception as e:
                print(f"Error al cifrar: {e}")

        elif opcion == "3":
            try:
                clave = cargarClave()
                with open("mensaje_cifrado.txt", "rb") as file:
                    mensajeLeido = file.read()
                mensajeDescifrado = descifrarMensaje(mensajeLeido, clave)
                print(f"\n🔓 Mensaje descifrado:\n{mensajeDescifrado}")

            except Exception as e:
                print(f"Error al descifrar: {e}")

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    menu()
