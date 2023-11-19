"""
Escribe una función llamada filtrar_lista que tome una lista de números y devuelva una nueva lista que incluya solo los números impares. Además, debe imprimir la suma de todos los números en la lista original.
"""
lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filtrar_lista (lista):
  lista_filtrada = []
  sumatoria = 0
  for i in range(len(lista)):
    sumatoria += lista[i]

    if lista[i] % 2 != 0:
      lista_filtrada.append(lista[i])

  print (f"Lista original: {lista_original}")
  print (f"Suma de la Lista Original: {sumatoria}")
  print (f"Lista Filtrada: {lista_filtrada}")

  return lista_filtrada

filtrar_lista(lista_original)
