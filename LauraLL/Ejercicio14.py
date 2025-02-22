#-------Autor:LauraLinares-------
#-----------Version:V1-----------
#-----Enunciado del ejercicio----
# Una persona se encuentra en el kilómetro 70 de una carretera, otra se encuentra en el km 150, los coches tienen sentido opuesto y tienen la misma velocidad.
# Realizar un programa para determinar en qué kilómetro de esa carretera se encontrarán

#----Importador de bibliotecas---
import os

#---Inicializador de variables---
coche1=70
coche2=150

#---Inicializador del programa---
    # Limpio la pantalla antes de entrar al programa
os.system("cls")

while coche1 != coche2: # Es decir, mientras no estén en el mismo punto (el mismo kilómetro)
    coche1=coche1+1 # El primer coche (o persona) avanza un kilómetro
    coche2=coche2-1 # El segundo coche (o persona) retrocede un kilónetro (o avanza uno hacia el coche 1)

print(f"El coche 1 ha se ha encontrado con el coche 2 en el kilómetro {coche1}")  
print(f"y el coche 2 ha se ha encontrado con el coche 1 en el kilómetro {coche2}")
print(f"¡Están en el mismo kilómetro!")  