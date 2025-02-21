# Author: Luis Palacios
# Version: 1.0

# 1️⃣8️⃣ Ejercicio 18: Cronómetro ⏱️
# Hacer un programa que muestre un cronómetro, indicando las horas, minutos y segundos.

minutos=0
horas=0

while horas != 10:
    horas=horas+1
    while minutos != 59:
        minutos=minutos+1
        for s in range(0,60):
            print(horas,":",minutos,":",s)
        


        