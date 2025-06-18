# Función lambda para verificar si un número es primo
es_primo = lambda n: n > 1 and all(map(lambda x: n % x != 0, range(2, int(n**0.5) + 1)))

# Lista para almacenar los primeros 100 números primos
primos = []

# Contador que empieza desde 2 (el primer número primo)
numero = 2

# Bucle para encontrar los primeros 100 números primos
while len(primos) < 100:
    if es_primo(numero):
        primos.append(numero)
    numero += 1

# Imprimir el resultado
print("Los 100 primeros números primos:")
print(primos)