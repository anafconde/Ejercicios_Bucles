# Author: Luis Palacios
# Version: 1.0

# 6️⃣ Ejercicio 6: Números pares entre dos valores 🔢
# Escribir un programa que imprima todos los números 
# pares entre dos números que se le pidan al usuario.

num1=int(input("Introduce un número: "))
num2=int(input("Introduce un segundo número: "))

if num1 > num2:
    for recorrer in range(num2,num1):
        if recorrer % 2 == 0:
            print(recorrer," ",end="")
        elif recorrer % 2 != 0:
            continue
elif num1 < num2:
    for recorrer in range(num1,num2):
        if recorrer % 2 == 0:
            print(recorrer," ",end="")
        elif recorrer % 2 != 0:
            continue
else:
    if num1 %2 == 0:
        print(num1,"es par")
