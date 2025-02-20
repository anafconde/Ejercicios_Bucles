#-----Autor:LauraLinares-----
#---------Version:V1---------
#Enunciado del ejercicio
#Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ 
#en caso contrario, el programa termina cuando se introduce un espacio

c=0

while c != " ":
    c=input("Introduzca un caracter cualquiera: ")
    c=c.upper()
    if c == " ":
        continue
    else:
        if c == "A" or c == "E" or c == "I" or c == "O" or c == "U":
            print(f"El caracter introducido {c} ES UNA VOCAL")
        else:
            print(f"El caracter introducido {c} NO ES VOCAL")

