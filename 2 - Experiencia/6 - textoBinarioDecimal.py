#D Función que convierte texto a binario (8 bits por carácter)
def textoBinario(texto):
    return ' '.join(format(ord(c), '08b') for c in texto)

# Función que convierte binario a lista de decimales
def binarioDecimal(binario):
    binarios = binario.strip().split()
    return [int(b, 2) for b in binarios]

# Función que convierte una lista de decimales a texto
def decimalTexto(decimales):
    return ''.join(chr(d) for d in decimales)

# Interfaz de usuario
if __name__ == "__main__":
    print("----- Conversor de Texto a Binario y Decimal -----")
    mensaje = input("Introduce un mensaje de texto: ")

    # 1. Texto a binario
    binario = textoBinario(mensaje)
    print(f"\nTexto en binario:\n{binario}")

    # 2. Binario a decimal
    decimales = binarioDecimal(binario)
    print(f"\nTexto en formato decimal:\n{decimales}")

    # 3. Decimal a texto (recuperación)
    mensajeRecuperado = decimalTexto(decimales)
    print(f"\n Mensaje recuperado desde decimal:\n{mensajeRecuperado}")