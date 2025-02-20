#---------------Autor: inesmariabp---------------#
#---------------Version: 1.0---------------------#
#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y 
# la media de todos los números introducidos.

#Inicializar varibles
n=1
suma=0 #Suma de todos los números introducidos
contador=0 #Iteraciones que realiza el bucle


while n!=0 :
    n=float(input("Introduce un número: "))
    if n==0:continue
    else:
        suma=suma+n
        contador+=1
media=suma/contador
print(f"Has introducido {contador} que suman {suma}, la media es: {media}")
