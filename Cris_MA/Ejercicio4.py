#Author: Cris Moreno
#Version: 7.77

# **4️⃣ Ejercicio 4**: Contar números positivos, negativos e iguales a cero ➗
# Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a 
# introducir).
# El programa debe informar de cuántos números introducidos son **mayores que 0**, 
# **menores que 0** e **iguales a 0**.

contadorPositivo=0
contadorNegativo=0
contadorCero=0


numeros=int(input("Cuantos numeros vas a introducir?: "))

while numeros > 0:
    numero=int(input("Dime un numero: "))
   
    if numero ==0:
        contadorCero=contadorCero+1
    elif numero > 0:
        contadorPositivo=contadorPositivo+1
    elif numero < 0:
        contadorNegativo=contadorNegativo+1
    numeros -=1
print("Resultados:")
print(f"Has introducido {contadorNegativo} numero(s) menor(es) que 0. ")
print(f"Has introducido {contadorPositivo} numero(s) mayor(es) que 0. ")
print(f"Has introducido {contadorCero} numero(s) que son/es 0. ")