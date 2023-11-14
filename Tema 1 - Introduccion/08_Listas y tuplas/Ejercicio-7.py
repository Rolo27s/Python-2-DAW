""" 
Escribir un programa que almacene el abecedario en una lista, elimine
de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por
pantalla la lista resultante.
"""

abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

newAbc = []

for i in range(len(abecedario)):
    if (i % 3 == 0):
        newAbc.append(abecedario[i])

print ("Lista resultante: ", newAbc)
