#-------Autor:LauraLinares-------
#-----------Version:V1-----------
#-----Enunciado del ejercicio----
# Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir).
# El programa debe informar de cuántos números introducidos son mayores que 0, menores que 0 e iguales a 0

#----Importador de bibliotecas---
import os

#---Inicializador de variables---
mayor=0
menor=0
igual=0

#---Inicializador del programa---
    # Limpio la pantalla antes de entrar al programa
os.system("cls")

num=int(input("Introduzca la cantidad de números que va a escribir: "))

for i in range(1,num+1):
    n=int(input("Introduzca el número %d: " % i))
    # Si el número es mayor que 0, se añade uno a su contador
    if n>0:
        mayor=mayor+1
    # Si el número es menor que 0, se añade uno a su contador
    elif n<0:
        menor=menor+1
    # En cualquier otro caso (es = 0), se añade uno a su contador
    else:
        igual=igual+1

# Se muestra el resultado final
print("")
print(f"De los {num} números introducidos, se han introducido:")
print(f"{mayor} números mayores que 0")
print(f"{menor} números menores que 0")
print(f"{igual} números iguales a 0")