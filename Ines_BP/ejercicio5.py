#---------------Autor: inesmariabp---------------#
#---------------Version: 1.0---------------------#
#Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, 
#el programa termina cuando se introduce un espacio.

#Inicializar variables



#Inicio del programa-------------------
car="a"
while car!=" ":
    car=input("Introdue un carácter: ")
    car=car.upper()
    if car==" ":continue
    elif car=='A' or car=='E' or car=='I' or car=='O' or car=='U':
        print(f"El carácter {car} es una VOCAL")
    else:
        print(f"El carácter {car} es una CONSONANTE")