# main.py
from funciones import vigenere
import os

def main():
    archivo = "documentos/texto.txt"
    clave = "CLAVE"

    if not os.path.exists(archivo):
        print("El archivo no existe.")
        return

    with open(archivo, 'r', encoding='utf-8') as f:
        texto = f.read()

    cifrado = vigenere.cifrar_vigenere(texto, clave)
    with open("documentos/textoVigenere.txt", 'w', encoding='utf-8') as f:
        f.write(cifrado)

    descifrado = vigenere.descifrar_vigenere(cifrado, clave)
    with open("documentos/textoDescifrado.txt", 'w', encoding='utf-8') as f:
        f.write(descifrado)

    print("Cifrado y descifrado Vigenère completado.")

if __name__ == "__main__":
    main()

