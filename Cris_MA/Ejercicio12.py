#Author: Cris Moreno
#Version: 7.77
## **1️⃣2️⃣ Ejercicio 12**: Ahorro mensual 💰
# Realizar un algoritmo para determinar cuánto **ahorrará** una persona en un año, si al final de cada mes 
# deposita cantidades variables de dinero. Además, se quiere saber cuánto lleva ahorrado cada mes.
mes=1
ahorroTotal=0
while mes<13:
    ahorroMes=int(input(f"Cuanto has ahorrado en el mes {mes}?: "))
    ahorroTotal=ahorroTotal+ahorroMes
    print(f"Tu ahorro hasta el mes {mes} es de {ahorroTotal}€")
    mes +=1
print(f"En un año has ahorrado {ahorroTotal}€ ")




