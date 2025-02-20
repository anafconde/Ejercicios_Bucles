#---------------Autor: inesmariabp---------------#
#---------------Version: 1.0---------------------#
#Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por 
#pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.
#-------------------------------Declaración de variables-------------------------------
#-------------------------------Declaración de funciones-------------------------------
#-------------------------------Inicio de programa-------------------------------------

#Leer los números
base=float(input("Introduce un número: "))
exp=int(input("Introduce el exponente: "))

#Bucle FOR para multiplicar el número por si mismo
for i in range(1,exp+1):
    result=base*base

print(f"El resultado de: {base}^{exp} = {result}")