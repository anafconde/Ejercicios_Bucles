#Author: Cris Moreno
#Version: 7.77

#Ejercicio 2
#Crea una aplicación que permita adivinar un número. La aplicación genera un número
#aleatorio del 1 al 100. A continuación va pidiendo números y va respondiendo si el número
#a adivinar es mayor o menor que el introducido, a demás de los intentos que te quedan 
#(tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número 
#(además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos 
#te muestra el número que había generado.


import random
aleatorio=random.randint(1,100)
contador=1
while contador < 11:
    numero=int(input("Intenta adivinar un numero del 1 al 100: "))
    if numero == aleatorio:
        print("Enhorabuena!, has acertado el numero 🏆🥇👏 ")
        break
    elif numero < aleatorio:
        print("El numero que buscas es MAYOR")
        print(f"Llevas {contador} intentos de 10 ")
    elif numero > aleatorio:
        print("El numero que buscas es MENOR")
        print(f"Llevas {contador} intentos de 10 ")
    contador +=1
if contador==11:
        print("Has agotado los intentos.")