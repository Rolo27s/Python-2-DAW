# Variables: global, nonlocal
# GLOBAL
a = 0


def suma_uno():
    global a
    a = a + 1


suma_uno()
print(a)
# Salida: 1


# NONLOCAL
def funcion_a():
    x = 10

    def funcion_b():
        nonlocal x
        # sustituir nonlocal por global
        x = 20
        print("funcion_b", x)

    funcion_b()
    print("funcion_a", x)


funcion_a()
# Salida:
# funcion_b 20
# funcion_a 20

# --------------------------------------------------

# Módulos: from, import
from collections import namedtuple

# --------------------------------------------------

# Pertenencia e Identidad: in, is

lista = ["a", "b", "c"]
print("a" in lista)

# --------------------------------------------------

del a  # Borro la variable a

# --------------------------------------------------

# Context Managers: with, as
with open("fichero.txt", "r") as file:
    print(file.read())

# --------------------------------------------------

# Concurrencia: async, await
# Creando una función async y usando await, podemos paralelizar la ejecución de los procesos, aprovechando el tiempo “muerto” mientras se retorna al await. En el siguiente ejemplo podemos ver como se tarda unos 10 segundos en ejecutar los 3 procesos.

import asyncio


async def proceso(id_proceso):
    print("Empieza proceso:", id_proceso)
    await asyncio.sleep(10)
    print("Acaba proceso:", id_proceso)


async def main():
    await asyncio.gather(proceso(1), proceso(2), proceso(3))


asyncio.run(main())

# Salida:
# Empieza proceso: 1
# Empieza proceso: 2
# Empieza proceso: 3
# Acaba proceso: 1
# Acaba proceso: 2
# Acaba proceso: 3
