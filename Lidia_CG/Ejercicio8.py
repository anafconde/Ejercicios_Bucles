#Lidia Castro Gutiérrez
#Version 1

#Ejercicio 8. Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que el superior lo tiene que volver a pedir. A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:

    # La suma de los números que están dentro del intervalo (intervalo abierto).

    # Cuantos números están fuera del intervalo.

    # He informa si hemos introducido algún número igual a los límites del intervalo.

inf=int(input("Dime un número como límite inferior: "))
sup=int(input("Dime un número como límite superior: "))

if inf>=sup:
    print("El límite superior debe ser más alto que el límite inferior.")
    inf=int(input("Dime un número como límite inferior: "))
    sup=int(input("Dime un número como límite superior: "))

else:
    
    n=int(input("Dime un número para ver si está en ese intervalo: "))
    
    contador=0
    suma=0
    while n!=0:
        n=int(input("Dime un número para ver si está en ese intervalo: "))

        if n==0:
            break
        
        elif inf<n<sup:
            suma=suma+n

        elif n<inf or n>sup and n!=0:
            print(f"El número {n} está fuera del intervalo {inf}-{sup}")
            contador=contador+1
        elif n==inf:
            print(f"El número {n} es igual al límite inferior {inf}")
        elif n==sup:
            print(f"El número {n} es igual al límite superior {sup}")

    
    print(f"Hay {contador} numeros fuera del intervalo {inf}-{sup}.")
    
    
    print(f"La suma de todos los números que están dentro del intervalo es {suma}.")
   

    

    
    


