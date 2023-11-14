"""
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos
listas y muestre por pantalla su producto escalar.
"""
vector_1 = list((1,2,3))
vector_2 = list((-1,0,-2))
multi = []
result = 0

for i in range(3):
    multi.append( vector_1[i] * vector_2[i])
    result += multi[i]

print(result)