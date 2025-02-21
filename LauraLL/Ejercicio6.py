#-------Autor:LauraLinares-------
#-----------Version:V1-----------
#-----Enunciado del ejercicio----
# Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario

#----Importador de bibliotecas---
import os

#---Inicializador de variables---


#---Inicializador del programa---
    # Limpio la pantalla antes de entrar al programa
os.system("cls")

n1=int(input("Introduzca el primer número: "))
n2=int(input("Introduzca el segundo número: "))

# Compruebo que el número 1 sea mayor que el 2, si no lo es, los intercambiamos
if n1>n2:
    aux=n1 # Uso una variable auxiliar para almacenar el valor de n1
    n1=n2 # Paso el valor de n2 para que ahora sea el de n1
    n2=aux # La variable n2 coge el valor de la variable auxiliar (que tenía el valor de n1)
elif n1 == n2:
    if n1%2 == 0:
        print(f"Los números {n1} y {n2} son iguales y, además, es un número par")
    else:
        print(f"Los números {n1} y {n2} son iguales y NO un número par")

for num in range(n1,n2+1):
    if num % 2 == 0:
        print(num," ",end="")
    else:
        continue