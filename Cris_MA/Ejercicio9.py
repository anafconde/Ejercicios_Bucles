#Author: Cris Moreno    
#Version: 7.77
## **9️⃣ Ejercicio 9**: Potencia sin usar el operador de potencia ⚡
#Escribe un programa que, dados dos números, uno real (**base**) y un entero positivo (**exponente**), 
#saque por pantalla el resultado de la potencia.
#No se puede utilizar el operador de potencia.

real=int(input("Dime un numero real: "))
exp=int(input("Dime el exponente: "))
result=1

while exp>0:
    result=result*real
    exp -= 1
print (result)


