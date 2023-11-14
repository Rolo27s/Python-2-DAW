"""
Desarrolla una función llamada "calcular_salario_promedio" que tome una lista de diccionarios, donde cada diccionario representa la información de un empleado, incluyendo salario, departamento y edad. 

La función debe calcular el salario promedio de los empleados en un departamento específico y devolverlo. Utiliza bucles, condicionales y diccionarios para realizar esta tarea.
"""
# Keys: id, nombre, salario, departamento, edad
lista_empleados = [
    {
        "id": 1,
        "nombre": "Antonio",
        "salario": 1234,
        "departamento": "informática",
        "edad": 34,
    },
    {
        "id": 2,
        "nombre": "María",
        "salario": 2500,
        "departamento": "informática",
        "edad": 28,
    },
    {
        "id": 3,
        "nombre": "Carlos",
        "salario": 1800,
        "departamento": "recursos humanos",
        "edad": 40,
    },
    {
        "id": 4,
        "nombre": "Laura",
        "salario": 3200,
        "departamento": "informática",
        "edad": 32,
    },
    {
        "id": 5,
        "nombre": "Pedro",
        "salario": 1500,
        "departamento": "informática",
        "edad": 45,
    },
    {
        "id": 6,
        "nombre": "Ana",
        "salario": 2800,
        "departamento": "producción",
        "edad": 30,
    },
]


# Función que recibe una lista de diccionarios con información de empleados y devuelve el salario promedio de un departamento específico
def calcular_salario_promedio(lista_empleados):
    departamentos_disponibles = set()  # Usamos un conjunto para evitar duplicados
    total_salario = 0
    cantidad_empleados = 0

    for empleado in lista_empleados:
        departamentos_disponibles.add(
            empleado["departamento"]
        )  # Agregamos el departamento a la lista de disponibles

    print("Departamentos disponibles:")
    for departamento in departamentos_disponibles:
        print(f"- {departamento}")

    departamento_elegido = input(
        "\nIngresa el nombre del departamento para calcular el salario promedio: "
    )

    for empleado in lista_empleados:
        if empleado["departamento"] == departamento_elegido:
            total_salario += empleado["salario"]
            cantidad_empleados += 1

    if cantidad_empleados == 0:
        print(f"No hay empleados en el departamento de {departamento_elegido}.")
        return 0  # Si no hay empleados en el departamento, el salario promedio es 0
    else:
        salario_promedio = total_salario / cantidad_empleados
        print(
            f"Salario promedio en el departamento de {departamento_elegido}: {salario_promedio}"
        )


calcular_salario_promedio(lista_empleados)
