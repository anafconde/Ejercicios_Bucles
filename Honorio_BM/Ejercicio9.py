#Autor: Honorio
#Version: 1.0
#9.Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado
# de la potencia. No se puede utilizar el operador de potencia.


base=int(input("Introduzca la base: "))
exponente=int(input("Introduzca el exponente: "))
if exponente < 0:
    print("Debe de ser un entero positivo")
else:
    resultado = 1
    for n in range(1,base+1):
        resultado=resultado*base
    print(f"El resultado es {resultado}")










