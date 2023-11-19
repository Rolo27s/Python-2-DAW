"""
Crea un programa que solicite al usuario ingresar el nombre y la edad de varias personas. Almacenar esta información en un diccionario donde el nombre es la clave y la edad es el valor. Luego, crea un conjunto (set) que contenga solo los nombres de las personas menores de 25 años.
"""
listado = dict()

while True:
    newName = (input("Ingresa el nombre de una nueva persona:")).upper()
    if newName in listado.keys():
        print(f"Nombre {newName} ya incluido en el listado")
    else:
        newAge = input("Ingresa la edad de esa persona:")
        listado.update({newName: newAge})

    option = input("Quieres terminar el listado? (S/N): ")
    if option == "S" or option == "s":
        break

print(listado)

conjunto = set()
for k, v in listado.items():
    if int(v) < 25:
        conjunto.add(k)

print(f"Personas menores de 25 años: {conjunto}")
