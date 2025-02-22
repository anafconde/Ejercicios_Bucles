# Version 1.0
# Autor David García Pérez

# Ejercicio 19
# Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que seleccionamos la opción de “Salir”.

while True:
    print("\nMenú:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Ha seleccionado la opción 1.")
    elif opcion == "2":
        print("Ha seleccionado la opción 2.")
    elif opcion == "3":
        print("Ha seleccionado la opción 3.")
    elif opcion == "4":
        print("Saliendo del programa...")
        break  # Sale del bucle while
    else:
        print("Opción inválida. Por favor, ingrese un número del 1 al 4.")