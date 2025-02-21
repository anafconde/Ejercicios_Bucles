#Author: Cris Moreno
#Version: 7.77
## **6️⃣ Ejercicio 6**: Números pares entre dos valores 🔢
#Escribir un programa que imprima todos los números **pares** entre dos números que se le pidan al usuario.

print("=Comprueba numeros pares=-")
num1=int(input("Dime un numero: "))
num2=int(input("Dime otro numero: "))

contador=0
while contador < 1:
    if num1%2 ==0:
        print(num1, "es par")
    if num2%2 ==0:
        print(num2, "es par")
    contador+=1
if num1%2 !=0 and num2%2 !=0:
    print("Ninguno de los dos numeros es par")


