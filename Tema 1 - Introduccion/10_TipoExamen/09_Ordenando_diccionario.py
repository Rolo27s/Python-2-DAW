"""
9. Ordenamiento de Listas de Diccionarios: Implementa una función llamada ordenar_por_edad en Python que tome una lista de diccionarios, donde cada diccionario representa a una persona con su 'nombre' y 'edad'. La función debe ordenar la lista de personas por edad de manera ascendente. 
"""

personas = [
    {"nombre": "Juan", "edad": 25},
    {"nombre": "María", "edad": 30},
    {"nombre": "Carlos", "edad": 22},
    {"nombre": "Ana", "edad": 28},
    {"nombre": "Luis", "edad": 35},
    {"nombre": "Laura", "edad": 29},
    {"nombre": "Pedro", "edad": 32},
    {"nombre": "Sofía", "edad": 27},
    {"nombre": "Pablo", "edad": 31},
    {"nombre": "Elena", "edad": 26},
    {"nombre": "Miguel", "edad": 33},
    {"nombre": "Isabel", "edad": 24},
    {"nombre": "Fernando", "edad": 36},
    {"nombre": "Carmen", "edad": 23},
    {"nombre": "Javier", "edad": 34},
    {"nombre": "Rosa", "edad": 28},
    {"nombre": "Diego", "edad": 29},
    {"nombre": "Silvia", "edad": 31},
    {"nombre": "Alejandro", "edad": 27},
    {"nombre": "Beatriz", "edad": 30},
]


def obtener_edad(persona):
    return persona["edad"]


def ordenar_por_edad(lista_personas):
    # Utilizar la función sorted para ordenar la lista de personas por edad
    lista_ordenada = sorted(lista_personas, key=obtener_edad)
    return lista_ordenada


personas_ordenadas = ordenar_por_edad(personas)

print(personas_ordenadas)
