#-------Autor:LauraLinares-------
#-----------Version:V1-----------
#-----Enunciado del ejercicio----
# Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ 
# en caso contrario, el programa termina cuando se introduce un espacio

#----Importador de bibliotecas---
import os

#---Inicializador de variables---
c=0

#---Inicializador del programa---
    # Limpio la pantalla antes de entrar al programa
os.system("cls")

while c != " ":
    c=input("Introduzca un caracter cualquiera: ")
    # Transformo el valor introducido a mayúsculas para tener un mayor control
    c=c.upper()
    # Primero verifico que no se ha introducido el carácter de la condición
    if c == " ":
        continue
    # Verifico si es igual a una vocal o no
    else:
        if c == "A" or c == "E" or c == "I" or c == "O" or c == "U":
            print(f"El caracter introducido {c} ES UNA VOCAL")
        else:
            print(f"El caracter introducido {c} NO ES VOCAL")

