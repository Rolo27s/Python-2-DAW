"""
Escribe un programa que gestione una lista de tareas pendientes. 
Utiliza un diccionario donde las claves son las categorías de las tareas y los valores son listas de tareas pendientes. 
Permite a los usuarios agregar, eliminar y marcar tareas como completadas utilizando condicionales y bucles para controlar el flujo del programa.
"""

# Inicializar el diccionario de tareas pendientes
tareas_pendientes = {
    "Trabajo": ["Preparar presentación", "Enviar informe", "Reunión con el equipo"],
    "Casa": ["Comprar víveres", "Lavar la ropa", "Pintar la habitación"],
    "Estudio": [
        "Hacer tarea de matemáticas",
        "Leer capítulo 5",
        "Preparar para el examen de historia",
    ],
    "Personal": ["Hacer ejercicio", "Llamar a mamá", "Planificar las vacaciones"],
}


# Función para mostrar las tareas pendientes por categoría
def mostrar_tareas():
    print("Tareas pendientes:")
    for categoria, tareas in tareas_pendientes.items():
        print(f"{categoria}:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
        print()


# Función para agregar una tarea
def agregar_tarea():
    categoria = input("Ingresa la categoría de la tarea: ")
    tarea = input("Ingresa la nueva tarea: ")
    if categoria in tareas_pendientes:
        tareas_pendientes[categoria].append(tarea)
    else:
        tareas_pendientes[categoria] = [tarea]
    print(f"Tarea '{tarea}' agregada a la categoría '{categoria}'.")


# Función para eliminar una tarea
def eliminar_tarea():
    mostrar_tareas()
    categoria = input("Ingresa la categoría de la tarea que deseas eliminar: ")
    if categoria in tareas_pendientes:
        tarea_numero = (
            int(input("Ingresa el número de tarea que deseas eliminar: ")) - 1
        )
        if 0 <= tarea_numero < len(tareas_pendientes[categoria]):
            tarea_eliminada = tareas_pendientes[categoria].pop(tarea_numero)
            print(f"Tarea '{tarea_eliminada}' eliminada.")
        else:
            print("Número de tarea inválido.")
    else:
        print("Categoría no encontrada.")


# Menú principal del programa
while True:
    print("\nGestor de Tareas Pendientes")
    print("1. Mostrar tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea (completada)")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        mostrar_tareas()
        input("Presione una tecla para continuar...")
    elif opcion == "2":
        agregar_tarea()
        input("Presione una tecla para continuar...")
    elif opcion == "3":
        eliminar_tarea()
        input("Presione una tecla para continuar...")
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
        input("Presione una tecla para continuar...")
