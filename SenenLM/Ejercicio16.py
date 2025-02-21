#version 1.0
#author Senén Lara
#Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. 
# Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, además, 
# calcule cuánto pagó la empresa por los N empleados.

totalpago = 0

Nemp = int(input("Ingrese el número de empleados: "))


for i in range(1, Nemp + 1):
    print("Trabajador numero:",i)
    horas_trabajadas = float(input("Ingrese las horas trabajadas por el empleado: "))
    pago_por_hora = float(input("Ingrese el pago por hora para el empleado: "))
    
    sueldo_semanal = horas_trabajadas * pago_por_hora
    
    
    print("El sueldo semanal del empleado",i, "es:",sueldo_semanal)
    
    
    totalpago = totalpago + sueldo_semanal

print("El total pagado por la empresa para los",Nemp, "empleados es:",totalpago)

    
    