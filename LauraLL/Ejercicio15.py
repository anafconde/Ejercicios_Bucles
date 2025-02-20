#-------Autor:LauraLinares-------
#-----------Version:V1-----------
#-----Enunciado del ejercicio----
# Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente.
# Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses

#-----Importador de programas----

#---Inicializador de variables---
pago=10
total=0

#---Inicializador del programa---

print(f"Durante el mes 1 tendrá que pagar {pago} €")

for i in range (2,21):
    pago=pago*2
    total=total+pago
    print(f"Durante el mes {i} tendrá que pagar {pago} €")

print(f"El total del pago será de {total} €")