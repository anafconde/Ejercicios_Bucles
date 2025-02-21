#-------Autor:LauraLinares-------
#-----------Version:V1-----------
#-----Enunciado del ejercicio----
# Algoritmo que muestre la tabla de multiplicar de los números 1, 2, 3, 4 y 5

#----Importador de bibliotecas---
import os

#---Inicializador de variables---

#---Inicializador del programa---
    # Limpio la pantalla antes de entrar al programa
os.system("cls")

for num in range(1,6):
    print(f"---TABLA DE MULTIPLICAR DEL NÚMERO {num}---")
    for num2 in range(1,11):
        mult=num*num2
        print(f"{num} x {num2} = {mult}")
