#Lidia Castro Gutiérrez
#Version 1

#Ejercicio 18. Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.


horas=0
minutos=0
segundos=0

while horas < 24: 
    minutos = 0
    horas += 1

    while minutos < 59:
        segundos = 0
        minutos += 1

        while segundos < 60:
            segundos += 1
            print(f"{horas}:{minutos}:{segundos}")
        
    


