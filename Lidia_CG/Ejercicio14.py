#Lidia Castro Gutiérrez
#Version 1

#Ejercicio 14. Una persona se encuentra en el kilómetro 70 de una carretera, otra se encuentra en el km 150, los coches tienen sentido opuesto y tienen la misma velocidad. Realizar un programa para determinar en qué kilómetro de esa carretera se encontrarán.

c1=70
c2=150

while c1>c2:
    c1=c1+1
    c2=c2-2
print(f"Los coches se encuentran en el kilómetro {c1}")