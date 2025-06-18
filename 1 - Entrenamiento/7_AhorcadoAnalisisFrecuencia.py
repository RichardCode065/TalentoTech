import random
from collections import Counter

simbolos = '><(((º>'  # Solo se usa para contar errores

def bienvenida():
    print('*' * 68)
    print('* Te doy la bienvenida al juego del ahorcado con IA de frecuencia :) *')
    print('*' * 68)

def inicializar_juego(diccionario):
    palabra = random.choice(diccionario).lower()
    tablero = ['_'] * len(palabra)
    return tablero, palabra, []

def mostrar_tablero(tablero, letras_erroneas):
    print("\nPalabra:", ' '.join(tablero))
    if letras_erroneas:
        print('Letras erróneas:', ', '.join(letras_erroneas))
    print(f'Errores: {len(letras_erroneas)} de {len(simbolos)}\n')

def obtener_frecuencia_letras(diccionario, letras_usadas):
    """
    Retorna las letras más frecuentes del diccionario excluyendo las ya usadas.
    """
    texto = ''.join(diccionario)
    frecuencias = Counter(texto)
    for letra in letras_usadas:
        frecuencias.pop(letra, None)
    return sorted(frecuencias.items(), key=lambda item: item[1], reverse=True)

def sugerir_letra(diccionario, letras_usadas):
    """
    Sugerencia basada en análisis de frecuencia.
    """
    frecuencias = obtener_frecuencia_letras(diccionario, letras_usadas)
    return frecuencias[0][0] if frecuencias else ''

def pedir_letra(tablero, letras_erroneas, diccionario):
    letras_usadas = tablero + letras_erroneas
    sugerencia = sugerir_letra(diccionario, letras_usadas)
    print(f"Sugerencia inteligente: prueba con la letra '{sugerencia}'")
    while True:
        letra = input('Introduce una letra (a-z): ').lower()
        if not (len(letra) == 1 and letra.isalpha()):
            print('Error, la letra debe ser una sola entre a-z.')
        elif letra in letras_usadas:
            print('Letra repetida, prueba con otra.')
        else:
            return letra

def procesar_letra(letra, palabra, tablero, letras_erroneas):
    if letra in palabra:
        print(f'✅ ¡Bien! La letra "{letra}" está en la palabra.')
        actualizar_tablero(letra, palabra, tablero)
    else:
        print(f'❌ La letra "{letra}" no está en la palabra.')
        letras_erroneas.append(letra)

def actualizar_tablero(letra, palabra, tablero):
    for i, letra_real in enumerate(palabra):
        if letra == letra_real:
            tablero[i] = letra

def comprobar_palabra(tablero):
    return '_' not in tablero

def jugar_al_ahorcado(diccionario):
    tablero, palabra, letras_erroneas = inicializar_juego(diccionario)
    while len(letras_erroneas) < len(simbolos):
        mostrar_tablero(tablero, letras_erroneas)
        letra = pedir_letra(tablero, letras_erroneas, diccionario)
        procesar_letra(letra, palabra, tablero, letras_erroneas)
        if comprobar_palabra(tablero):
            print(f'🎉 ¡Ganaste! La palabra era: {palabra}')
            break
    else:
        print(f'💀 ¡Perdiste! La palabra era: {palabra}')
    mostrar_tablero(tablero, letras_erroneas)

def jugar_otra_vez():
    return input('¿Deseas jugar otra vez? (s/n): ').lower() == 's'

def despedida():
    print('*' * 68)
    print('* Gracias por jugar al ahorcado inteligente. ¡Hasta pronto! *')
    print('*' * 68)

if __name__ == '__main__':
    diccionario = [
    'firewall', 'malware', 'phishing', 'ransomware', 'spyware',
    'antivirus', 'criptografia', 'vpn', 'puerto', 'exploit',
    'hacker', 'token', 'rootkit', 'proxy', 'backdoor',
    'ingenieriasocial', 'sniffer', 'cifrado', 'autenticacion', 'vulnerabilidad'
]
    
    bienvenida()
    while True:
        jugar_al_ahorcado(diccionario)
        if not jugar_otra_vez():
            break
    despedida()