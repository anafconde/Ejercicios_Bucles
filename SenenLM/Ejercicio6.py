#version 1.0
#author Senén Lara

#Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.


n1 = int(input("Introduce el primer numero: "))
n2 = int(input("Introduce el segundo numero: "))
if n1%2 == 0:    
    for var in range(n1,n2,2):
        print(var," ",end="")
elif n1%2 != 0:
    n1 = n1 + 1
    for var in range(n1,n2,2):
        print(var," ",end="")