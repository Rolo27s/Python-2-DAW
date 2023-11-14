"""
10. Calculadora de Calificaciones: Diseña un programa en Python que permita a un usuario ingresar las calificaciones de los estudiantes en un curso. Calcula y muestra el promedio de calificaciones, la calificación más alta y la más baja. Además, presenta a cada estudiante como "Aprobado" o "Suspenso"
"""
list = []


def newStudent():
    newStudentName = input("Add a student's name:")
    while len(newStudentName) < 3:
        print("Error in name. The name must be at least 3 characters long")
        newStudentName = input("Add a student's name:")

    newStudentMark = float(input("Add the score:"))
    while newStudentMark < 0 or newStudentMark > 10:
        print("The mark is not correct. It should be between 0 and 10")
        newStudentMark = float(input("Add the score:"))

    print(f"The new student is {newStudentName} and his mark is {newStudentMark:.2f}")
    return newStudentName, newStudentMark


def addStudentIntoDicc(list):
    newStudentName, newStudentScore = newStudent()
    list.append([newStudentName, newStudentScore])


# Main
while True:
    print("Introduce a new student")
    addStudentIntoDicc(list)

    print(list)

    next = input("Do you want to introduce a new student? (Y/N): ")
    while next != "Y" and next != "N":
        next = input(
            "ANSWER 'Y' OR 'N'. Do you want to introduce a new student? (Y/N): "
        )

    if next == "N":
        break


minNote = 10
for student in list:
    name = student[0]
    note = student[1]
    if note < minNote:
        nameMinNote = name
        minNote = note

maxNote = 0
for student in list:
    name = student[0]
    note = student[1]
    if note > maxNote:
        nameMaxNote = name
        maxNote = note

totalNotes = 0
count = 0
for student in list:
    count = int(count + 1)
    totalNotes += float(student[1])

for student in list:
    if student[1] >= 5:
        print(f"Student {student[0]} passed")
    else:
        print(f"Student {student[0]} failed")

print(
    f"\n{nameMaxNote} got the highest mark, a {maxNote}, and {nameMinNote} got the lowest, a {minNote}"
)

print(f"The average mark is {(totalNotes / count):.2f}")
