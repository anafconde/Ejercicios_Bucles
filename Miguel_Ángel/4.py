#Autor: Miguel Angel Garcia Cortes
#Version: 1.0

#Descripcion: Este programa solicita al usuario una cantidad de números y devuelve cuantos son mayores que 0, 
#menores que 0 e iguales a 0.

cantidad = int(input("Introduce la cantidad de números: "))

mayores_que_cero = 0
menores_que_cero = 0
iguales_a_cero = 0

for _ in range(cantidad):
    numero = float(input("Introduce un número: "))
    if numero > 0:
        mayores_que_cero += 1
    elif numero < 0:
        menores_que_cero += 1
    else:
        iguales_a_cero += 1

print(f"Números mayores que 0: {mayores_que_cero}")
print(f"Números menores que 0: {menores_que_cero}")
print(f"Números iguales a 0: {iguales_a_cero}")