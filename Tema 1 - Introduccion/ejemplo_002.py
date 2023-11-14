# Excepciones: assert, try, except, finally, raise
# Probamos el assert
x = 5
y = 10

# Verificar que x sea menor que y usando assert
assert x < y, "x no es menor que y"

# Si la afirmación es falsa, se generará una excepción AssertionError
print("La afirmación es verdadera: x es menor que y")

# ----------------------------------------------------------------

# Ejemplo básico de try (pizarra)
x = "10w"
valor = None
try:
    valor = int(x)
except Exception as e:
    print("Hubo un error: ", e)

print("Valor: ", valor)

# ejemplo de try
try:
    # Código que puede generar una excepción
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    resultado = num1 / num2
    print("El resultado de la división es:", resultado)

except ZeroDivisionError:
    # Manejo de la excepción cuando se intenta dividir por cero
    print("No puedes dividir por cero.")

except ValueError:
    # Manejo de la excepción cuando se ingresa algo que no es un número
    print("Debes ingresar números válidos.")

finally:
    # Código que se ejecuta siempre, independientemente de si se produce una excepción o no.
    print("Este bloque se ejecuta siempre, haya excepción o no.")


# ----------------------------------------------------------------


# Ejemplo con raise
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b


try:
    resultado = dividir(10, 0)
    print("El resultado de la división es:", resultado)
except ZeroDivisionError as e:
    print("Se generó una excepción:", e)

# La declaración raise te permite crear y lanzar tus propias excepciones personalizadas cuando sea necesario en tu código. Esto puede ser útil para manejar situaciones específicas o para proporcionar información detallada sobre errores en tu programa.

# Raise son para condiciones no deseadas. Except maneja excepciones generadas por el código en el bloque try.

