#version 1.0
#author Senén Lara

#Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, 
#si al final de cada mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva ahorrado cada mes.
# Inicializa el ahorro total anual
ahorro = 0

for mes in range(1, 13):
    print ("Mes:",mes)
    cantidad = float(input("Ingrese la cantidad ahorrada en el mes: " ))
    
    ahorro = cantidad + ahorro
    
    print("Total ahorrado hasta el mes",mes, ahorro,)

print("Total ahorrado en el año:",ahorro,)
