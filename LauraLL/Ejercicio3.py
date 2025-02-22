#-------Autor:LauraLinares-------
#-----------Version:V1-----------
#-----Enunciado del ejercicio----
# Algoritmo que pida números hasta que se introduzca un cero. 
# Debe imprimir la suma y la media de todos los números introducidos.

#----Importador de bibliotecas---
import os

#---Inicializador de variables---
print("---PROGRAMA PARA REALIZAR LA MEDIA DE NÚMEROS---")
n=float(input("Introduzca el primer número: "))
suma=n
contador=1

#---Inicializador del programa---
    # Limpio la pantalla antes de entrar al programa
os.system("cls")

while n!=0:
    n=float(input("Introduzca un número: "))
    if n==0:
        continue
    else:
        suma=suma+n
        contador=contador+1
    
media=suma/contador
print(f"La media de la suma de los números introducidos es: {media}")