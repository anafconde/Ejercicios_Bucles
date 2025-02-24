#Author: Cris Moreno
#Version: 7.77
## **5️⃣ Ejercicio 5**: Clasificar vocales y no vocales 🔤
#Algoritmo que pida caracteres e imprima **‘VOCAL’** si son vocales y **‘NO VOCAL’** en 
#caso contrario.
#El programa termina cuando se introduce un **espacio**.

char=""
while char != " ":
    char=input("Introduce un caracter: ")
    if char.lower() =="a" or char.lower()=="e" or char.lower()=="i" or char.lower()=="o" or char.lower()=="u":
        print("VOCAL.")
    else:
        print("NO VOCAL ")
            
