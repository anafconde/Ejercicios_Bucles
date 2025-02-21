#autor -------------Richard Bustamante Carreño
#version --------------version:1
#Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que seleccionamos la opción de “Salir”.

while True:
    print("\nMenú de Opciones:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        print("Has seleccionado la Opción 1")
    elif opcion == "2":
        print("Has seleccionado la Opción 2")
    elif opcion == "3":
        print("Has seleccionado la Opción 3")
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")