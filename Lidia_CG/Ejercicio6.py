#Lidia Castro Gutiérrez
#Version 1

#Ejercicio 6. Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

n=int(input("Dime un número: "))
m=int(input("Dime otro número: "))

if n > m:
    n,m=m,n

for i in range(n,m):
    if i % 2 == 0:
        print(f"{i} es par")


