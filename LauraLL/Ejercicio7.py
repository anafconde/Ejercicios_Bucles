#-------Autor:LauraLinares-------
#-----------Version:V1-----------
#-----Enunciado del ejercicio----
# Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado

#----Importador de bibliotecas---
import os

#---Inicializador de variables---


#---Inicializador del programa---
    # Limpio la pantalla antes de entrar al programa
os.system("cls")

print("---TABLA DE MULTIPLICAR POR NÚMEROS---")
n=int(input("Introduzca el número: "))

for i in range(1,11):
    mult=n*i
    print(f"{n} x {i} = {mult}")

