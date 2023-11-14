# Ejercicios de tipos de datos simples
""" Ejercicio 1
Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!. """

print("Ejercicio 1");
print("-----------");
print("Hola Mundo!\n");

""" Ejercicio 2
Escribir un programa que almacene la cadena ¡Hola Mundo! en una
variable y luego muestre por pantalla el contenido de la variable. """

print("Ejercicio 2");
print("-----------");
saludo = "Hola Mundo!\n";
print(saludo);

""" Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola
y después de que el usuario lo introduzca muestre por pantalla la
cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario
haya introducido. """

print("Ejercicio 3");
print("-----------");

nombre = input("Introduce tu nombre: ");

# Pequeño controlador por si el nombre está vacío
if (nombre == ''): nombre = "Sr/a.X";
print("Hola " + nombre + "!\n");

""" Ejercicio 4
Escribir un programa que muestre por pantalla el resultado de la
siguiente operación aritmética (3+2/2*5)^2 """

print("Ejercicio 4");
print("-----------");
print(((3 + 2) / (2 * 5)) ** 2);
print("\n");


""" Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas
trabajadas y el coste por hora. Después debe mostrar por pantalla la
paga que le corresponde. """

print("Ejercicio 5");
print("-----------");

horas = int(input("Introduce el número de horas trabajadas: "));
costo = float(input("Introduce el costo por hora: "));

paga = horas * costo;

# Pequeño controlador
if (paga <= 0):
  print("Error en la entrada de datos. La paga no puede ser menor que 0");
  print("\n");
else:
  print("Tu paga es: " + str(paga) + "€\n");


""" Ejercicio 6
Escribir un programa que lea un entero positivo, n, introducido por el
usuario y después muestre en pantalla la suma de todos los enteros
desde 1 hasta n. La suma de los n primeros enteros positivos puede ser
calculada de la siguiente forma:
𝑠𝑢𝑚𝑎 = 𝑛*(𝑛+1)/2 """

print("Ejercicio 6");
print("-----------");

n = int(input("Introduce un número entero positivo: "));

# Pequeño controlador para saber si el número es negativo
if (n >= 0):
  suma = 0;

  for i in range(1, n + 1):
    suma = suma + i;
  # También es posible usar la formula de Gauss como se propone en el enunciado

  print("La suma total es: " + str(suma));
  print("\n");
else:
  print("Error en la entrada de datos. El número no puede ser menor que 0");
  print("\n");

""" Ejercicio 7
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, 
y muestre por pantalla la frase Tu índice de masa corporal
es <imc> donde <imc> es el índice de masa corporal calculado
redondeado con dos decimales. """

print("Ejercicio 7");
print("-----------");

peso = float(input("Introduce tu peso (Kg): "));
estatura = float(input("Introduce tu estatura (m): "));

if(peso > 0 and estatura > 0):
  imc = peso / (estatura * estatura);

  print("Tu índice de masa corporal es: " + str(round(imc, 2)));
  print("\n");
else:
  print("Error en la entrada de datos. Los datos no pueden ser negativos");
  print("\n");

if(imc < 18.5):
  print("Dado que tu índice de masa corporal es: " + str(round(imc, 2)) + " y tu índice de masa corporal es menor que 18.5, estas en la franja de bajo peso");
  print("\n");

elif(imc >= 18.5 and imc <= 24.9):
  print("Dado que tu índice de masa corporal es: " + str(round(imc, 2)) + " y tu índice de masa corporal es entre 18.5 y 24.9, estas en la franja de peso normal (saludable)");
  print("\n");

elif(imc >= 25 and imc <= 29.9):
  print("Dado que tu índice de masa corporal es: " + str(round(imc, 2)) + " y tu índice de masa corporal es entre 25 y 29.9, estas en la franja de sobrepeso");
  print("\n");

elif(imc >= 30 and imc <= 34.9):
  print("Dado que tu índice de masa corporal es: " + str(round(imc, 2)) + " y tu índice de masa corporal es entre 30 y 34.9, estas en la franja de obesidad clase 1 (ligera)");
  print("\n");

elif(imc >= 35 and imc <= 39.9):
  print("Dado que tu índice de masa corporal es: " + str(round(imc, 2)) + " y tu índice de masa corporal es entre 35 y 39.9, estas en la franja de obesidad clase 2 (moderada)");
  print("\n");

elif(imc >= 40):
  print("Dado que tu índice de masa corporal es: " + str(round(imc, 2)) + " y tu índice de masa corporal es mayor que 40, estas en la franja de obesidad clase 3 (grave)");
  print("\n");

""" Ejercicio 8
Escribir un programa que pida al usuario dos números enteros y
muestre por pantalla la <n> entre <m> da un cociente <c> y un
resto <r> donde <n> y <m> son los números introducidos por el usuario,
y <c> y <r> son el cociente y el resto de la división entera
respectivamente. """

