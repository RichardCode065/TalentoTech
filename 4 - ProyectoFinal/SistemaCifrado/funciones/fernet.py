# funciones/fernet.py
import os
from cryptography.fernet import Fernet

def generarClave(rutaDestino):
    clave = Fernet.generate_key()
    with open(rutaDestino, 'wb') as archivoClave:
        archivoClave.write(clave)
    return clave

def cargarClave(ruta):
    with open(ruta, 'rb') as archivo:
        return archivo.read()

def cifrarArchivo(rutaArchivo, clave):
    fernet = Fernet(clave)
    with open(rutaArchivo, 'rb') as file:
        datos = file.read()
    datosCifrados = fernet.encrypt(datos)
    rutaSalida = rutaArchivo.replace('.txt', 'Fernet.txt')
    with open(rutaSalida, 'wb') as file:
        file.write(datosCifrados)
    return rutaSalida

def descifrarArchivo(rutaArchivo, clave):
    fernet = Fernet(clave)
    with open(rutaArchivo, 'rb') as file:
        datosCifrados = file.read()
    datos = fernet.decrypt(datosCifrados)
    rutaSalida = rutaArchivo.replace('Fernet.txt', 'Descifrado.txt')
    with open(rutaSalida, 'wb') as file:
        file.write(datos)
    return rutaSalida
