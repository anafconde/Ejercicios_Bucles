# Version 1.0
# Autor David García Pérez

#Ejercicio 11
#Escribe un programa que diga si un número introducido por teclado es o no primo. Un número primo es aquel que sólo es divisible entre él mismo y la unidad. Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.

import math

numero = int(input("Introduce un número: "))

if numero <= 1:
    print("El número no es primo.")
else:
    es_primo = True
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            es_primo = False
            break

    if es_primo:
        print("El número es primo.")
    else:
        print("El número no es primo.")