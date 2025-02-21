# Author: Luis Palacios
# Version: 2.0

# 🔟 Ejercicio 10: Tabla de multiplicar de los primeros 5 números 🧮
# Algoritmo que muestre la tabla de multiplicar de los números 1, 2, 3, 4 y 5.

tecla=input("ENTER para mostrar las tablas de multiplicar de los números 1, 2, 3, 4 y 5: ")

for n2 in range(1,6):
    
    print("Tabla de multiplicar del número",n2)

    for n in range(1,11):

        tabla=n2*n
        print(n2,"x",n,"=",tabla)
