#Lidia Castro Gutiérrez
#Version 1

#Ejercicio 1. Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120).


num=int(input("Dime un número que quieras factorizar: "))

if num < 0:
    print("El factorial no está definido para números negativos")
elif num==0:
    print("0!= 1")
else:
    factorial = 1
    for n in range(1, num + 1):
        factorial= factorial*n

    print(f"{num}! = {factorial}")



