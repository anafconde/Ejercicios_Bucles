# Author: Luis Palacios
# Version: 1.0

# 8️⃣ Ejercicio 8: Intervalo de números 📏
# Escribe un programa que pida el límite inferior y superior de un intervalo.
# Si el límite inferior es mayor que el superior, lo tiene que volver a pedir.
# A continuación, se van introduciendo números hasta que introduzcamos el 0.
# Cuando termine el programa, dará las siguientes informaciones:

# La suma de los números que están dentro del intervalo (intervalo abierto).
# Cuántos números están fuera del intervalo.
# Informa si hemos introducido algún número igual a los límites del intervalo.

numero=1
cont=0
total=0
cont2=0

limsuperior=int(input("Introduce el limite superior de tu intervalo: "))
liminferior=int(input("Introduce el límite inferior de tu intervalo: "))

while liminferior > limsuperior:
    print("ERROR. El limite inferior debe ser menor que el límite superior.")
    limsuperior=int(input("Introduce el limite superior de tu intervalo: "))
    liminferior=int(input("Introduce el límite inferior de tu intervalo: "))

while numero != 0:

    numero=0
    numero=int(input("Introduce un número(Pulsa 0 para salir): "))

    if numero > liminferior and numero < limsuperior:
        total=total+numero
    elif (numero < liminferior or numero > limsuperior) and numero != 0:
        print(numero,"está fuera del límite (",liminferior,",",limsuperior,")")
        cont = cont + 1
    else:
        print(numero,"está en el límite del intervalo (",liminferior,",",limsuperior,")")
        cont2=cont2+1

print("La suma de los números introducidos dentro del intervalo (",liminferior,",",limsuperior,") es: ",total)
print("Has introducido",cont,"numero/s fuera de los límites")
print("Se han introducido",cont2, "números en el límite del intervalo (",liminferior,",",limsuperior,")")

