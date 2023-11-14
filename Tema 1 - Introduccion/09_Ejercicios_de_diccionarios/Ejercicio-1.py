"""
Escribir un programa que guarde en una variable el diccionario
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una
divisa y muestre su símbolo o un mensaje de aviso si la divisa no está
en el diccionario.
"""

TOT_DIV = {"Euro": "€", "Dollar": "$", "Yen": "¥"}

divisa = input("Dame una divisa (Euro, Dollar, Yen, ...): ")

# Inicializo divisa en no encontrada
encontrada = False

for i in TOT_DIV:
    # i esta revisando la información del key
    if i == divisa:
        print("Divisa encontrada: " + TOT_DIV[i])  # TOT_DIV[i] revisa el value
        encontrada = True

if encontrada == False:
    print(f"Divisa {divisa} no encontrada")
