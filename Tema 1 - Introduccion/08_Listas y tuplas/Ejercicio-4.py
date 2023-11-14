""" 
Escribir un programa que pregunte al usuario los números ganadores de
la lotería primitiva, los almacene en una lista y los muestre por pantalla
ordenados de menor a mayor.
"""

print("Dame los números ganadores de la lotería separados por un espacio: ")
numeros = input()

# Paso de cadena a lista con el separador espacio
numArr = numeros.split(" ")

# Por cada num en numArr, lo convierto a int
numArr = [int(num) for num in numArr]

# Ordeno el array. Por defecto de menor a mayor.
numArr.sort()

print(f"Los números ordenados de menor a mayor son: {numArr}")
