"""
Escribir un programa que guarde en un diccionario los precios de las
frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y
muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta
no está en el diccionario debe mostrar un mensaje informando de ello.

Fruta   |   Precio
Plátano |   1.35
Manzana |   0.80
Pera    |   0.85
Naranja |   0.70
"""

Frutas = {"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}

fruta = input("Dame una fruta (en singular): ")
# Me aseguro de que tenga el formato Mayus_minus correcto
fruta = fruta.title()

encontrado = False

for x in Frutas:
    if x == fruta:
        encontrado = True
        print(f"Tengo {x}s")
        cantidad = input("¿Cuantos kilos quieres?: ")
        print(
            f"Marchando {cantidad} Kilos de {fruta}. Son {(float(cantidad) * float(Frutas[x])):.2f} euros. Vuelva pronto!"
        )

if encontrado == False:
    print("Fruta no encontrada")
