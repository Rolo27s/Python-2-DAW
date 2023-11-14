"""
Diseña una función llamada "agregar_a_lista" que tome una lista y una tupla como argumentos. 
La función debe agregar todos los elementos de la tupla a la lista, asegurándose de que no haya duplicados.
Utiliza bucles y condicionales para lograrlo.
"""


def agregar_a_lista(lista, tupla):
    # Itera a través de los elementos de la tupla
    for elemento in tupla:
        # Comprueba si el elemento no está en la lista
        if elemento not in lista:
            # Agrega el elemento a la lista si no existe en ella
            lista.append(elemento)

    # Opción muy simple que hace lo mismo
    # lista.extend(set(tupla) - set(lista))


# Ejemplo de uso
mi_lista = [1, 2, 3, 4]
mi_tupla = (3, 4, 5, 6)

agregar_a_lista(mi_lista, mi_tupla)
print("Lista después de agregar elementos de la tupla:", mi_lista)
