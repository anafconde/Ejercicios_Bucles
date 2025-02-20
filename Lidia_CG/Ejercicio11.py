#Lidia Castro Gutiérrez
#Version 1

#Ejercicio 11. Escribe un programa que diga si un número introducido por teclado es o no primo. Un número primo es aquel que sólo es divisible entre él mismo y la unidad. Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.

import math
nprimo=int(input("Dime un número para saber si es primo o no: "))
es_primo=1 #inicializo a que es primo
for n in range(2,int(math.sqrt(nprimo))+1): 
    #Un numero nunca va a ser divisible por otro numero entero mayor a su raiz cuadrada

    if nprimo % n==0:
        es_primo=0 #no es primo
        break

if es_primo==0:
    print(f"El número {nprimo} no es primo.")
else:
    print(f"El número {nprimo} es primo.")
