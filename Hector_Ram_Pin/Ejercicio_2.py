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
