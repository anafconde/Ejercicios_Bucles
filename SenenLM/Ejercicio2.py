#version 1.0
#author Senén Lara

# Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. 
# A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,
# a demás de los intentos que te quedan (tienes 10 intentos para acertarlo).
# El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), 
# si se llega al limite de intentos te muestra el número que había generado.


import random

numeroadivinar= random.randint(1,100)
intentos=10
while intentos > 0:
    print ("Juego de adivinar")
    numeroadivina=int(input("Introduce el numero para adivinar: "))
    if numeroadivinar < numeroadivina:
        print ("El numero es mas bajo")
        intentos = intentos -1
        print ("Te quedan",intentos,"intentos")
    elif numeroadivinar > numeroadivina:
        print ("El numero es mas alto")
        intentos = intentos - 1
        print ("Te quedan",intentos,"intentos")
    elif numeroadivina == numeroadivinar:
        print ("Has acertado!!")
        break
    if intentos == 0:
        print ("Te has quedado sin intentos :(")
    