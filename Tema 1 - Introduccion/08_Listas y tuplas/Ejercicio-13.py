"""
Escribir un programa que pregunte por una muestra de números,
separados por comas, los guarde en una lista y muestre por pantalla su
media y desviación típica.
"""

"""
Fórmula de desviación típica
sqrt(sumatoria de (x-media)² / media)
"""

import math


listaNum = input("Dame una lista de números separados por comas: ")

arr = listaNum.split(",")

total = 0
count = 0
for n in arr:
    num = float(n)
    total += num
    count += 1

media = total / count
print(f"La media es {media:.2f}")

sumDesv = 0
for n in arr:
    num = float(n)
    sumDesv += math.pow(num - media, 2)

desv = math.sqrt(sumDesv / count)

print(f"La desviación típica es {desv:.2f}")  # :.2f muestra dos decimales
