"""
Crea una función llamada "encontrar_diferencia_set" que tome dos conjuntos como argumentos y devuelva un conjunto que contenga elementos que estén presentes en el primer conjunto pero no en el segundo. 
Asegúrate de manejar adecuadamente situaciones en las que los conjuntos sean vacíos o no tengan elementos en común.
"""


def encontrar_diferencia_set(conjunto1, conjunto2):
    # Comprueba si el primer conjunto está vacío
    if not conjunto1:
        # Si el primer conjunto está vacío, no hay elementos para comparar, entonces devolvemos un conjunto vacío.
        return set()
    # Comprueba si el segundo conjunto está vacío
    if not conjunto2:
        # Si el segundo conjunto está vacío, la diferencia es el primer conjunto.
        return conjunto1

    # Inicializamos un conjunto vacío para almacenar la diferencia entre los conjuntos.
    diferencia = set()

    # Iteramos a través de los elementos en el primer conjunto.
    for elemento in conjunto1:
        # Si el elemento no está en el segundo conjunto, lo agregamos a la diferencia.
        if elemento not in conjunto2:
            diferencia.add(elemento)

    # Devolvemos el conjunto que contiene la diferencia.
    return diferencia


# Ejemplo
conjunto1 = {1, 8, 9, 10, 12}
conjunto2 = {7, 8, 9, 15, 16}

resultado = encontrar_diferencia_set(conjunto1, conjunto2)
print(f"Diferencia entre conjunto1 y conjunto2: {resultado}")
