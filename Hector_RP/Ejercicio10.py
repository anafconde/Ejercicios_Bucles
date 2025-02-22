#version 1.0
#author Héctor RP
#Ejercicio 10

numero = int(input("Introduce el número de la tabla de multiplicar (hasta el 5): "))

if numero > 5:
    print("No puedo multiplicar por números mayores a 5")
else:
    print(f"Tabla de multiplicar del {numero}:")
    for j in range(1, 11):
        print(f"{numero} x {j} = {numero * j}")
