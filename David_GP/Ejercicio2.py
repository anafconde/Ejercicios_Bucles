# Version 1.0
# Autor David García Pérez

#Ejercicio 2
#Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido, a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número que había generado.

import random

def adivina_el_numero():

  numero_secreto = random.randint(1, 100)
  intentos_restantes = 10

  print("¡Bienvenido al juego de adivinar el número!")
  print("He generado un número aleatorio del 1 al 100.")

  while intentos_restantes > 0:
    try:
      adivina = int(input(f"Adivina el número (intentos restantes: {intentos_restantes}): "))
    except ValueError:
      print("Por favor, introduce un número válido.")
      continue

    if adivina < numero_secreto:
      print("El número secreto es mayor.")
    elif adivina > numero_secreto:
      print("El número secreto es menor.")
    else:
      print(f"¡Acertaste! El número secreto era {numero_secreto}. Lo has adivinado en {10 - intentos_restantes} intentos.")
      return

    intentos_restantes -= 1

  print(f"Te has quedado sin intentos. El número secreto era {numero_secreto}.")

if __name__ == "__main__":
  adivina_el_numero()