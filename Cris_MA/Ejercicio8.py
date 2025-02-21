#Author: Cris Moreno
#Version: 7.77
## **8️⃣ Ejercicio 8**: Intervalo de números 📏
#Escribe un programa que pida el **límite inferior** y **superior** de un intervalo.
#Si el límite inferior es mayor que el superior, lo tiene que volver a pedir.
#A continuación, se van introduciendo números hasta que introduzcamos el 0.
#Cuando termine el programa, dará las siguientes informaciones:

# - La **suma** de los números que están dentro del intervalo (intervalo abierto).
# - Cuántos números están **fuera del intervalo**.
# - Informa si hemos introducido algún número **igual a los límites del intervalo**.



limiteInf=int(input("Dime el limite inferior del intervalo: "))
limiteSup=int(input("Dime el limite superior del intervalo (Debe ser superior al limite inferior): "))

while limiteSup < limiteInf:
    limiteInf=int(input("Dime el limite inferior del intervalo: "))
    limiteSup=int(input("Dime el limite superior del intervalo (Debe ser superior al limite inferior): "))

contFuera=int(0)
suma=0
contLimite=0

num=1
while num !=0:
    num=int(input("Introduce un numero: "))
    if num==limiteInf or num==limiteSup:
        contLimite +=1
    if (num>limiteSup or num<limiteInf) and num!=0:
        contFuera +=1
    if num<limiteSup and num>limiteInf:
        suma=suma+num

print(f"Los numeros que has introducido suman {suma}, has introducido {contFuera} numeros fuera del intervalo y {contLimite} que son algun limite del intervalo ")







