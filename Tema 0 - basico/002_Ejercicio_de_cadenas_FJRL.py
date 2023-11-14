# Ejercicio de Cadenas

""" Ejercicio 1
Escribir un programa que pregunte el nombre del usuario en la consola
y un número entero e imprima por pantalla en líneas distintas el nombre
del usuario tantas veces como el número introducido. """


def ejercicio1():
    print("Ejercicio 1")
    print("-----------")

    nombre = input("Introduce tu nombre: ")
    numero = input("Cuantas veces quieres verlo en pantalla?: ")
    numero = int(numero)

    if numero > 0:
        for i in range(0, numero):
            print(nombre)
    else:
        print("Error en la entrada de datos. Los datos no pueden ser negativos ni cero")


# Descomentar ejecución de función para comprobar el resultado del ejercicio
# ejercicio1()

""" Ejercicio 2
Escribir un programa que pregunte el nombre completo del usuario en la
consola y después muestre por pantalla el nombre completo del usuario
tres veces, una con todas las letras minúsculas, otra con todas las letras
mayúsculas y otra solo con la primera letra del nombre y de los apellidos
en mayúscula. El usuario puede introducir su nombre combinando
mayúsculas y minúsculas como quiera. """


def ejercicio2():
    print("Ejercicio 2")
    print("-----------")

    nombre = input("Introduce tu nombre completo: ")

    print("Tu nombre completo es: " + nombre.lower())
    print("Tu nombre completo es: " + nombre.upper())
    print("Tu nombre completo es: " + nombre.title())


# Descomentar ejecución de función para comprobar el resultado del ejercicio
# ejercicio2()

""" Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola
y después de que el usuario lo introduzca muestre por pantalla <NOMBRE>
tiene <n> letras, donde <NOMBRE> es el nombre de usuario en
mayúsculas y <n> es el número de letras que tienen el nombre. """


def ejercicio3():
    print("Ejercicio 3")
    print("-----------")

    nombre = input("Introduce tu nombre: ")
    print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")


# Descomentar ejecución de función para comprobar el resultado del ejercicio
# ejercicio3()


""" Ejercicio 4
Los teléfonos de una empresa tienen el siguiente formato
prefijo-número-extension donde el prefijo es el código del país +34, y
la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir
un programa que pregunte por un número de teléfono con este formato
y muestre por pantalla el número de teléfono sin el prefijo y la extensión. """


def ejercicio4():
    print("Ejercicio 4")
    print("-----------")

    numero = input("Introduce el número de teléfono (formato +34-913724710-56): ")

    import re

    # Patrón de expresión regular
    patron = r"^\+\d{2}-\d{9}-\d{2}$"

    # Comprobar si la cadena coincide con el patrón
    if re.match(patron, numero):
        print("La cadena es válida.")
        print(
            "El número de teléfono sin el prefijo es: " + numero.split("-")[1]
        )  # Recorto por el símbolo - que se guarda en un array, y me quedo con el segundo elemento del array en la posición 1, que es el número.
    else:
        print("La cadena no es válida.")


# Descomentar ejecución de función para comprobar el resultado del ejercicio
# ejercicio4()

""" Ejercicio 5
Escribir un programa que pida al usuario que introduzca una frase en la
consola y muestre por pantalla la frase invertida. """


def ejercicio5():
    print("Ejercicio 5")
    print("-----------")

    frase = input("Introduce una frase: ")
    print(frase[::-1])


# Descomentar ejecución de función para comprobar el resultado del ejercicio
# ejercicio5()

""" Ejercicio 6
Escribir un programa que pida al usuario que introduzca una frase en la
consola y una vocal, y después muestre por pantalla la misma frase
pero con la vocal introducida en mayúscula. """


def ejercicio6():
    print("Ejercicio 6")
    print("-----------")

    frase = input("Introduce una frase: ")
    vocal = input("Introduce una vocal: ")

    print(frase.replace(vocal, vocal.upper()))


# Descomentar ejecución de función para comprobar el resultado del ejercicio
# ejercicio6()

""" Ejercicio 7
Escribir un programa que pregunte el correo electrónico del usuario en
la consola y muestre por pantalla otro correo electrónico con el mismo
nombre (la parte delante de la arroba @) pero con dominio
iesgbrenan.com. """


def ejercicio7():
    print("Ejercicio 7")
    print("-----------")

    correo = input("Introduce tu correo electrónico: ")
    correo = correo.split("@")[0]
    correo += "@iesgbrenan.com"
    print(correo)


# Descomentar ejecución de función para comprobar el resultado del ejercicio
# ejercicio7()

""" Ejercicio 8
Escribir un programa que pregunte por consola el precio de un producto
en euros con dos decimales y muestre por pantalla el número de euros
y el número de céntimos del precio introducido. """


def ejercicio8():
    print("Ejercicio 8")
    print("-----------")

    precio = input(
        "Introduce el precio del producto con dos decimales (Ejemplo 14.89): "
    )
    parteEntera = precio.split(".")[0]
    parteDecimal = precio.split(".")[1]

    print("El número de euros es: " + parteEntera)
    print("El número de céntimos es: " + parteDecimal)


# Descomentar ejecución de función para comprobar el resultado del ejercicio
# ejercicio8()

""" Ejercicio 9
Escribir un programa que pregunte al usuario la fecha de su nacimiento
en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
Adaptar el programa anterior para que también funcione cuando el día o
el mes se introduzcan con un solo carácter. """


def ejercicio9():
    print("Ejercicio 9")
    print("-----------")

    fecha = input("Introduce la fecha de su nacimiento (dd/mm/aaaa): ")
    dia = fecha.split("/")[0]
    mes = fecha.split("/")[1]
    año = fecha.split("/")[2]

    print("El día es: " + dia)
    print("El mes es: " + mes)
    print("El año es: " + año)


# Descomentar ejecución de función para comprobar el resultado del ejercicio
# ejercicio9()


""" Ejercicio 10
Escribir un programa que pregunte por consola por los productos de una
cesta de la compra, separados por comas, y muestre por pantalla cada
uno de los productos en una línea distinta. """


def ejercicio10():
    print("Ejercicio 10")
    print("-----------")

    productos = input("Introduce los productos de la compra separados por comas: ")
    productos = productos.split(",")

    print("Lista de la compra: ")
    for producto in productos:
        print(producto)


# Descomentar ejecución de función para comprobar el resultado del ejercicio
# ejercicio10()

""" Ejercicio 11
Escribir un programa que pregunte el nombre el un producto, su precio y
un número de unidades y muestre por pantalla una cadena con el
nombre del producto seguido de su precio unitario con 6 dígitos enteros
y 2 decimales, el número de unidades con tres dígitos y el coste total
con 8 dígitos enteros y 2 decimales. """


def ejercicio11():
    print("Ejercicio 11")
    print("-----------")

    producto = input("Introduce el nombre del producto: ")
    precio = float(input("Introduce el precio del producto: "))
    unidades = int(input("Introduce el número de unidades: "))

    coste_total = float(precio) * float(unidades)

    print("\n")

    # Formatear la cadena de salida
    cadena_resultado = f"Nombre del producto: {producto}\n"
    cadena_resultado += f"Precio unitario: {precio:09.2f}\n"  # 06.2f significa 9 caracteres en total (incluye el punto) y rellena con ceros y dos dígitos en la parte decimal.
    cadena_resultado += f"Número de unidades: {unidades:03d}\n"
    cadena_resultado += f"Coste total: {coste_total:011.2f}\n"

    print(cadena_resultado)


# Descomentar ejecución de función para comprobar el resultado del ejercicio
# ejercicio11()
