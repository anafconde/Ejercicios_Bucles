#-------Autor:LauraLinares-------
#-----------Version:V1-----------
#-----Enunciado del ejercicio----
# Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, 
# si al final de cada mes deposita cantidades variables de dinero. Además, se quiere saber cuánto lleva ahorrado cada mes

#----Importador de bibliotecas---
import os

#---Inicializador de variables---
ahorros=0

#---Inicializador del programa---
    # Limpio la pantalla antes de entrar al programa
os.system("cls")

for i in range(1,12):
    dinero=float(input("Introduzca el dinero ahorrado durante el mes %d: " % i))
    ahorros=ahorros+dinero
    round(ahorros,2) # Se redondea a dos para que no salga con mil decimales si metiese céntimos
    print(f"En el mes {i} ha ahorrado {dinero} € y lleva en total {ahorros} € ahorrados")
    print("")
