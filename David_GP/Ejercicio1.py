# Version 1.0
# Autor David García Pérez

#Ejercicio 1
#Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120).

# Solicita al usuario que ingrese un número
numero = int(input("Introduce un número para factorizar: "))

def factorial(numero):
  if numero == 0:
    return 1
  else:
    return numero * factorial(numero-1)

# Calcula el factorial del número
factorial_numero = factorial(numero)

# Imprime el resultado
print(f"El factorial de {numero} es {factorial_numero}")