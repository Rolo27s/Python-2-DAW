""" 
Escribir un programa que pida al usuario una palabra y muestre por
pantalla si es un palíndromo. 
"""

palabra = input("Escribe una palabra: ")

# Guardo la palabra inicial
palabraInicial = palabra.lower()

# Invierto la palabra
palabra = palabra[::-1].lower()

if palabraInicial == palabra:
    print(f"La palabra {palabraInicial} es un palíndromo!")
else:
    print(f"La palabra {palabraInicial} no es un palíndromo ...")

""" Explicación detallada sobre [::-1]
Estableciendo los valores por defecto
start = None  # None indica el primer elemento
stop = None   # None indica el último elemento
step = -1     # -1 indica inverso

cadena_invertida = cadena[start:stop:step]
"""
