# Version 1.0
# Autor David García Pérez

# Ejercicio 6
# Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

# Solicitar al usuario que ingrese dos números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Imprimir los números pares entre num1 y num2
print(f"Los números pares entre {num1} y {num2} son:")

# Iterar del menor al mayor
for num in range(min(num1, num2), max(num1, num2) + 1):
    if num % 2 == 0:
        print(num)