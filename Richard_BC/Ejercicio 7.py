#autor -------------Richard Bustamante Carreño
#version --------------version:1
#Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.

numero = 0
contador = 1
numero = int(input("Di un numero para ver su tabla de multiplicar: "))

print(f"Tabla de multiplicar del {numero}:")
for contador in range(1, 11):
    print(f"{numero} x {contador} = {numero * contador}")
