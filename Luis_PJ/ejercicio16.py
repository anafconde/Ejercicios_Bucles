# Author: Luis Palacios
# Version: 1.0

# 1️⃣6️⃣ Ejercicio 16: Sueldo semanal de empleados 💵
# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana.
# Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, 
# además, calcule cuánto pagó la empresa por los N empleados.

emple=int(input("Cuantos trabajadores hay en la empresa: "))
salhora=float(input("Cuanto se paga a la hora: "))
total=0

for n in range(1,emple+1):
    horas=float(input("Cuantas horas ha trabajado el empleado nº%d: " % n))
    salario=salhora*horas
    total=total+salario
    print("El empleado",n,"ha trabajado",horas,"horas y ha cobrado esta semana",salario,"€")
print("La empresa se ha gastado esta semana en sueldos de empleados",total,"€")




