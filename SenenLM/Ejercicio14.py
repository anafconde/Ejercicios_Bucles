#version 1.0
#author Senén Lara
#Una persona se encuentra en el kilómetro 70 de una carretera, otra se encuentra en el km 150, 
# los coches tienen sentido opuesto y tienen la misma velocidad. 
# Realizar un programa para determinar en qué kilómetro de esa carretera se encontrarán.

# Inicializa las posiciones de los dos coches
posicion_a = 70
posicion_b = 150

velocidad = int(input("Dime a que velocidad van los dos coches: "))

while posicion_a < posicion_b:
    posicion_a = posicion_a + velocidad
    posicion_b = posicion_b - velocidad

print("Los coches se encontrarán en el kilómetro",posicion_a)
