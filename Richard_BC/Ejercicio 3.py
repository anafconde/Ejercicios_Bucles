#autor -------------Richard Bustamante Carreño
#version --------------version:1
#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.
contador = 0
suma = 0
while True:
    numero = int(input("Introduce numero para sumarlos y calcular su media, introduce 0 para terminar: "))
    if numero == 0:
        break
    else:
        suma = numero + suma
        contador += 1
media = suma / contador
print(f"La suma de los numeros es: {suma}, la media es: {media}")