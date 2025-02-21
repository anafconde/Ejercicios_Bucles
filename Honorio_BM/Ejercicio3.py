#Autor: Honorio
#Version: 1.0
#3.Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.

num=int(input("Introduzca un numero: "))


contador=0
suma=0
while num != 0:
    num=int(input("Introduzca un numero: "))

    if num==0:
        break
    
    suma=suma+num
    contador=contador +1
if contador > 0:
    media= suma / contador
    print(f"La suma es {suma}")
    print(f"La media es {media}")
else:
    print("Error el numero introducido no es correcto.")












