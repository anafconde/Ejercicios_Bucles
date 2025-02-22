# Ejercicio_12.py

ahorros_totales = 0
ahorros_mensuales = []

for mes in range(1, 13):
    deposito = int(input(f"Ingrese la cantidad depositada en el mes {mes}: "))
    ahorros_totales += deposito
    ahorros_mensuales.append(ahorros_totales)
    print(f"Ahorros acumulados hasta el mes {mes}: {ahorros_totales} euros")

print(f"El total ahorrado en el año es: {ahorros_totales} euros")
