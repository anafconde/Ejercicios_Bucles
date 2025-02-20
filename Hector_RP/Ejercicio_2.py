# Version: 1.0
# Author: Hector Ramirez Pineda
# Ejercicio 2:
# Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido, a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número que había generado.

import random

numero_secreto = random.randint(1, 100)
intentos = 10
contador = 0

while contador < intentos:

    adivinanza = int(input("Introduce un número (entre 1 y 100): "))
    
    contador += 1

    if adivinanza == numero_secreto:
        print(f"¡Felicidades! Has acertado el número en {contador} intentos.")
        break
    elif adivinanza < numero_secreto:
        print("El número a adivinar es mayor.")
    else:
        print("El número a adivinar es menor.")
    
    print(f"Te quedan {intentos - contador} intentos.")

else:
    print(f"Lo siento, has agotado los intentos. El número era {numero_secreto}.")
