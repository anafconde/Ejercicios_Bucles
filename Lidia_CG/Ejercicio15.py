#Lidia Castro Gutiérrez
#Version 1

#Ejercicio 15. Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses.

mensualidad=10
total=0
print(f"La cuota del primer mes es {mensualidad} €")
for m in range(1,20):

    mensualidad=mensualidad*2
    total=total+mensualidad

    print(f"Cuota del mes {m+1} es de {mensualidad} €")

print(f"El total a pagar es {total} €")