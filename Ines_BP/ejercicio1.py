#---------------Autor: inesmariabp---------------#
#---------------Version: 1.0---------------------#
#Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de todos 
#los enteros entre 1 y el propio número y se representa por el número seguido de un signo de exclamación. 
#Por ejemplo 5! = 1x2x3x4x5=120).

#Inicializar variables
fact=1

#Leer el número
n=int(input("Introduce un número: "))

#Realizar un bucle con FOR
for i in range(1,n+1):
    fact=fact*i
print(f"{n}! = {fact}")