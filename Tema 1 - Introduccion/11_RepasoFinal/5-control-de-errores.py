"""Modifica la función calcular_area_rectangulo del ejercicio 3 para manejar posibles errores de entrada. Si se proporciona un valor no numérico, imprime un mensaje de error y devuelve -1."""


def calcular_area_rectangulo(longitud=5, ancho=3):
    if longitud.isdigit() and ancho.isdigit():
        return longitud * ancho
    else:
        print("Error: Los valores de longitud y ancho deben ser numéricos.")
        return -1


area_invalida = calcular_area_rectangulo("abc", 6)
print("Área con valor no numérico:", area_invalida)
