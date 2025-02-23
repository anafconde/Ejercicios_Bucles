#Author: Cris Moreno
#Version: 7.77
## **2️⃣0️⃣ Ejercicio 20**: Números primos hasta N 🔢
#Mostrar en pantalla los **N primeros números primos**.
#Se pide por teclado la cantidad de números primos que queremos mostrar.
import math
cant=int(input("Cuantos numeros primos quieres que te muestre?: "))
num=2

while cant>0:
    numeroPrimo=True
    raiz=int(math.sqrt(num))
    for i in range(2,raiz+1):
        if num%i==0:
            numeroPrimo=False
            break
    if numeroPrimo==True:
        print (num)
        cant-=1
    num+=1


    
    

