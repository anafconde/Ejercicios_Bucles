#Autor: Juan Manuel López Torres
#Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuántos números introducidos son mayores que 0, menores que 0 e iguales a 0.

numeros=int(input("Indica la cantidad de números que desees: "))

mayores= 0
menores= 0
iguales= 0

for i in range(numeros):
    num=int(input(f"Introduce el número que desees {i + 1}: "))

    if num > 0:
        mayores += 1
    elif num < 0:
        menores += 1
    else:
        iguales += 1

print("Los resultados son...")
print(f"Números mayores que 0: {mayores}")
print(f"Números menores que 0: {menores}")
print(f"Números iguales que 0: {iguales}")

