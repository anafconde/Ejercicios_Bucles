#---------------Autor: inesmariabp---------------#
#---------------Version: 1.0---------------------#
#Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.

#Leer el número
n=int(input("Introduce un número: "))

for i in range (1,11):
    print(f"{n} X {i} = {n*i}")