#-------Autor:LauraLinares-------
#-----------Version:V1-----------
#-----Enunciado del ejercicio----
# Escribe un programa que diga si un número introducido por teclado es o no primo.
# Un número primo es aquel que sólo es divisible entre él mismo y la unidad.
# Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número

#----Importador de bibliotecas---
import math
import os

#---Inicializador de variables---
primo=1

#---Inicializador del programa---
    # Limpio la pantalla antes de entrar al programa
os.system("cls")

print("----PROGRAMA COMPROBADOR DE NÚMEROS PRIMOS----")
n=int(input("Introduzca el número a comprobar: "))

raiz=int(math.sqrt(n))

# El 1 no es un número primo, así que lo descarto primero
if n < 2:
    print(f"El número {n} NO es primo")
    exit ()
# Compruebo que desde 2 hasta la raiz del numero (+1), si hay algún otro número capaz de dividir el número, significa que no es primo
else:
    for i in range(2,raiz+1):
        if n%i == 0:
            primo=0
            break

# Si no ha cambiado el contador es porque el for no ha dado resultados, ergo es primo
if primo == 1:
    print(f"El número {n} es primo")
# Si el for encuentra resultados (otros números que pueden dividir el número), no es primo
else:
    print(f"El número {n} NO es primo")
