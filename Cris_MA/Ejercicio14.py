#Author: Cris Moreno
#Version: 7.77
## **1️⃣4️⃣ Ejercicio 14**: Encuentro de dos coches 🚗
# Una persona se encuentra en el **kilómetro 70** de una carretera, otra se encuentra en 
# el **km 150**, los coches tienen **sentido opuesto** y tienen la misma velocidad.
# Realizar un programa para determinar en qué kilómetro de esa carretera se encontrarán.

cocheA=70
cocheB=150

while cocheA != cocheB:
    cocheA+=1
    cocheB-=1
print (f"Los coches se encontraran en el km {cocheA} ")

