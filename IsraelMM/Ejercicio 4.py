#Autor: Israel
#Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuántos números introducidos son mayores que 0, menores que 0 e iguales a 0.

mayores = 0
menores = 0
iguales = 0

cant = int(input("Dime la cantidad de numeros que quieres introducir: "))


while cant > 0:
    numero = int(input("Dime un numero: "))
    if numero > 0:
        mayores += 1
    elif numero < 0:
        menores += 1
    elif numero == 0:
        iguales += 1
    cant -= 1

print(f"Has introducido la cantidad de numero mayores a 0: {mayores}" )
print(f"Has introducido la cantidad de numero menores a 0: {menores}" )
print(f"Has introducido la cantidad de numero iguales a 0: {iguales}" )