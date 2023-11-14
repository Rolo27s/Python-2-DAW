"""
Escribir un programa que gestione las facturas pendientes de cobro de
una empresa. Las facturas se almacenarán en un diccionario donde la
clave de cada factura será el número de factura y el valor el coste de la
factura. ID_Factura -> coste_Factura

El programa debe preguntar al usuario si quiere añadir una
nueva factura, pagar una existente o terminar. 
    * Añadir
    * Pagar
    * Terminar (Salir del bucle)

Controles:
Si desea añadir una nueva factura se preguntará por el número de factura (ID) y su coste, y se añadirá al diccionario.

Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. 

Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
"""
# Con la funcion de Pagar se irá sumando esa cantidad al total_cobrado
total_cobrado = 0


def verFacturas():
    total_pendiente = sum(gestionFacturas.values())

    if not gestionFacturas:
        print("No hay facturas para mostrar.")
    else:
        print("Facturas pendientes:")
        for factura, costo in gestionFacturas.items():
            print(f"Factura con ID: {factura} y coste: {costo}")

    print(f"Total cobrado hasta el momento: {total_cobrado}")
    print(f"Total pendiente de cobro: {total_pendiente}")


# Inicializo el diccionario de facturas 'numeroFactura' : coste
gestionFacturas = {"0345": 23.32, "0032": 13.48, "0020": 44.56}

continuarBucle = True

print("Bienvenido a su gestor de facturas")
print("----------------------------------")
while continuarBucle:
    print("1. Ver facturas")
    print("2. Añadir factura")
    print("3. Pagar factura")
    print("4. Salir")
    opcion = int(input("Ingresa una opción: "))

    # Control del menu
    while opcion < 1 or opcion > 4:
        print("Opcion incorrecta")
        opcion = int(input("Ingresa una opción: "))

    # Parte del código que interacciona con el menu
    verFacturas()

    # Al final siempre se mostrarán todas las facturas

    # Salir del menu o volver al principio
    if opcion == 4:
        continuarBucle = False
