"""
6. Función para Calcular Descuentos en una Factura: Diseña una función llamada calcular_descuentos en Python que tome una lista de productos en una factura. Cada producto está representado como un diccionario con las claves 'nombre', 'precio' y 'cantidad'. La función deberá calcular el total de la factura después de aplicar un descuento del 10% a los productos cuya cantidad sea mayor a 5. Devuelve el total de la factura después de aplicar los descuentos. 
"""
productos = [
    {"nombre": "plátano", "precio": 2.78, "cantidad": 24},
    {"nombre": "sandia", "precio": 6.48, "cantidad": 3},
    {"nombre": "pera", "precio": 1.89, "cantidad": 12},
    {"nombre": "fresa", "precio": 3.28, "cantidad": 20},
]


def calcular_descuentos(lista):
    total = 0
    for producto in lista:
        # nombre = producto["nombre"]
        precio = producto["precio"]
        cantidad = producto["cantidad"]

        if cantidad > 5:
            total += (precio * 0.9) * cantidad
        else:
            total += precio * cantidad

    print(f"El total de la factura es {total:.2f}")
    return total


calcular_descuentos(productos)
