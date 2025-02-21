#Autor: Honorio
#Version: 1.0
#1.Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de todos los enteros entre 1 y
# el propio número y se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120).


num=int(input("Introduzca el un numero: "))
resultado = 1
if num < 0:
    print("No existe factorial de negativos")
else:
    for n in range(1,num+1):
        resultado= resultado * n
        print (f"!{num}={n}x={resultado}")    
    
    
    



