# Version 1.0
# Autor David García Pérez


# Ejercicio 4
# Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

# Obtener la cantidad de números a introducir
cantidad_numeros = int(input("Ingrese la cantidad de números a introducir: "))

# Inicializar contadores
positivos = 0
negativos = 0
ceros = 0

# Iterar sobre cada número
for i in range(cantidad_numeros):
    numero = float(input(f"Ingrese el número {i+1}: "))

    # Incrementar el contador correspondiente
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1

# Mostrar los resultados
print(f"\nNúmeros mayores que 0: {positivos}")
print(f"Números menores que 0: {negativos}")
print(f"Números iguales a 0: {ceros}")