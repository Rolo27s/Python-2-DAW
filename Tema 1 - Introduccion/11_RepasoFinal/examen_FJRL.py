# Alumno: Francisco José Rodríguez López
# 1. Lista de Meses salvo Diciembre
meses = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
]

# 2. Tupla que contiene las cifras de ventas mensuales introducidas por consola
cifra_ventas_tupla = tuple()

# Como una tupla es inmutable y no tiene metodo de adicion, voy a usar en primera instancia una lista para generar las cifras y finalmente convertiré esa lista a tupla para cumplir con el requisito del enunciado

cifra_venta_lista = list()

for mes in meses:
    cifra_mes = float(input(f"Ventas en {mes}: "))
    # Control de numero positivo
    while cifra_mes <= 0:
        print("Cifra introducida incorrecta. Vuelve a ingresar la cifra")
        cifra_mes = float(input(f"Ventas en {mes}: "))

    # Tras pasar el control agrego la cifra a la lista
    cifra_venta_lista.append(cifra_mes)

# Cuando tengo la lista de cifras completa, obtengo la tupla
cifra_ventas_tupla = tuple(cifra_venta_lista)
# print (type(cifra_ventas_tupla))

# 3. Creamos un diccionario que relacione el mes (key) con la cifra (value)
relacion_mes_cifra = dict()

for i in range(len(meses)):
    relacion_mes_cifra.update({meses[i]: cifra_ventas_tupla[i]})

# Reviso el diccionario (No es necesario en este momento pero compruebo que esté correcto el diccionario con su key, value)
# for key, val in relacion_mes_cifra.items():
#     print(f"Mes: {key} -> {val}")

# 4. Agrego el nuevo mes de diciembre a la lista y el valor de 12.000 a la tupla de cifras.
meses.append("Diciembre")

cifra_venta_lista.append(12000.0)
cifra_venta_tupla = tuple(cifra_venta_lista)

# 5. Inserto de manera manual el dato. También se podría agregar cogiendo la informacion de la lista meses y la tupla cifra_venta_tupla
relacion_mes_cifra.update({"Diciembre": 12000.0})

# 6., 7., 8. Calcula el total de ventas anuales y al mismo tiempo aprovecho el bucle para encontrar el precio mayor y el menor
total = 0
cifra_mayor = 0
cifra_menor = 10e1000
mes_mayor_cifra = ""
mes_menor_cifra = ""
for key, val in relacion_mes_cifra.items():
    total += val

    if val > cifra_mayor:
        cifra_mayor = val
        mes_mayor_cifra = key

    if val < cifra_menor:
        cifra_menor = val
        mes_menor_cifra = key

# 9. Imprime por consola el diccionario final
print("Mi diccionario de mes -> cifra")
print("------------------------------")
for key, val in relacion_mes_cifra.items():
    print(f"Mes: {key} -> {val}")

# Termino mostrando también la información recopilada de total, menor y mayor
print(f"\nTotal de ventas anual: {total}")
print(f"Mes con mayor volumen de ventas: {mes_mayor_cifra} -> {cifra_mayor}")
print(f"Mes con menor volumen de ventas: {mes_menor_cifra} -> {cifra_menor}")
