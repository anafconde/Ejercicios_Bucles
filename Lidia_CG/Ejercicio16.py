#Lidia Castro Gutiérrez
#Version 1

#Ejercicio 16. Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, además, calcule cuánto pagó la empresa por los N empleados.

phora=15
total=0

N=int(input("Cuantos trabajadores hay?: "))

   
for n in range(1,N+1):
    h=int(input(f"Cuántas horas a la semana ha trabajado el trabajador {n}?: "))
    salario=n*phora
    print(f"El sueldo semanal del trabajador {n} es {salario} €")
    total=total+salario
print(f"La empresa ha pagado {total} € por los {N} empleados.")


