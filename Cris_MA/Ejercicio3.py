#Author: Cris Moreno
#Version: 7.77
## **3️⃣ Ejercicio 3**: Suma y media de números ➕
#Algoritmo que pida números hasta que se introduzca un **cero**.
#Debe imprimir la **suma** y la **media** de todos los números introducidos.
suma=0
contador=0
num=1
while num !=0:
    num=int(input("Introduce un numero: ")) 
    suma=suma+num
    contador +=1
media=suma/(contador-1)
print (f"La suma de los numeros introducidos es {suma} y la media es {media} ")
