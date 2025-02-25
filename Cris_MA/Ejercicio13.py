#Author: Cris Moreno
#Version: 7.77

## **1️⃣3️⃣ Ejercicio 13**: Sueldo por horas trabajadas 💼
#Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana (seis días) 
# y requiere determinar el total de éstas, así como el sueldo que recibirá por las horas trabajadas.

semana=1
totalHoras=0
sueldoHora=13
while semana<7:
    horas=int(input(f"Cuantas horas trabajaste el dia {semana}  "))
    totalHoras= totalHoras+horas
    semana += 1
sueldo=totalHoras*sueldoHora
print(f"El trabajador ha realizado un total de {totalHoras} horas en la semana y se le deberá pagar por ello {sueldo}€")

