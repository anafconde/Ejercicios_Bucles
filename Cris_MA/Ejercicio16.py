#Author: Cris Moreno
#Version: 7.77
## **1️⃣6️⃣ Ejercicio 16**: Sueldo semanal de empleados 💵
# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana.
# Realice un algoritmo para determinar el **sueldo semanal** de **N** trabajadores y, 
# además, calcule cuánto pagó la empresa por los **N** empleados.

precioHora=13
pagoEmpresa=0
confirmacion="si"
salario=0
while confirmacion=="si":
    confirmacion=input("Quieres calcular el salario de un nuevo empleado para esta semana?: ")
    if confirmacion!="si":
        break
    horas=int(input("Cuantas horas trabajó el empleado esa semana?: "))
    salario=horas*precioHora
    pagoEmpresa=pagoEmpresa+salario
    print(f"El salario a pagar al trabajador es de {salario} € ")
print(f"La empresa debera pagar en concepto de salarios {pagoEmpresa}€")




