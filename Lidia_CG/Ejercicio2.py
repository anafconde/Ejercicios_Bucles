#Lidia Castro Gutiérrez
#Version 1

#Ejercicio2. Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A continuación, va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido, además de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número (además te dice en cuántos intentos lo has acertado), y si llegas al límite de intentos, te muestra el número generado.

import random


num_secreto=random.randint(1,100)
contador=0

while contador < 10:
    numero=int(input("A ver si adivinas el número que esoy pensando: "))
    if numero < num_secreto:
        print("Ese número es más bajo que el número secreto")
        contador += 1
        print(f"LLevas {contador} intentos")
    elif numero > num_secreto:
        print("Ese número es más alto que el número secreto")
        contador += 1
        print(f"LLevas {contador} intentos")
    else:
        print(f"Has acertado!! {num_secreto} es el número que estaba pensando")
        break
    if contador == 10:
        print("No te quedan más intentos")

        
   


