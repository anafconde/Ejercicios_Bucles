# Version: 1.0
# Author: Hector Ramirez Pineda
# Ejercicio 8:

numero=1
contador_fuera=0
suma_dentro=0
contador_limite=0

limite_superior=int(input("Introduce el límite superior del intervalo: "))
limite_inferior=int(input("Introduce el límite inferior del intervalo: "))

while limite_inferior > limite_superior:
    print("El límite inferior no puede ser mayor al límite superior.")
    limite_superior=int(input("Introduce el límite superior del intervalo: "))
    limite_inferior=int(input("Introduce el límite inferior del intervalo: "))

while numero != 0:

    numero=int(input("Introduce un número (Pulsa 0 para salir): "))

    if limite_inferior < numero < limite_superior:
        suma_dentro += numero
    elif (numero < limite_inferior or numero > limite_superior) and numero != 0:
        print(f"El número {numero} no está dentro del intervalo ({limite_inferior}, {limite_superior}).")
        contador_fuera += 1
    elif numero != 0:
        print(f"El número {numero} está justo en el límite del intervalo ({limite_inferior}, {limite_superior}).")
        contador_limite += 1

    print(f"La suma de los números dentro del intervalo ({limite_inferior}, {limite_superior}) es: {suma_dentro}.")
    print(f"Se han ingresado {contador_fuera} número(s) fuera del intervalo.")
    print(f"Se han ingresado {contador_limite} número(s) en el límite del intervalo ({limite_inferior}, {limite_superior}).")
