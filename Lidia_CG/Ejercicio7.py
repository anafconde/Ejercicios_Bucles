#Lidia Castro Gutiérrez
#Version 1

#Ejercicio 7. Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.

num=int(input("Dime un número del que quieras la tabla de multiplicar: "))

for n in range(1, 11):
    
 print(f"{n} x {n} = {num * n}")

# n=1
# while n <= 10:
    # print(f"{num} x {n} = {num * n}")
    # n += 1