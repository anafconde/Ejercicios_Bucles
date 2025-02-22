#Lidia Castro Gutiérrez
#Version 1

#Ejercicio 10. Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

for num in range(1,6):

    print(f"--- Tabla del {num} ---")

    for n in range(0,11):
        print(f"{num} x {n} = {num * n}")