print("Ejercicio 8");
print("-----------");

m = int(input("Introduce el primer número entero (dividendo): "));
n = int(input("Introduce el segundo número entero (divisor): "));

# Pequeño controlador para saber si el número es negativo
if(m > 0 and n > 0):
  c = m / n;
  r = m % n;

  print("El cociente es: " + str(c));
  print("El resto es: " + str(r));
  print("\n");
else:
  print("Error en la entrada de datos. Los datos no pueden ser negativos");
  print("\n");

""" Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a invertir, el
interés anual y el número de años, y muestre por pantalla el capital
obtenido en la inversión. """

print("Ejercicio 9");
print("-----------");

capital = float(input("Introduce el capital a invertir: "));
interes = float(input("Introduce el interés anual (Dato en %): "));
numAnios = int(input("Introduce el número de años: "));

# Paso de porcentaje a decimal para el cálculo
interes = interes / 100;

# Pequeño controlador para saber si el número es negativo
if(capital > 0 and interes > 0 and numAnios > 0):
  capitalFinal = capital * (1 + interes) ** numAnios;

  print("El capital final es: " + str(round(capitalFinal, 2)));
  print("\n");
else:
  print("Error en la entrada de datos. Los datos no pueden ser negativos");
  print("\n");

""" Ejercicio 10
Una juguetería tiene mucho éxito en dos de sus productos: payasos y
muñecas. Suele hacer venta por correo y la empresa de logística les
cobra por peso de cada paquete así que deben calcular el peso de los
payasos y muñecas que saldrán en cada paquete a demanda. Cada
payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el
número de payasos y muñecas vendidos en el último pedido y calcule el
peso total del paquete que será enviado. """

print("Ejercicio 10");
print("-----------");

payasos = int(input("Introduce el número de payasos vendidos: "));
muñecas = int(input("Introduce el número de muñecas vendidas: "));

# Pequeño controlador para saber si el número es negativo

if(payasos > 0 and muñecas > 0):
  peso_payasos = payasos * 112;
  peso_muñecas = muñecas * 75;

  total = payasos + muñecas;
  total_peso = peso_payasos + peso_muñecas;

  print("El total de payasos y muñecas es: " + str(round(total, 2)));
  print("El peso total del paquete es: " + str(round(total_peso, 2)));
  print("\n");
else:
  print("Error en la entrada de datos. Los datos no pueden ser negativos");
  print("\n");

""" Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece
el 4% de interés al año. Estos ahorros debido a intereses, que no se
cobran hasta finales de año, se te añaden al balance final de tu cuenta
de ahorros. Escribir un programa que comience leyendo la cantidad de
dinero depositada en la cuenta de ahorros, introducida por el usuario.
Después el programa debe calcular y mostrar por pantalla la cantidad de
ahorros tras el primer, segundo y tercer años. Redondear cada cantidad
a dos decimales. """

print("Ejercicio 11");
print("-----------");

INTERES = 0.04;
dinero = float(input("Introduce el dinero depositado en la cuenta de ahorros: "));

# Pequeño controlador para saber si el número es negativo
if (dinero > 0):
  for i in range (1, 4):
    capitalFinal = dinero * (1 + INTERES) ** i;

    print("El capital final en el año " + str(i) + " sería de: " + str(round(capitalFinal, 2)) + "€");
  
  print("\n");
else:
  print("Error en la entrada de datos. Los datos no pueden ser negativos");
  print("\n");

""" Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es
el día tiene un descuento del 60%. Escribir un programa que comience
leyendo el número de barras vendidas que no son del día. Después el
programa debe mostrar el precio habitual de una barra de pan, el
descuento que se le hace por no ser fresca y el coste final total. """

print("Ejercicio 12");
print("-----------");

PRECIO_HABITUAL = 3.49;
DESCUENTO = 0.6;

barras_antiguas_vendidas = 14;
barras_nuevas_vendidas = 34;

print("Se han vendido " + str(barras_antiguas_vendidas) + " barras antiguas y " + str(barras_nuevas_vendidas) + " barras nuevas");
print("Las barras antiguas tienen un descuento de 60% y el coste final es de: " + str(round(PRECIO_HABITUAL * barras_antiguas_vendidas * DESCUENTO + PRECIO_HABITUAL * barras_nuevas_vendidas, 2)) + "€");
# Desglose
print("Las barras antiguas sería: " + str(round(PRECIO_HABITUAL * barras_antiguas_vendidas * DESCUENTO, 2)) + "€");
print("Las barras nuevas sería: " + str(round(PRECIO_HABITUAL * barras_nuevas_vendidas, 2)) + "€");