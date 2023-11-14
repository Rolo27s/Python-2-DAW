"""
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y
muestre por pantalla la misma fecha en formato dd de <mes> de aaaa
donde <mes> es el nombre del mes.
"""

fecha = input("Dame una fecha en formato 'dd/mm/aaaa' :")

Meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre",
}

# Como tengo el formato 'dd/mm/yyyy' claramente definido uso esta propiedad de string. También se puede usar el método de split de array por '/'
dia = fecha[0:2]
mes = fecha[3:5]
mes = int(mes)
anio = fecha[6:10]
print(dia, mes, anio)

if mes in Meses:
    print(f"Fecha formateada: {dia} de {Meses[mes]} de {anio}")
else:
    print("Mes no válido en la fecha proporcionada.")
