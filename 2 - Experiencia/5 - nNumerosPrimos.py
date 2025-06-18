def esPrimo(num):
    "Verifica si un número es primo."
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primerosNumerosPrimos(n):
    "Devuelve una lista con los primeros 'n' números primos."
    primos = []
    numero = 2
    while len(primos) < n:
        if esPrimo(numero):
            primos.append(numero)
        numero += 1
    return primos

# Entrada del usuario con validación
try:
    n = int(input("¿Cuántos números primos deseas obtener? "))
    if n <= 0:
        print("Por favor ingresa un número mayor que 0.")
    else:
        resultado = primerosNumerosPrimos(n)
        print(f"\nLos primeros {n} números primos son:\n{resultado}")
except ValueError:
    print("Entrada no válida. Debes ingresar un número entero.")