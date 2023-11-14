"""
Escribir un programa que cree un diccionario de traducción
español-inglés. El usuario introducirá las palabras en español e inglés
separadas por dos puntos, y cada par <palabra>:<traducción>
separados por comas. El programa debe crear un diccionario con las
palabras y sus traducciones. Después pedirá una frase en español y
utilizará el diccionario para traducirla palabra a palabra. Si una palabra
no está en el diccionario debe dejarla sin traducir.
"""
# Entrada español:ingles. se deberá separar el string por ':'
# Pide frase en español y las que coincidan en el diccionario se traducirán al inglés

diccionario = {}
seguir = True

while seguir:
    entrada = input("Ingresa palabra en formato 'esp:en' : ")
    entrada = entrada.lower()

    # Destructuración
    esp, en = entrada.split(":")

    diccionario[esp] = en

    pregunta = input("Terminar diccionario (Y/N): ")
    if pregunta == "y" or pregunta == "Y":
        seguir = False

# print(diccionario)

fraseESP = input("Ingresa una frase en español: ")
fraseESP = fraseESP.lower()

# Divido la frase por espacios y genero un array para controlar cada palabra por separado
fraseArr = fraseESP.split(" ")

fraseTraducida = []
for palabra in fraseArr:
    if palabra in diccionario:
        fraseTraducida.append(diccionario[palabra])
    else:
        fraseTraducida.append(palabra)

# Imprimir la frase traducida
fraseTraducida = " ".join(fraseTraducida)
print("Frase en inglés: " + fraseTraducida)
