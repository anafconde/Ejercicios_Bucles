#-------Autor:LauraLinares-------
#-----------Version:V1-----------
#-----Enunciado del ejercicio----
# Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana (seis días) 
# y requiere determinar el total de éstas, así como el sueldo que recibirá por las horas trabajadas

#----Importador de bibliotecas---
import os

#---Inicializador de variables---
total=0
horas_t=0

#---Inicializador del programa---
    # Limpio la pantalla antes de entrar al programa
os.system("cls")

print("----PROGRAMA CALCULADOR HORAS TRABAJADAS----")
sueldo=float(input("Introduzca el sueldo por hora del empleado: "))

# Para cada uno de los días de la semana, pido el numero de horas trabajadas y las añado a una variable
# Además, se va calculando el total a pagar al empleado
for i in range(1,7):
    h=float(input(f"Introduzca el número de horas trabajadas en el día {i}: "))
    horas_t=horas_t+h
    total=total+(h*sueldo)

print(f"El empleado que ha trabajado {horas_t} durante la semana, a {sueldo} € la hora, recibirá un total de: {total} €")
