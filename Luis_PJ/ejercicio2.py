# Author: Luis Palacios
# Version: 1.0

# Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. 
# A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido, 
# a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el
# número (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número 
# que había generado.

import random

intentos=10
num_secreto=random.randint(1,100)
contador=0

while contador < 10:
    numero=int(input("Introduce un número: "))
    if numero < num_secreto:
        print("El número introducido es más bajo que el número a adivinar")
        contador += 1
        print("LLevas",contador,"intentos")
    elif numero > num_secreto:
        print("El número introducido es más alto que el número a adivinar")
        contador += 1
        print("Llevas",contador,"intentos")
    else:
        print("Enhorabuena",num_secreto,"era el número a adivinar")
        break
    if contador == 10:
        print("Has agotado el número de intentos")



