"""
Escribir un programa que cree un diccionario vacío y lo vaya llenado con
información sobre una persona (por ejemplo nombre, edad, sexo,
teléfono, correo electrónico, etc.) que se le pida al usuario. 

Cada vez que se añada un nuevo dato debe imprimirse el contenido del
diccionario.
"""

# Declaración de diccionario vacío por enunciado
mi_diccionario = {}

mi_diccionario["nombre"] = input("Ingresa el nombre: ")
print(f"Nombre ingresado: {mi_diccionario['nombre']}")
print("\n")
print(mi_diccionario)
print("\n")

mi_diccionario["apellido"] = input("Ingresa el apellido: ")
print(f"Apellido ingresado: {mi_diccionario['apellido']}")
print("\n")
print(mi_diccionario)
print("\n")

mi_diccionario["edad"] = input("Ingresa tu edad: ")
print(f"Edad ingresada: {mi_diccionario['edad']}")
print("\n")
print(mi_diccionario)
print("\n")

mi_diccionario["sexo"] = input("Ingresa el sexo: ")
print(f"Sexo ingresado: {mi_diccionario['sexo']}")
print("\n")
print(mi_diccionario)
print("\n")

mi_diccionario["telf"] = input("Ingresa el teléfono: ")
print(f"Teléfono ingresado: {mi_diccionario['telf']}")
print("\n")
print(mi_diccionario)
print("\n")

mi_diccionario["email"] = input("Ingresa el email: ")
print(f"Email ingresado: {mi_diccionario['email']}")
print("\n")
print(mi_diccionario)
print("\n")
