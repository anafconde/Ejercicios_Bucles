#-------Autor:LauraLinares-------
#-----------Version:V1-----------
#-----Enunciado del ejercicio----
# Mostrar en pantalla los N primeros números primos.
# Se pide por teclado la cantidad de números primos que queremos mostrar

#----Importador de bibliotecas---
import os
import math

#---Inicializador de variables---
numero=2 #Inicializo en 2 porque el 1 no es primo
contador=0

#---Inicializador del programa---
    # Limpio la pantalla antes de entrar al programa
os.system("cls")

num=int(input("¿Cuántos números primos quiere mostrar? "))

while contador<num:
    primo=1
    raiz=int(math.sqrt(numero))
    for n in range(2,raiz+1):
        if numero % n == 0:
            primo=0
            break
    if primo == 1:
        print(numero, "", end="")
        contador=contador+1 #Sumamos uno al contador porque se ha encontrado un primo

    numero=numero+1 #Vamos sumando uno a uno los numeros para ir recorriendolos todos
