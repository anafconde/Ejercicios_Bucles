# Author: Luis Palacios
# Version: 1.0

# 🔟 Ejercicio 10: Tabla de multiplicar de los primeros 5 números 🧮
# Algoritmo que muestre la tabla de multiplicar de los números 1, 2, 3, 4 y 5.

numero=int(input("Introduce el número (1 al 5) de la tabla de multiplicar que quieres ver: "))

if 1 <= numero < 6:

    print("Tabla de multiplicar del número",numero)

    for n in range(1,11):

        tabla=numero*n
        print(numero,"x",n,"=",tabla)
else:
    print("ERROR, disponible solo las tablas de multiplicar del 1 al 5")