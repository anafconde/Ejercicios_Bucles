# Version 1.0
# Autor David García Pérez

#Ejercicio 9
#Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.

def potencia(base, exponente):

    resultado = 1
    for _ in range(exponente):
        resultado *= base
    return resultado

base = float(input("Introduce la base (número real): "))
exponente = int(input("Introduce el exponente (entero positivo): "))

if exponente < 0:
    print("El exponente debe ser un entero positivo.")
else:
    resultado = potencia(base, exponente)
    print(f"{base} elevado a {exponente} es: {resultado}")