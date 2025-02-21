# Version 1.0
# Autor David García Pérez

#Ejercicio 7
#Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado

numero = int(input("Introduce un número: "))

print(f"Tabla de multiplicar del {numero}:")

for i in range(0, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")