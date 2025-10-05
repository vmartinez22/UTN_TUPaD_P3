#TRABAJO PRÁCTICO N3 - CONDICIONALES

#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# #deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "));

if edad >= 18:
    print("Es mayor de edad");
else:
    print("No es mayor de edad");

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar 
# #por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = float(input("Ingrese su nota: "));

if nota >= 6:
    print("Aprobado");
else:
    print("Desaprobado"); 

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, 
# #imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por 
# #pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en 
# Python para evaluar si un número es par o impar.

num = int(input("Ingrese un numero entero: "));

if num % 2 == 0:
    print("Ha ingresado un numero par.");
else:
    print("Por favor, ingrese un número par.")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes 
# categorías pertenece: ● Niño/a: menor de 12 años. ● Adolescente: mayor o igual que 12 años y 
# menor que 18 años. ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "));

if edad < 12:
    print("Categoría: Niño.");
elif edad >= 12 and edad < 18:
    print("Categoría: Adolescente.");
elif edad >= 18 and edad < 30:
    print("Categoría: Adulto.");
else:
    print("Categoría: Adulto mayor.");


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14).
#  Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje 
# "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese
# una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para 
# evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

contraseña = str(input("Ingrese la contraseña: "));

longitud = len(contraseña);

if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña correcta.");
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.");



#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular 
#la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente:
#La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se pueden utilizar 
# para predecir la forma de una distribución normal a partir del siguiente criterio: ● Sesgo positivo o 
# a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda. 
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es 
# menor que la moda. ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, 
# calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o
# no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mode, median, mean
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios);
mediana = median(numeros_aleatorios);
moda = mode(numeros_aleatorios);

print("Media: ", media);
print("Mediana: ", mediana);
print("Moda: ", moda);

if media > mediana > moda:
    print("Sesgo positivo o a la derecha.");
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda.");
else:
    print("Sin sesgo.")


#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con 
# vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso 
# contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase = str(input("Ingrese una frase o palabra: "));

if frase.lower().endswith(("a", "e", "i", "o", "u")):
    frase = frase+"!"

print("Resultado: ", frase);

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e 
#imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre =str(input("Ingrese el nombre: "));

print("Deberá elegir una opción: ");
print("1. Si quiere su nombre en mayúsculas.");
print("2. Si quiere su nombre en minúsculas.");
print("3. Si quiere su nombre con la primera letra mayúscula.");

opcion = int(input("Cuál opción eliges? "));

if opcion == 1:
    nom = nombre.upper()
elif opcion == 2:
    nom = nombre.lower()
else:
    nom = nombre.title()

print("Resultado: ", nom);

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = int(input("Ingrese la magnitud del terremoto: "));

if magnitud < 3:
    print("Muy leve (Imperceptible).");
elif magnitud >= 3 and magnitud < 4:
    print("Leve (Ligeramente perceptible).");
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)");
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)");
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños)");
else:
    print("Extremo (puede causar graves daños a gran escala)");

#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = str(input("¿En cuál hermisferio te encuentras? (N/S) ")).upper();
mes = int(input("¿Mes del año es? "));
dia = int(input("¿Qué día es? "));

if hemisferio == "N":
      if (mes == 12 and dia >= 21) or (mes <= 3 and (mes != 3 or dia <= 20)) or (mes < 3):
        estacion = "Invierno"
      if (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20) or (mes > 3 and mes < 6):
        estacion = "Primavera"
      if (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20) or (mes > 6 and mes < 9):
        estacion = "Verano"
      if (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20) or (mes > 9 and mes < 12):
        estacion = "Otoño"
elif hemisferio == "S":
      if (mes == 12 and dia >= 21) or (mes <= 3 and (mes != 3 or dia <= 20)) or (mes < 3):
        estacion = "Verano"
      if (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20) or (mes > 3 and mes < 6):
        estacion = "Otoño"
      if (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20) or (mes > 6 and mes < 9):
        estacion = "Invierno"
      if (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20) or (mes > 9 and mes < 12):
        estacion = "Primavera"
else:
    estacion = "Hemisferio inválido"


print(f"En el hemisferio {hemisferio} es {estacion}.")

