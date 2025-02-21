# Author: Luis Palacios
# Version: 1.0

# 1️⃣2️⃣ Ejercicio 12: Ahorro mensual 💰
# Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, 
# si al final de cada mes deposita cantidades variables de dinero. 
# Además, se quiere saber cuánto lleva ahorrado cada mes.

total=0

for n in range(1,13):
    ahorro=float(input("Cuanto has ahorrado: "))
    total=total+ahorro
    print("En el mes",n,"º, lleva ahorrado un total de",total,"€")

