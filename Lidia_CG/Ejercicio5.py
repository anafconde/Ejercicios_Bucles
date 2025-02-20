#Lidia Castro Gutiérrez
#Version 1

#Ejercicio 5. Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un espacio.

caracter=0

while caracter!=" ":
    caracter=(input("Dime una letra: "))
    caracter=caracter.lower()

    if caracter == " ":
        print("Salimos...")
        break
    else:
        if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "0" or caracter == "u":
            print(f"El caracter {caracter} es una VOCAL")
        else:
            print(f"El caracter {caracter} es NO VOCAL")


 
    