#Autor: Juan Manuel López Torres
#Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A continuación, va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido, además de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número (además te dice en cuántos intentos lo has acertado), y si llegas al límite de intentos, te muestra el número generado.

numero=int(input("Indique un número entre el 1 y el 100: "))
intentos= 10

print("Adivine el número seleccionado por el usuario: ")

while intentos > 0:
    num=int(input("Indique un número y prueba suerte a adivinar el número secreto: "))

    if numero < 1 and numero > 100:
        print("ERROR. Debe de escoger un número entre el 1 y el 100")
        continue
    if numero == num:
        print("!Felicidades!!, Has adivinado el número")
        break
    elif numero > num:
        print("El número a adivinar es mayor que el indicado")
    else:
        print("El número a adivinar es menor que el indicado")

    intentos -= 1

    if intentos == 0:
        print("Ohhh que pena, te has quedado sin intentos")

