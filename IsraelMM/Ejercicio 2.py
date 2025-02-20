#Autor: Israel
#Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido, a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número que había generado.

import random

intentos=10
num_secreto = random.randint(1,100)
contador=0

while contador <= 10:
    num=int(input("Adivine el numero: "))
    if num < num_secreto:
        print("El numero introducido es mas bajo")
    elif num > num_secreto:
        print("El numero introducido es mas alto")
    else:
        input("Bravoooo acertastee")
        break
    contador = contador+1
