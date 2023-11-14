# Hola mundo en Python
print("Hola Mundo")

# Definiendo variables en Python
x = 5
print(x)

# Sumando variables en Python
a = 3
b = 7
print(f"La suma de {a} + {b} es {a+b}")

# Otra manera es:
# print("La suma de {} + {} es {}".format(a, b, a + b))

# Ejemplo condicional
a = 10
if a == 10:
    print("Es 10")
else:
    print("No es 10")

# Decimales y cadenas
valor_decimal = 10.3234
mi_cadena = "Hola Mundo"

# --- EJEMPLO DE OPERACIÓN ARITMÉTICA ---
# Definimos una variable x con una cadena
x = "El valor de (a+b)*c es"

# Podemos realizar múltiples asignaciones
a, b, c = 4, 3, 2

# Realizamos unas operaciones con a,b,c
d = (a + b) * c

# Definimos una variable booleana
imprimir = True

# Si imprimir, print()
if imprimir:
    print(x, d)

# Salida: El valor de (a+b)*c es 14

'''
Esto es un comentario
de varias líneas
de código
'''

# Identación y bloques de código
if True:
    print("True")

# Múltiples líneas. 
'''
Haciendo uso de \ se puede romper el código en varias líneas, 
lo que en determinados casos hace que el código sea mucho más legible.
'''
x = 1 + 2 + 3 + 4 +\
    5 + 6 + 7 + 8

# Otra opción
x = (1 + 2 + 3 + 4 +
     5 + 6 + 7 + 8)

# Se puede hacer lo mismo para llamadas a funciones
def funcion(a, b, c):
    return a+b+c

d = funcion(10,
23,
3)

# Creando variables
x = y = z = 10
x, y = 4, 2
x, y, z = 1, 2, 3

# Nombrando variables. 
# 1. Es sensitive case.
# 2. No se permite - ni espacios
# 3. No se puede empezar por un número

# No usar nombres reservados
import keyword
print(keyword.kwlist)

# Lista de palabras reservadas:
'''
['False', 'None', 'True', 'and', 'as', 'assert',
'async', 'await', 'break', 'class', 'continue',
'def', 'del', 'elif', 'else', 'except', 'finally',
'for', 'from', 'global', 'if', 'import', 'in', 'is',
'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
'return', 'try', 'while', 'with', 'yield']
'''

# Print texto y numeros
x = 10
y = 20
print("Los valores x, y son:", x, y)
# Salida: Los valores x, y son: 10 20

# ------------------------------------

# Condicionales: if, elif, else (Switch case en Python no existe)
lenguaje = "Python"

if lenguaje == "Python":
    print("Estoy de acuerdo, Python es el mejor")
elif lenguaje == "Java":
    print("No me gusta, Java no mola")
else:
    print("Ningún otro lenguaje supera a Python")

# Salida: Estoy de acuerdo, Python es el mejor

# Bucles: while, for, break, continue
x = 0
while x < 3:
    print(x)
    x += 1

# Salida: 0, 1, 2

for i in range(3):
    print(i)

# Salida: 0, 1, 2

# Funcion lambda (anónima)
print("La suma es", (lambda a, b: a + b)(3, 5))

# Me quedo en pass y yield