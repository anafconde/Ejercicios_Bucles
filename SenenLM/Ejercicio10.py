#version 1.0
#author Senén Lara
#Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

numero = 1

while numero <= 5:
    print(f"Tabla de multiplicar del {numero}:")
    contador = 1
    while contador <= 10:
        print(f"{numero} x {contador} = {numero * contador}")
        contador = contador + 1
    print("Tabla del numero", numero)
    numero = numero + 1
