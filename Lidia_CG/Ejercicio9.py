#Lidia Castro Gutiérrez
#Version 1

#Ejercicio 9. Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.

nb=int(input("Dime un número como base de una potencia: "))
ne=int(input("Dime un número como exponente de una potencia: "))

if ne < 0:
    print("El exponente debe ser un entero positivo.")

else:

    resultado = 1
    for n in range(1,ne+1):
        resultado =resultado * nb
    
    
    print(f"{nb} elevado a {ne} es {resultado}")