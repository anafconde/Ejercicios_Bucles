#Lidia Castro Gutiérrez
#Version 1

#Ejercicio 12. Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva ahorrado cada mes.

total=0

for n in range(1,13):

    m=float(input(f"¿Cuánto dinero has ahorrado el mes {n}?: "))

    total=total+m

    print(f"En total llevas ahorrado {total} €")

print(f"Llevas ahorrado en un año {total} €")