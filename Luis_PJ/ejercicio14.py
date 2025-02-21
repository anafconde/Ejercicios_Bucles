# Author: Luis Palacios
# Version: 1.0

# 1️⃣4️⃣ Ejercicio 14: Encuentro de dos coches 🚗
# Una persona se encuentra en el kilómetro 70 de una carretera, 
# otra se encuentra en el km 150, los coches tienen sentido opuesto y tienen la misma velocidad.
# Realizar un programa para determinar en qué kilómetro de esa carretera se encontrarán.

# CON EL PUNTO MEDIO

coche1=70
coche2=150

while coche1 != coche2:
    coche1=coche1+1
    coche2=coche2-1
print("Los dos coches se encuentras en el km",coche1)

