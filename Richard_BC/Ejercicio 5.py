#autor -------------Richard Bustamante Carreño
#version --------------version:1
#Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un espacio.
while True:
    caracter = input("Ingrese un carácter (espacio para terminar): ")
    if caracter == " ":
        break
    elif caracter in "aeiou":
        print("Vocal")
    else:
        print("No Vocal")
