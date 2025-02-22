#Lidia Castro Gutiérrez
#Version 1

#Ejercicio 17. Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. Para esto, se registran los días que trabajó y las horas de cada día. Realice un algoritmo para determinar el sueldo semanal de N trabajadores y además calcule cuánto pagó la empresa por los N empleados.

E=int(input("Dime el número de trabajadores: "))
phora=15

total=0

for n in range(1,E+1):
    htotales=0
    for d in range(1, 6):
        h=int(input(f"¿cuántas horas ha trabajado el trabajador {n} el dia {d}?"))
        htotales=htotales+h
    print(f"El sueldo semanal del trabajador {n} es {phora*htotales} €")

    total=total + htotales*15

print(f"El sueldo total de los {E} trabajadores es {total} €")

    




