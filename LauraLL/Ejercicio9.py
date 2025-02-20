#-----Autor:LauraLinares-----
#---------Version:V1---------
#Enunciado del ejercicio
#Escribe un programa que, dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado de la potencia.
#No se puede utilizar el operador de potencia

#Inicializador de variables--
potencia=1

#Inicializador del programa--
print("----PROGRAMA DE POTENCIAS----")
n=float(input("Introduzca el número base: "))
e=int(input("Introduzca el exponente: "))

print("Realizando la potencia...")

#Compruebo que el exponente no sea negativo ni cero
if e<0:
    print("El exponente introducido NO es un número entero positivo")
    exit()
elif e==0:
    print(f"La potencia del número {n} elevado a {e} = 1")
#Una vez que el exponente es un número entero positivo, procedo a realizar el exponente
else:
    for i in range(1,e+1):
        potencia=potencia*n

#Se imprime el resultado del programa
print(f"La potencia del número {n} elevado a {e} = {potencia}")