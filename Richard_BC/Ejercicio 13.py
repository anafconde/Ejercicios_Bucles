#autor -------------Richard Bustamante Carreño
#version --------------version:1
#Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana (seis días) y requiere determinar el total de éstas, así como el sueldo que recibirá por las horas trabajadas.
total_horas = 0
pago_por_hora = float(input("Ingrese el pago por hora: "))

total_horas = 0
for dia in range(1, 7):
    horas = float(input(f"Ingrese las horas trabajadas en el día {dia}: "))
    total_horas += horas

sueldo = total_horas * pago_por_hora
print(f"Total de horas trabajadas: {total_horas}, y el sueldo total: {sueldo}")