#version 1.0
#author Senén Lara

#Escribe un programa que pida el limite inferior y superior de un intervalo. 
# Si el límite inferior es mayor que el superior lo tiene que volver a pedir. 
# A continuación se van introduciendo números hasta que introduzcamos el 0. 
# Cuando termine el programa dará las siguientes informaciones:

#•La suma de los números que están dentro del intervalo (intervalo abierto).

#•Cuantos números están fuera del intervalo.

#•He informa si hemos introducido algún número igual a los límites del intervalo.
liminferior = int(input("Introduce el limite inferior: "))
limsuperior = int(input("Introduce el limite superior: "))
while liminferior > limsuperior:
    print ("No puede ser que el limite inferior sea mas grande que el inferior!")
    liminferior = int(input("Introduce el limite inferior: "))
    limsuperior = int(input("Introduce el limite superior: "))
num=int(input("Introduce numeros! "))
suma = 0
fuera = 0
if num > liminferior and num < limsuperior:
    suma = num    
while num != 0:
    num=int(input("Introduce numeros! "))
    if num > liminferior and num < limsuperior:
        suma = num + suma
    elif num < liminferior or num > limsuperior:
        fuera = fuera + 1
    elif num == liminferior or num == limsuperior:
        print ("Tu numero ", num , "es igual a uno dentro de los limites del intervalo")
print ("La suma de los numeros de dentro del intervalo es",suma,"y has introducido",fuera,"numeros fuera del intervalo")
        
    


