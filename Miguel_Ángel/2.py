#Autor: Miguel Ángel García Cortés
#Version: 1.0

#Descripción: Juego de adivinar el número. El programa genera un número aleatorio entre 1 y 100 y el usuario tiene
#10 intentos para adivinarlo. Tras cada intento, el programa le dirá al usuario si el número a adivinar es 
#mayor o menor que el introducido. Al finalizar, el programa le dirá al usuario si ha adivinado el número o no.


import random

def adivina_el_numero():
    numero_a_adivinar = random.randint(1, 100)
    intentos_restantes = 10
    print("Adivina el numero del 1 al 100")

    while intentos_restantes > 0:
        try:
            numero_introducido = int(input("Introduce un número: "))
            if numero_introducido < 1 or numero_introducido > 100:
                raise ValueError("El número debe estar entre 1 y 100.")
        except ValueError as e:
            print(e)
            continue

        intentos_restantes -= 1

        if numero_introducido < numero_a_adivinar:
            print(f"El número a adivinar es mayor. Te quedan {intentos_restantes} intentos.")
        elif numero_introducido > numero_a_adivinar:
            print(f"El número a adivinar es menor. Te quedan {intentos_restantes} intentos.")
        else:
            print(f"¡Felicidades! Has adivinado el número en {intentos_restantes} intentos.")
            return

    print(f"Lo siento, has agotado tus intentos. El número era {10 - numero_a_adivinar}.")

if __name__ == "__main__":
    adivina_el_numero()