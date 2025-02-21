#autor -------------Richard Bustamante Carreño
#version --------------version:1
#Escribe un programa que diga si un número introducido por teclado es o no primo. Un número primo es aquel que sólo es divisible entre él mismo y la unidad. Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.
import math

numero = int(input("Introduce un número: "))
contador = 2
while contador <= math.isqrt(numero):
    if numero % contador == 0:
        print(f"{numero} no es un número primo.")
        break
    contador += 1
else:
    print(f"{numero} es un número primo.")