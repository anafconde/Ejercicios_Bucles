# Ejercicio_12.py

ahorros_totales = 0
ahorros_mensuales = []

for mes in range(1, 13):
    deposito = int(input(f"Ingrese la cantidad depositada en el mes {mes}: "))
    ahorros_totales += deposito
    ahorros_mensuales.append(ahorros_totales)
    print(f"Ahorros acumulados hasta el mes {mes}: {ahorros_totales:.2f} euros")

print(f"\nEl total ahorrado en el año es: {ahorros_totales:.2f} euros")
