#Lidia Castro Gutiérrez
#Version 1

#Ejercicio 3. Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.

n=(int(input("Dime un número: ")))
contador=0
suma=0
while n!=0:
    n=(int(input("Dime un número: ")))

    if n==0:
        break

suma=suma+n
contador=contador+1

if contador > 0:
    media = suma / contador
    print(f"La suma de los números introducidos es: {suma}")
    print(f"La media de los números introducidos es: {media}")
else:
    print("Error, no has introducido ningún número")


    

