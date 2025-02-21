#Autor: Juan Manuel López Torres
#Crea una aplicación que pida un número y calcule su factorial. El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se representa por el número seguido de un signo de exclamación. Por ejemplo: 5! = 1x2x3x4x5 = 120.

numero=int(input("Escribe el número que desees: "))

contador= 1
resultado= 1

if numero < 0:
    print("No se puede factorizar debido a que su número es negativo....")
elif numero == 0:
    print("El resultado es 1....")

while contador <= numero:
    resultado= resultado * contador
    contador += 1

print(f"El factorial de {numero} es {resultado}")