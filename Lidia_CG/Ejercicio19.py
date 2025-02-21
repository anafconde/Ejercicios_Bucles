#Lidia Castro Gutiérrez
#Version 1

#Ejercicio 19. Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que seleccionamos la opción de “Salir”.

opc=0
while opc!=4: 
    
    print("-- MENÚ --")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")
    
   
    opc = int(input("Seleccione una opción: "))
    
    
    if opc == 1:
        print("Has seleccionado la Opción 1.")
        
    elif opc == 2:
        print("Has seleccionado la Opción 2.")
        
    elif opc == 3:
        print("Has seleccionado la Opción 3.")
        
    elif opc == 4:
        print("Saliendo....")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

