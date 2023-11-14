"""
Escribir un programa que almacene las matrices A y B dadas
en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas,
representando cada vector fila en una lista.
"""

Matrix_A = [[1, 2, 3], [4, 5, 6]]
Matrix_B = [[-1, 0], [0, 1], [1, 1]]
print(str(Matrix_A[0]) + "\n" + str(Matrix_A[1]))
print("multiplicado por")
print(str(Matrix_B[0]) + "\n" + str(Matrix_B[1]) + "\n" + str(Matrix_B[2]))
print("Es igual a")

# Matriz resultado de multiplicación
# A B
# C D

A = 0
B = 0
C = 0
D = 0

# Tendré 4 incógnitas a calcular: A, B, C, D
for i in range(4):
    for j in range(3):
        if i == 0:
            A += Matrix_A[i][j] * Matrix_B[j][i]
        if i == 1:
            B += Matrix_A[i - 1][j] * Matrix_B[j][i]
        if i == 2:
            C += Matrix_A[1][j] * Matrix_B[j][0]
        if i == 3:
            D += Matrix_A[1][j] * Matrix_B[j][1]

Matrix_C = [[A, B], [C, D]]

print(f"{Matrix_C[0]}\n{Matrix_C[1]}")
