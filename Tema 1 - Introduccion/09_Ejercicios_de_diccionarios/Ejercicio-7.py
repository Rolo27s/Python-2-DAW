"""
Escribir un programa que cree un diccionario simulando una cesta de la
compra. El programa debe preguntar el artículo y su precio y añadir el
par al diccionario, hasta que el usuario decida terminar. Después se
debe mostrar por pantalla la lista de la compra y el coste total, con el
siguiente formato:

Lista de la compra
Artículo 1  Precio
Artículo 2  Precio
Artículo 3  Precio
...         ...
Total       Coste
"""

lista_Compra = {}
continuar = True
total = 0

while continuar:
    key = input("Ingresa el nombre del artículo:")
    value = float(input("Ingresa el precio: "))
    lista_Compra[key] = value
    con = input("Continuar lista (Y/N): ")
    if con == "N" or con == "n":
        continuar = False

print("\nLista de la compra")
print("-------------------------------")
print("Artículo\t\t|\tPrecio")
print("-------------------------------")
for key, value in lista_Compra.items():
    print(f"{key.ljust(20)}\t|\t{str(value).rjust(6)}")
    total += value

print("-------------------------------")
print(f"Total\t\t\t|\t{str(total).rjust(6)}\n")
