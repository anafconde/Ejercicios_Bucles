#Version
#Enunciado del algoritmo: Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un espacio.

while True:
    char = input("dame un carácter, espacio para salir ").lower()
    if char == " ":
        break
    elif char in "aeiou":
        print("VOCAL")
    else:
        print("NO VOCAL")
