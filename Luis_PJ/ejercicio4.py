# Author: Luis Palacios
# Version: 1.0

# Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir).
# El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

nintro=int(input("Cuantos números vas a introducir: "))
contpositivo=0
contnegativo=0
contigual=0

while nintro > 0:
    numero=int(input("Introduce un número: "))
    if numero > 0:
        contpositivo=contpositivo+1
        nintro=nintro-1
    elif numero < 0:
        contnegativo=contnegativo+1
        nintro=nintro-1
    else:
        contigual=contigual+1
        nintro=nintro-1
print("Has introducido",contpositivo,"números positivos",contnegativo,"numeros negativos y",contigual,"iguales a 0")
    