"""
Escribir un programa que almacene en una lista los siguientes precios,
50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de
los precios.
"""

precios = [50, 75, 46, 22, 80, 65, 8]

# Ordeno el array de menor a mayor
precios.sort()

print (f"El precio menor es {precios[0]} y el mayor es {precios[-1]}")
