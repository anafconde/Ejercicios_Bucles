#autor -------------Richard Bustamante Carreño
#version --------------version:1
#Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. Para esto, se registran los días que trabajó y las horas de cada día. Realice un algoritmo para determinar el sueldo semanal de N trabajadores y además calcule cuánto pagó la empresa por los N empleados.

num_empleados = int(input("Ingrese la cantidad de empleados: "))
pago_por_hora = int(input("Ingrese el pago por hora: "))
total_pago_empresa = 0

for empleado in range(1, num_empleados + 1):
    total_horas = 0
    dias_trabajados = int(input(f"Ingrese los días trabajados por el empleado {empleado}: "))
    
    for dia in range(1, dias_trabajados + 1):
        horas = float(input(f"Ingrese las horas trabajadas en el día {dia} para el empleado {empleado}: "))
        total_horas += horas
    
    sueldo = total_horas * pago_por_hora
    total_pago_empresa += sueldo
    print(f"Sueldo semanal del empleado {empleado}: {sueldo}€")

print(f"Total pagado por la empresa: {total_pago_empresa}€")