#-------Autor:LauraLinares-------
#-----------Version:V1-----------
#-----Enunciado del ejercicio----
# Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100.
# A continuación, va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido, 
# además de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta 
# el número (además te dice en cuántos intentos lo has acertado), y si llegas al límite de intentos, te muestra el número generado

#-----Importador de programas----
import random #biblioteca generadora de números random

#---Inicializador de variables---
n=random.randint(1,100)
contador_fallo=10
contador_acierto=0

#---Inicializador del programa---
for i in range(1,11):
    print("")
    print(f"Intento número {i}")
    print("")
    n2=int(input("Introduzca un número del 1 al 100: "))
    contador_fallo=contador_fallo-1
    contador_acierto=contador_acierto+1
    if n2<n:
        print(f"El número {n2} es menor que el número a adivinar")
        print(f"Le quedan {contador_fallo} intentos")
    elif n2>n:
        print(f"El número {n2} es mayor que el número a adivinar")
        print(f"Le quedan {contador_fallo} intentos")
    else:
        print(f"¡Enhorabuena! Ha acertado el número. Su número introducido {n2} es igual al número generado aleatoriamente {n}")
        print(f"Lo ha acertado en tan sólo {contador_acierto} intentos")
        break
