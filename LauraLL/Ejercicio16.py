#-------Autor:LauraLinares-------
#-----------Version:V1-----------
#-----Enunciado del ejercicio----
# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana.
# Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, además, calcule cuánto pagó la empresa por los N empleados

#----Importador de bibliotecas---
import os

#---Inicializador de variables---
total=0

#---Inicializador del programa---
    # Limpio la pantalla antes de entrar al programa
os.system("cls")

empleados=int(input("¿Cuántos trabajadores se van a tener en cuenta para esta semana? "))

for trabajador in range(1,empleados+1):
    sueldo=float(input("¿Cuál es el sueldo base del empleado %d? " % trabajador))
    horas=float(input("¿Cuántas horas trabajó está semana el empleado %d? " % trabajador))
    s_semanal=sueldo*horas # Calculo el sueldo semanal por empleado
    total=total+s_semanal # Sumo el sueldo semanal de cada empleado a un total para el cálculo de todos los empleados
    print(f"El sueldo semanal del empleado {trabajador} es de {s_semanal} €")

print(f"El total que tendrá que pagar la empresa por los {empleados} empleados esta semana será de {total}")