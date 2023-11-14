""" 
Escribir un programa que pida al usuario una palabra y muestre por
pantalla el número de veces que contiene cada vocal.
"""

palabra = input("Introduce una palabra: ")

palabra = palabra.lower()

# Fuerzo a list para tener un key, value por separado. Se podría usar diccionario en este caso.

countKey = ["a", "e", "i", "o", "u"]
# Array para contar las letras.
countVal = [0, 0, 0, 0, 0]

# Paso el string de la palabra a un array para ir leyendo carácter a carácter
descPalabra = list(palabra)

for letra in descPalabra:
    if letra == "a":
        countVal[0] = countVal[0] + 1
    if letra == "e":
        countVal[1] = countVal[1] + 1
    if letra == "i":
        countVal[2] = countVal[2] + 1
    if letra == "o":
        countVal[3] = countVal[3] + 1
    if letra == "u":
        countVal[4] = countVal[4] + 1

for i in range(5):
    print (f"La vocal {countKey[i]} apareció {countVal[i]}")
