#Autor: Israel
#Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada mes deposita cantidades variables de dinero. Además, se quiere saber cuánto lleva ahorrado cada mes.

total = 0

for mes in range(1,13):
    mensual = int(input(f"Ahorro del mes {mes}: "))
    total += mensual
    print(f"Total ahorrado del mes {mes}: {total}")