"""Crea una función llamada invertir_palabras que tome una cadena de texto y devuelva una nueva cadena donde las palabras estén invertidas, pero el orden de las palabras se mantenga."""

cadena_original = "Python es divertido"

def invertir_palabras(cadena):
  cadenaToArray = cadena.split(' ')
  cadena_resultado_list = []
  for palabra in cadenaToArray:
    palabra = palabra[::-1]
    cadena_resultado_list.append(palabra)

  cadena_resultado = ""
  for palabra in cadena_resultado_list:
    cadena_resultado += (palabra + " ")

  return cadena_resultado


resultado = invertir_palabras(cadena_original)
print(resultado)
