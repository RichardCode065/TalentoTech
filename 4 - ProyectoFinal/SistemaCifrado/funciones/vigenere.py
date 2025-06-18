# funciones/vigenere.py

def cifrar_vigenere(texto, clave):
    """
    Cifra un texto usando el cifrado Vigenère.

    Parámetros:
    texto (str): Texto plano que se desea cifrar.
    clave (str): Clave utilizada para el cifrado.

    Retorna:
    str: Texto cifrado.
    """
    texto_cifrado = ""
    clave = clave.upper()
    clave_index = 0

    for caracter in texto:
        if caracter.isalpha():
            offset = 65 if caracter.isupper() else 97
            letra_clave = clave[clave_index % len(clave)]
            letra_clave_offset = ord(letra_clave.upper()) - 65
            nueva_letra = chr((ord(caracter) - offset + letra_clave_offset) % 26 + offset)
            texto_cifrado += nueva_letra
            clave_index += 1
        else:
            texto_cifrado += caracter

    return texto_cifrado


def descifrar_vigenere(texto_cifrado, clave):
    """
    Descifra un texto usando el cifrado Vigenère.

    Parámetros:
    texto_cifrado (str): Texto cifrado que se desea descifrar.
    clave (str): Clave utilizada para el descifrado (la misma que para cifrar).

    Retorna:
    str: Texto descifrado.
    """
    texto_descifrado = ""
    clave = clave.upper()
    clave_index = 0

    for caracter in texto_cifrado:
        if caracter.isalpha():
            offset = 65 if caracter.isupper() else 97
            letra_clave = clave[clave_index % len(clave)]
            letra_clave_offset = ord(letra_clave.upper()) - 65
            nueva_letra = chr((ord(caracter) - offset - letra_clave_offset) % 26 + offset)
            texto_descifrado += nueva_letra
            clave_index += 1
        else:
            texto_descifrado += caracter

    return texto_descifrado
