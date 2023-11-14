""" 
Escribir un programa que almacene las asignaturas de un curso (por
ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
pregunte al usuario la nota que ha sacado en cada asignatura y elimine
de la lista las asignaturas aprobadas. Al final el programa debe mostrar
por pantalla las asignaturas que el usuario tiene que repetir.
"""

asignaturas = ["Matemáticas", "Química", "Historia", "Lengua"]
notas = []

for asignatura in asignaturas:
    nota = input(f"Que nota has sacado en {asignatura}?: ")
    nota = float(nota)
    while nota < 0 or nota > 10:
        print ("La nota debe estar entre 0 y 10")
        nota = input(f"Que nota has sacado en {asignatura}?: ")
        nota = float(nota)
    notas.append(nota)

asignaturas_a_repetir = asignaturas.copy()

for i in range(len(asignaturas)):
    if notas[i] >= 5:
        asignaturas_a_repetir.remove(asignaturas[i])

if asignaturas_a_repetir:
    print("Debes repetir las siguientes asignaturas:")
    for asignatura in asignaturas_a_repetir:
        print(asignatura)
else:
    print("¡Has aprobado todas las asignaturas!")
    
