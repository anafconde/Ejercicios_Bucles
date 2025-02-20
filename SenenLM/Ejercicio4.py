#version 1.0
#author Senén Lara

#Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). 
#El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.


cuentanumeros = int(input("Introduce cuantos numeros vas a introducir: "))
positivos= 0
negativos = 0
neutros = 0
while cuentanumeros > 0:
    numero=int(input("Introduce tu numero: "))
    if numero > 0:
        positivos = positivos + 1
        cuentanumeros = cuentanumeros -1
    elif numero < 0:
        negativos = negativos + 1
        cuentanumeros = cuentanumeros -1
    elif numero == 0:
        neutros = neutros + 1
        cuentanumeros = cuentanumeros -1
print ("Tienes",positivos,"Numeros positivos,",negativos,"Numeros negativos y",neutros,"ceros")
    
