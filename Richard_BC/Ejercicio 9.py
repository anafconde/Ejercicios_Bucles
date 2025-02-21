#autor -------------Richard Bustamante Carreño
#version --------------version:1
#Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.

base = int(input("Introduce el numero: "))
exponente = int(input("Introduce el numero al que quieres exponer: "))
resultado = 1
contador = 0

while contador < exponente:
    resultado = resultado * base
    contador += 1

print(f"{base} Elevado a {exponente} es {resultado}")