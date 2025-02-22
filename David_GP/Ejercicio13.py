# Version 1.0
# Autor David García Pérez

#Ejercicio 13
#Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana (seis días) y requiere determinar el total de éstas, así como el sueldo que recibirá por las horas trabajadas.

# Constantes
HORAS_DIARIAS = 8  # Horas diarias de trabajo
TARIFA_HORA = 10  # Tarifa por hora trabajada

# Obtener las horas trabajadas por día
horas_trabajadas = []
for dia in range(1, 7):
    horas = float(input(f"Ingrese las horas trabajadas el día {dia}: "))
    horas_trabajadas.append(horas)

# Calcular el total de horas trabajadas
total_horas = sum(horas_trabajadas)

# Calcular el sueldo
sueldo = total_horas * TARIFA_HORA

# Mostrar los resultados
print(f"Total de horas trabajadas: {total_horas} horas")
print(f"Sueldo: ${sueldo}")