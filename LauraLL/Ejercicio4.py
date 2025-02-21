#-------Autor:LauraLinares-------
#-----------Version:V1-----------
#-----Enunciado del ejercicio----
# Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir).
# El programa debe informar de cuántos números introducidos son mayores que 0, menores que 0 e iguales a 0

#-----Importador de programas----

#---Inicializador de variables---
mayor=0
menor=0
igual=0

#---Inicializador del programa---
num=int(input("Introduzca la cantidad de números que va a escribir: "))

for i in range(1,num+1):
    n=int(input("Introduzca el número %d: " % i))
    if n>0:
        mayor=mayor+1
    elif n<0:
        menor=menor+1
    else:
        igual=igual+1

print("")
print(f"De los {num} números introducidos, se han introducido:")
print(f"{mayor} números mayores que 0")
print(f"{menor} números menores que 0")
print(f"{igual} números iguales a 0")