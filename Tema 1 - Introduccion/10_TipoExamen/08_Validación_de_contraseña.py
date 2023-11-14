"""
8. Validación de Contraseña: Crea una función llamada validar_contraseña en Python que tome una cadena como argumento y verifique si cumple con los siguientes criterios: • Tiene al menos 8 caracteres de longitud. • Contiene al menos una letra mayúscula y una letra minúscula. • Contiene al menos un carácter especial (por ejemplo, !, @, #). La función debe devolver True si la contraseña es válida y False en caso contrario.
"""

import re


def validar_contraseña(contraseña):
    # Verificar la longitud mínima
    if len(contraseña) < 8:
        print(f"{contraseña} - Error en longitud mínima")
        return False

    # Verificar al menos una letra mayúscula
    if not any(c.isupper() for c in contraseña):
        print(f"{contraseña} - Error. Debe contener un carácter en mayúsculas")
        return False

    # Verificar al menos una letra minúscula
    if not any(c.islower() for c in contraseña):
        print(f"{contraseña} - Error. Debe contener un carácter en minúsculas")
        return False

    # Verificar al menos un carácter especial
    if not re.search(r"[!@#?*]", contraseña):
        print(f"{contraseña} - Error. Debe contener un carácter especial")
        return False

    # La contraseña cumple con todos los criterios
    print(f"{contraseña} es una contraseña segura")
    return True


# Ejemplo:
contraseña1 = "Yamakasi123!"
contraseña2 = "1234"

validar_contraseña(contraseña1)
validar_contraseña(contraseña2)
