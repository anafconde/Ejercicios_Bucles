#Lidia Castro Gutiérrez
#Version 1

#Ejercicio 13. Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana (seis días) y requiere determinar el total de éstas, así como el sueldo que recibirá por las horas trabajadas.

phora = 15 

total_horas = 0

for dia in range(1, 7):
    horas = float(input(f"Dime las horas trabajadas el día {dia}: "))
    total_horas = total_horas + horas

sueldo_total = total_horas * phora

print(f"Total de horas trabajadas en la semana: {total_horas}")
print(f"Sueldo total por las horas trabajadas: {sueldo_total} euros")