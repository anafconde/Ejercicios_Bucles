#Lidia Castro Gutiérrez
#Version 1

#Ejercicio 20. Mostrar en pantalla los N primeros números primos. Se pide por teclado la cantidad de números primos que queremos mostrar.


import math

N=int(input("Cuántos números primos quieres ver?: "))
contador=0
num=1
while N>contador:
        num=num+1
        primo=1
                
        for n in range(2,int(math.sqrt(num))+1):

            if num % n==0:
                primo=0
                break
        if primo==1:
                
                contador=contador+1
                print(num," ",end="")
            





