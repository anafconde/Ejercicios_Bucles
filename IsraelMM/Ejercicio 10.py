#Autor: Israel
#Algoritmo que muestre la tabla de multiplicar de los números 1, 2, 3, 4 y 5.

for n1 in range(1,6):
    print(f"Tabla del {n1}")
    for n2 in range(0,11):
        mult = n1*n2
        print(f"{n1}*{n2} = {mult}")