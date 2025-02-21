# Version 1.0
# Autor David García Pérez

# Ejercicio 15
# Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses.

# Número de meses
meses = 20

# Pago inicial
pago_inicial = 10

# Calcular el total pagado
total_pagado = 0
pago_actual = pago_inicial

for mes in range(1, meses + 1):
    total_pagado += pago_actual
    pago_actual *= 2  # Duplicar el pago para el siguiente mes

# Mostrar los resultados
print(f"Pago mensual del mes {mes}: {pago_actual} €")
print(f"Total pagado después de {meses} meses: {total_pagado} €")