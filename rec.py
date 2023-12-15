"""Examen práctico de Python:

Tienes que trabajar con datos que representan el volumen de ventas mensuales de una tienda durante un año.

1) Crea un SET que contenga los nombres de todos los meses en orden (los meses no se piden por consola) (1 punto)

2) Implementa una función llamada ingresar_ventas_mensuales que, mediante un bucle, solicite al usuario que ingrese las cifras de venta mes a mes. Asegúrate de validar que el valor introducido sea un número positivo. La función debe devolver la lista de ventas mensuales. (2 puntos)

3) Genera una función llamada crear_diccionario_ventas que tome la lista de meses y la lista de ventas mensuales como argumentos y devuelva un diccionario donde las claves sean los nombres de los meses y los valores sean las cifras de ventas correspondientes. (2 puntos)

4) Calcula e imprime por consola el total de las ventas anuales utilizando una función llamada calcular_total_ventas. La función debe tomar el diccionario de ventas como argumento y devolver el total. (1 puntos)

5) Encuentra e imprime por consola el mes con el mayor volumen de ventas utilizando una función llamada mes_con_mayor_ventas. La función debe tomar el diccionario de ventas como argumento y devolver nombre y valor de ventas con mayor volumen. (1 puntos)

6) Encuentra e imprime por consola el mes con el menor volumen de ventas utilizando una función llamada mes_con_menor_ventas. La función debe tomar el diccionario de ventas como argumento y devolver el nombre del mes y el valor de ventas con el menor volumen. (1 puntos)

7) Imprime por consola el diccionario final de manera clara y legible. (2 puntos)
"""

# Punto 1
meses = {
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
    "Diciembre",
}


# Punto 2
def ingresar_ventas_mensuales(meses):
    ventas = []
    for mes in meses:
        # Posible implementación de control con try - except
        cifra = float(
            input(f"Ingresa cifra de ventas del mes de {mes}: ")
        )  # El uso del decimal en python recuerdo que es el punto '.'. La coma daría error de formato. (EN JAVA ES AL REVÉS)
        ventas.append(cifra)

    return ventas


# Defino ventas en el scope global usando la funcion correspondiente
ventas = ingresar_ventas_mensuales(meses)


# Punto 3
def crear_diccionario_ventas(meses, ventas):
    dicc = {}
    i = 0
    for mes in meses:
        # print(mes, ventas[i])
        dicc.update({mes: ventas[i]})
        i += 1

    # print(dicc)
    return dicc


dicc = crear_diccionario_ventas(meses, ventas)


# Punto 4
def calcular_total_ventas(dicc):
    total = 0
    for i in dicc.values():
        total += i

    print(f"Total de ventas: {total}")
    return total


total_de_ventas = calcular_total_ventas(dicc)


# Punto 5
def mes_con_mayor_ventas(dicc):
    mayorMes = ""
    mayorMesCifra = 0
    for k, v in dicc.items():
        # print(k, v)
        if v > mayorMesCifra:
            mayorMesCifra = v
            mayorMes = k
            # En caso de que fuera igual y hubiera meses con la misma cifra, quedará guardado en memoria el primer mes ingresado con esa cantidad de volumen
            listMes = [k, v]

    print(f"Mayores ventas en {listMes[0]} con un total de {listMes[1]}")

    return listMes


maximo = mes_con_mayor_ventas(dicc)


# Punto 6
def mes_con_menor_ventas(dicc):
    menorMes = ""
    valores = list(dicc.values())
    menorMesCifra = valores[0]
    for k, v in dicc.items():
        # print(k, v)
        if v < menorMesCifra:
            menorMesCifra = v
            menorMes = k
            # En caso de que fuera igual y hubiera meses con la misma cifra, quedará guardado en memoria el primer mes ingresado con esa cantidad de volumen
            listMes = [k, v]

    print(f"Menores ventas en {listMes[0]} con un total de {listMes[1]}")

    return listMes


minimo = mes_con_menor_ventas(dicc)

# Punto 7
print(f"\n\nDiccionario:")
for mes, cifra in dicc.items():
    print(f"{mes} - {cifra}")
