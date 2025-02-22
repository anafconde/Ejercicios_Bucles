#Lidia Castro Gutiérrez
#Version 1

#Ejercicio 4. Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.


n=int(input("Dime cuántos números me vas a dar: "))

positivos=0
negativos=0
ceros=0
while n>0:
    num=int (input("Introduce un número: "))

    if num > 0:
        positivos=positivos+1
        n=n-1
    elif num < 0:
        negativos=negativos+1
        n=n-1
    else:
        ceros=ceros+1
        n=n-1

print(f'''Hay \n {positivos} números positivos \n {negativos} números negativos \n {ceros} numeros iguales a cero.''')