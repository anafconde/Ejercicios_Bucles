#-----Autor:LauraLinares-----
#---------Version:V1---------
#Enunciado del ejercicio
#Crea una aplicación que pida un número y calcule su factorial 
#(El factorial de un número es el producto de todos los enteros entre 1 y el propio número y 
#se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120)

#--Iniciación de variables----
fact=1

numero=int(input("Por favor, introduzca un número: "))

for n in range(1,numero+1):
    fact=fact*n

print(f"{numero}! = {fact}")
