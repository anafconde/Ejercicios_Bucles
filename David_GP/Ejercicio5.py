# Version 1.0
# Autor David García Pérez

#Ejercicio 5
#Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un espacio.

while True:
    caracter = input("Introduce un carácter:")

    if caracter == " ":
        break  # Termina el bucle si se introduce un espacio

    if caracter.lower() in "aeiou":
        print("VOCAL")
    else:
        print("NO VOCAL")

print("Programa terminado.")