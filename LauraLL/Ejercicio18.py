#-------Autor:LauraLinares-------
#-----------Version:V1.1-----------
#-----Enunciado del ejercicio----
# Hacer un programa que muestre un cronómetro, indicando las horas, minutos y segundos

#----Importador de bibliotecas---
import os
import time

#---Inicializador de variables---

#---Inicializador del programa---
    # Limpio la pantalla antes de entrar al programa
os.system("cls")

for h in range(0,61):
    for min in range(0,61):
        for seg in range(0,61):
            os.system("cls")
            print(f"{h}:{min}:{seg}")
            time.sleep(1)