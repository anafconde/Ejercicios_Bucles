#Author: Cris Moreno
#Version: 7.77

## **1️⃣5️⃣ Ejercicio 15**: Pago mensual de producto 🛒
#Una persona adquirió un producto para pagar en **20 meses**. El primer mes pagó 10 €, el segundo 20 €, 
#el tercero 40 € y así sucesivamente.
#Realizar un algoritmo para determinar cuánto debe pagar **mensualmente** y el **total de lo que pagó** después 
#de los 20 meses.

mes=1
pagoMes=10
suma=0
while mes <=20:
    print(f"El mes {mes} debe pagar {pagoMes} ")
    pagoMes=pagoMes*2
    suma=suma+pagoMes
    mes += 1

print(f"El total a pagar es de {suma}€")




