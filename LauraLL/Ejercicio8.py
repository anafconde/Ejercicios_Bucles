#-------Autor:LauraLinares-------
#-----------Version:V1-----------
#-----Enunciado del ejercicio----
# Escribe un programa que pida el límite inferior y superior de un intervalo.
# Si el límite inferior es mayor que el superior, lo tiene que volver a pedir.
# A continuación, se van introduciendo números hasta que introduzcamos el 0.
# Cuando termine el programa, dará las siguientes informaciones:
# La suma de los números que están dentro del intervalo (intervalo abierto).
# Cuántos números están fuera del intervalo.
# Informa si hemos introducido algún número igual a los límites del intervalo

#----Importador de bibliotecas---
import os

#---Inicializador de variables---
num=1
contador=0
suma=0
n_fuera=0
igual=0

#---Inicializador del programa---
    # Limpio la pantalla antes de entrar al programa
os.system("cls")

print("---PROGRAMA NÚMEROS ENTRE INTERVALOS - PULSAR 0 PARA SALIR UNA VEZ INICIADO EL CONTEO---")

lim_inferior=float(input("Introduzca el límite inferior del intervalo: "))
lim_superior=float(input("Introduzca el límite superior del intervalo: "))

# Compruebo que el límite superior sea mayor al inferior y mientras no se introduzcan esos datos, el bucle sigue
while lim_inferior>lim_superior:
    print("Parece que ha ocurrido un problema")
    print(f"¡El límite superior {lim_superior} no puede ser más pequeño que el límite interior {lim_inferior}!")
    print("")
    print("Por favor, vuelva a introducir los datos")
    lim_inferior=float(input("Introduzca el límite inferior del intervalo: "))
    lim_superior=float(input("Introduzca el límite superior del intervalo: "))
    print("")

while num != 0:
    print("")
    # Amplio el contador para que el usuario sepa qué numero está introduciendo
    contador=contador+1
    # Pido el número al usuario
    num=float(input("Introduzca el número %d: " % contador))
    # Compruebo si se cumple la condición del while lo primero
    if num == 0:
        continue
    # Dependiendo del número que se introduzca:
    if num>lim_inferior and num<lim_superior: # Si está dentro del intervalo, se suma
        suma=suma+num
    elif num == lim_inferior or num == lim_superior: # Si es igual a uno de los límites, se añade a un contador
        igual=igual+1
    else: # Si está fuera de los límites, se añade a otro contador
        n_fuera=n_fuera+1

# Muestro los resultados finales
print("") # Abajo resto 1 al contador para eliminar al 0 que también se sumaría cuando se introduzca justo antes de salir del while
print(f"Tras el conteo de {contador-1} números, la suma de todos ellos es {suma}")
print(f"Ha habido {igual} números que eran iguales a los límites y {n_fuera} números que estaban fuera de ellos")