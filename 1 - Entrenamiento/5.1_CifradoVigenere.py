from string import ascii_uppercase

# ----- VIGENÈRE CON DICCIONARIO -----

def crearTablaVigenere():
    tabla = {}
    alfabeto = ascii_uppercase
    for i, letra in enumerate(alfabeto):
        fila = alfabeto[i:] + alfabeto[:i]
        tabla[letra] = fila
    return tabla

def cifrarVigenereDiccionario(texto, clave):
    tabla = crearTablaVigenere()
    texto = texto.upper()
    clave = clave.upper()
    resultado = []

    for i, letra in enumerate(texto):
        if letra in ascii_uppercase:
            fila = tabla[clave[i % len(clave)]]
            columna = ascii_uppercase.index(letra)
            resultado.append(fila[columna])
        else:
            resultado.append(letra)
    return ''.join(resultado)

def descifrarVigenereDiccionario(textoCifrado, clave):
    tabla = crearTablaVigenere()
    textoCifrado = textoCifrado.upper()
    clave = clave.upper()
    resultado = []

    for i, letra in enumerate(textoCifrado):
        if letra in ascii_uppercase:
            fila = tabla[clave[i % len(clave)]]
            columna = fila.index(letra)
            resultado.append(ascii_uppercase[columna])
        else:
            resultado.append(letra)
    return ''.join(resultado)

# ----- VIGENÈRE SIN DICCIONARIO -----

def cifrarVigenereSinDiccionario(texto, clave):
    resultado = []
    clave = clave.upper()
    n = len(clave)

    for i, letra in enumerate(texto):
        shift = ord(clave[i % n]) - ord('A')
        if letra.isupper():
            cifrado = (ord(letra) - ord('A') + shift) % 26 + ord('A')
            resultado.append(chr(cifrado))
        elif letra.islower():
            cifrado = (ord(letra) - ord('a') + shift) % 26 + ord('a')
            resultado.append(chr(cifrado))
        else:
            resultado.append(letra)
    return ''.join(resultado)

def descifrarVigenereSinDiccionario(textoCifrado, clave):
    resultado = []
    clave = clave.upper()
    n = len(clave)

    for i, letra in enumerate(textoCifrado):
        shift = ord(clave[i % n]) - ord('A')
        if letra.isupper():
            original = (ord(letra) - ord('A') - shift) % 26 + ord('A')
            resultado.append(chr(original))
        elif letra.islower():
            original = (ord(letra) - ord('a') - shift) % 26 + ord('a')
            resultado.append(chr(original))
        else:
            resultado.append(letra)
    return ''.join(resultado)

# ========== MENÚ INTERACTIVO ==========

def menu():
    print("\n-------------------------------------")
    print("\n----- Cifrado Vigenère -----")
    print("1. Cifrar usando diccionario")
    print("2. Descifrar usando diccionario")
    print("3. Cifrar sin diccionario (ASCII)")
    print("4. Descifrar sin diccionario (ASCII)")
    print("5. Salir")
    print("-------------------------------------")

def solicitarTextoClave():
    Texto = input("Ingresa el mensaje: ")
    Clave = input("Ingresa la clave (solo letras): ").upper()
    while not Clave.isalpha():
        Clave = input("La clave debe contener solo letras. Intenta de nuevo: ").upper()
    return Texto, Clave

def main():
    while True:
        menu()
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion in ['1', '2', '3', '4']:
            Texto, Clave = solicitarTextoClave()

            if opcion == '1':
                resultado = cifrarVigenereDiccionario(Texto, Clave)
                print("Mensaje cifrado (diccionario):", resultado)
            elif opcion == '2':
                resultado = descifrarVigenereDiccionario(Texto, Clave)
                print("Mensaje descifrado (diccionario):", resultado)
            elif opcion == '3':
                resultado = cifrarVigenereSinDiccionario(Texto, Clave)
                print("Mensaje cifrado (ASCII):", resultado)
            elif opcion == '4':
                resultado = descifrarVigenereSinDiccionario(Texto, Clave)
                print("Mensaje descifrado (ASCII):", resultado)

        elif opcion == '5':
            print("Gracias por usar el cifrado de Vigenère.")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    main()