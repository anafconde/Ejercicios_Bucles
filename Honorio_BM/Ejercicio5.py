#Autor: Honorio
#Version: 1.0
#5.Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un espacio.
caract=input("Intoduzca cualquier caracter: ")
contador=0

while caract != "":
    caract=input("Intoduzca cualquier caracter: ")
    if caract == "a" or caract == "e" or caract == "i" or caract == "o" or caract == "u":
        print("ES VOCAL")
        contador+=1
    elif caract == "":
        break
    else:
        print("No es vocal")
        




