#Version
#Enunciado del algoritmo: Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.

suma = 0
contador = 0

while True:
    num = int(input("dame un número, 0 para salir "))
    if num == 0:
        break
    suma = suma + num
    contador = contador + 1

if contador > 0:
    print(f"Suma: {suma}, Media: {suma / contador}")
else:
    print("No se añadieron numeros")
