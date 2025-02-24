#Author: Cris Moreno
#Version: 7.77
## **7️⃣ Ejercicio 7**: Tabla de multiplicar 🧮
#Realizar un algoritmo que muestre la **tabla de multiplicar** de un número introducido por teclado.


mult=int(input("Dime un numero para calcular su tabla de multiplicar: "))
for i in range(1,11):
    result=mult*i
    print(f"{mult}x{i}={result}")
