# Version 1.0
# Autor David García Pérez

# Ejercicio 17
# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. Para esto, se registran los días que trabajó y las horas de cada día. Realice un algoritmo para determinar el sueldo semanal de N trabajadores y además calcule cuánto pagó la empresa por los N empleados.

# Constantes
TARIFA_HORA = 10  # Tarifa por hora trabajada

# Obtener el número de trabajadores
N = int(input("Ingrese el número de trabajadores: "))

# Inicializar variables para el total pagado
total_pagado = 0

# Repetir sobre cada trabajador
for trabajador in range(1, N + 1):
    print(f"\nTrabajador {trabajador}:")

    # Obtener las horas trabajadas por día
    horas_trabajadas = []
    for dia in range(1, 6):  # Asumiendo que la semana laboral es de 5 días
        horas = float(input(f"Ingrese las horas trabajadas el día {dia}: "))
        horas_trabajadas.append(horas)

    # Calcular el sueldo del trabajador
    sueldo = sum(horas_trabajadas) * TARIFA_HORA

    # Mostrar el sueldo del trabajador
    print(f"Sueldo del trabajador {trabajador}: ${sueldo}")

    # Sumar el sueldo al total pagado
    total_pagado += sueldo

# Mostrar el total pagado por la empresa
print(f"\nTotal pagado por la empresa: ${total_pagado}")