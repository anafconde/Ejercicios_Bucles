# Version: 1.0
# Author: Hector Ramirez Pineda
# Ejercicio 6:
# Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

if numero1 > numero2:
    numero1, numero2 = numero2, numero1

for num in range(numero1, numero2 + 1):
    if num % 2 == 0:
        print(num)