#Autor: Israel
#Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

n1 = int(input("Dime el primer numero: "))
n2 = int(input("Dime el segundo numero: "))

for var in range(n1, n2, 2):
    print(var," ", end=" ")