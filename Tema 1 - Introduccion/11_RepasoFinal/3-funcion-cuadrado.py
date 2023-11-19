"""
Escribe una función llamada calcular_area_rectangulo que tome dos parámetros (longitud y ancho) y devuelva el área del rectángulo. Si no se proporciona alguno de los parámetros, la función debe usar valores predeterminados de 5 para longitud y 3 para ancho."""


def calcular_area_rectangulo(longitud=5, ancho=3):
    return longitud * ancho


area_default = calcular_area_rectangulo()
area_personalizada = calcular_area_rectangulo(8, 6)

print("Área con valores predeterminados:", area_default)
print("Área con valores personalizados:", area_personalizada)
