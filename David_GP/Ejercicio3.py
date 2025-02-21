# Version 1.0
# Autor David García Pérez

#Ejercicio 3
#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.

suma = 0
contador = 0

while True:
    numero = int(input("Introduce un número:"))
    if numero == 0:
        break
    suma += numero
    contador += 1

if contador > 0:
    media = suma / contador
    print(f"La suma de los números es: {suma}")
    print(f"La media de los números es: {media}")
else:
    print("No se introdujeron números.")