#Author: Cris Moreno
#Version: 7.77
## **1️⃣1️⃣ Ejercicio 11**: Número primo 🔍
#Escribe un programa que diga si un número introducido por teclado es o no **primo**.
#Un número primo es aquel que sólo es divisible entre él mismo y la unidad.
#**Nota**: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro 
#número.

import math
num=int(input("Dime un numero, te dire si es primo o no: "))

raiz=int(math.sqrt(num))
primo=True
for i in range(2,raiz+1):
    if num%i == 0:
        primo=False
if primo==True and num>1:
    print(f"El numero {num} es primo")
else:
    print(f"El numero {num} NO es primo")

    

