#-------Autor:LauraLinares-------
#-----------Version:V1-----------
#-----Enunciado del ejercicio----
# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. Para esto, se registran los días que trabajó y las horas de cada día.
# Realice un algoritmo para determinar el sueldo semanal de N trabajadores y además calcule cuánto pagó la empresa por los N empleados

#----Importador de bibliotecas---
import os

#---Inicializador de variables---
total=0

#---Inicializador del programa---
    # Limpio la pantalla antes de entrar al programa
os.system("cls")

print("----PROGRAMA CALCULADOR DE NÓMINAS----")

n=int(input("Introduzca el número de trabajadores: "))

# Para registrar las horas y días trabajados en la semana por cada uno de los trabajadores
for i in range(1,n+1):
    total_horas=0
    sueldo_semanal=0
    print(f"En relación al empleado {i}, introduzca los siguientes datos:")
    sueldo=float(input("Sueldo base del empleado por hora: "))
    for u in range(1,8):
        print(f"En el día {u}")
        horas=float(input("¿Cuántas horas trabajó? "))
        # Añado a la variable total_horas las horas que ha trabajado cada día de la semana
        total_horas=total_horas+horas
    # Una vez que tengo el total de horas trabajadas, hago el sueldo semanal de ese empleado
    sueldo_semanal=total_horas*sueldo
    print(f"El sueldo semanal del empleado {i} es de: {sueldo_semanal} €")

    # Añado a la variable total, el sueldo semanal de cada empleado
    total=total+sueldo_semanal

# Muestro el total a pagar por la empresa por todos los empleados
print(f"La empresa deberá pagar por sus {n} empleados y el trabajo de estos realizado durante la semana, un total de {total} €")