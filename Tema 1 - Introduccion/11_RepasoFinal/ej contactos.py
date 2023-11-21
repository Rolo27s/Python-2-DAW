"""Escribe un programa que gestione una lista de contactos. 
Utiliza un diccionario donde las claves son los nombres de las personas y los valores son números de teléfono. 
Permite a los usuarios agregar nuevos contactos, eliminar contactos existentes y buscar números de teléfono 
utilizando condicionales y bucles para controlar el flujo del programa."""


import re  # Importa el módulo de expresiones regulares para validar el número de teléfono.

def mostrar_menu():
    # Imprime las opciones del menú.
    print("\nGestor de Contactos")
    print("1. Agregar Contacto")
    print("2. Eliminar Contacto")
    print("3. Buscar Contacto")
    print("4. Mostrar Todos los Contactos")
    print("5. Salir")

def validar_nombre(nombre):
    # Comprueba que el nombre del contacto no esté vacío.
    return nombre.strip() != ""

def validar_numero(numero):
    # Valida que el número de teléfono solo contenga dígitos y caracteres permitidos.
    patron = re.compile(r'^[\d\s\-()+]+$')
    return patron.match(numero) is not None

def agregar_contacto(contactos):
    # Solicita al usuario que introduzca el nombre y el número del nuevo contacto.
    nombre = input("Ingrese el nombre del contacto: ")
    # Verifica si el nombre es válido.
    if not validar_nombre(nombre):
        print("Nombre inválido. Intente de nuevo.")
        return

    numero = input("Ingrese el número de teléfono: ")
    # Verifica si el número es válido.
    if not validar_numero(numero):
        print("Número inválido. Intente de nuevo.")
        return

    # Agrega el nuevo contacto al diccionario.
    contactos[nombre] = numero
    print(f"Contacto {nombre} agregado.")

def eliminar_contacto(contactos):
    # Solicita el nombre del contacto a eliminar.
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    # Elimina el contacto si se encuentra en el diccionario.
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        print("Contacto no encontrado.")

def buscar_contacto(contactos):
    # Solicita el nombre del contacto a buscar.
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    # Busca el contacto y muestra su número si existe.
    numero = contactos.get(nombre)
    if numero:
        print(f"El número de {nombre} es {numero}.")
    else:
        print("Contacto no encontrado.")

def mostrar_contactos(contactos):
    # Muestra todos los contactos almacenados.
    if contactos:
        print("\nLista de Contactos:")
        for nombre, numero in contactos.items():
            print(f"{nombre}: {numero}")
    else:
        print("No hay contactos guardados.")

def gestor_contactos():
    # Inicializa el diccionario de contactos.
    contactos = {}
    # Ciclo infinito para ejecutar el menú de opciones.
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        # Ejecuta la opción seleccionada.
        if opcion == "1":
            agregar_contacto(contactos)
        elif opcion == "2":
            eliminar_contacto(contactos)
        elif opcion == "3":
            buscar_contacto(contactos)
        elif opcion == "4":
            mostrar_contactos(contactos)
        elif opcion == "5":
            print("Saliendo del gestor de contactos.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Ejecutar el programa.
gestor_contactos()
