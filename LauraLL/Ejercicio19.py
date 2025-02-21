#-------Autor:LauraLinares-------
#-----------Version:V1-----------
#-----Enunciado del ejercicio----
# Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que seleccionamos la opción de “Salir”

#-----Importador de programas----
import os
#---Inicializador de variables---

#---Inicializador del programa---

while True:
    # Programa para que se pueda utilizar el comando cls y limpiar la pantalla
    os.system("cls")
    
    # Menú de opciones
    print("")
    print("-----PROGRAMA PARA DESCUBRIR CURIOSIDADES SOBRE MI------")
    print("")
    print("1. ¿Nací en un año bisiesto?")
    print("2. ¿Cuál es mi horóscopo chino?")
    print("3. ¿Cuál será mi suerte este 2025 según mi horóscopo chino?")
    print("4. ¿Está mi número favorito dentro de la lista de números de la suerte del 2025?")
    print("5. Salir")
    print("")

    opc=int(input("Introduzca la opción (1,2,3,4,5): "))
    
    if opc <=0 or opc > 5:
        print("")
        print("Opción incorrecta, inténtelo de nuevo")
        #Mensaje para que el usuario pueda ver la respuesta antes de que se borre la pantalla y vuelva al menú
        print("")
        c=input("Pulse cualquier tecla para volver al menú ")
        continue

    else:
        if opc == 1:
            # Calcular si nació en un año bisiesto
            print("")
            print("---¿NACÍ EN UN AÑO BISIESTO?---")
            anyo=int(input("Introduzca su año de nacimiento: "))
            if (anyo%4 == 0 and anyo%100 != 0) or (anyo%400 == 0):
                print(f"Su año de nacimiento {anyo} es un año bisiesto")
            else:
                print(f"Su año de nacimiento {anyo} no es un año bisiesto")
            #Mensaje para que el usuario pueda ver la respuesta antes de que se borre la pantalla y vuelva al menú
            print("")
            c=input("Pulse cualquier tecla para volver al menú ")
                
        elif opc == 2:
            # Para saber el horóscopo chino, hay que saber el año en que nació
            print("")
            print("---¿CUÁL ES MI HORÓSCOPO CHINO?---")
            anyo=int(input("Introduzca su año de nacimiento: "))
            # Se resta al año 1900 porque el 1900 fue el año chino de la rata, así que partiendo de esa base, se puede crear el primer punto, que sería el % == 0 --> la rata
            # (He elegido la rata simplemente porque es el mío)
            animal=(anyo - 1900) % 12
                        
            # Dependiendo del resultado que me haya dado el resto de la división, será un animal u otro, empezando por la rata
            if animal == 0:
                print(f"Habiendo nacido en el año {anyo}, su horóscopo chino es LA RATA")
            elif animal == 1:
                print(f"Habiendo nacido en el año {anyo}, su horóscopo chino es EL BUEY")
            elif animal == 2:
                print(f"Habiendo nacido en el año {anyo}, su horóscopo chino es EL TIGRE")
            elif animal == 3:
                print(f"Habiendo nacido en el año {anyo}, su horóscopo chino es EL CONEJO")
            elif animal == 4:
                print(f"Habiendo nacido en el año {anyo}, su horóscopo chino es EL DRAGÓN")
            elif animal == 5:
                print(f"Habiendo nacido en el año {anyo}, su horóscopo chino es LA SERPIENTE")
            elif animal == 6:
                print(f"Habiendo nacido en el año {anyo}, su horóscopo chino es EL CABALLO")
            elif animal == 7:
                print(f"Habiendo nacido en el año {anyo}, su horóscopo chino es LA CABRA")
            elif animal == 8:
                print(f"Habiendo nacido en el año {anyo}, su horóscopo chino es EL MONO")
            elif animal == 9:
                print(f"Habiendo nacido en el año {anyo}, su horóscopo chino es EL GALLO")
            elif animal == 10:
                print(f"Habiendo nacido en el año {anyo}, su horóscopo chino es EL PERRO")
            elif animal == 11:
                print(f"Habiendo nacido en el año {anyo}, su horóscopo chino es EL JABALÍ")
            
            #Mensaje para que el usuario pueda ver la respuesta antes de que se borre la pantalla y vuelva al menú
            print("")
            c=input("Pulse cualquier tecla para volver al menú ")
        
        # Para comprobar la suerte, simplemente se pide el horóscopo, se transforma a mayúsculas para que no haya problemas de comprobaciones
        # y después se comprueba según la variable y se muestra la respuesta
        elif opc == 3:
            print("")
            print("---¿CUÁL SERÁ MI SUERTE EN 2025 SEGÚN EL HORÓSCOPO CHINO?---")
            horoscopo=input("Introduzca su horóscopo chino (sólo el nombre del animal): ")
            horoscopo=horoscopo.upper()

            if horoscopo == "RATA":
                print("Siendo del horóscopo de la RATA, su fortuna para este 2025 será...")
                print("La vida te pondrá a prueba y deberás afrontar muchos retos inesperados. Confía en tu potencial y nunca dudes de lo que puedes lograr este Año Nuevo Chino 2025. Medita y practica la introspección para encontrar la respuesta a los problemas.")
            elif horoscopo == "BUEY":
                print("Siendo del horóscopo del BUEY, su fortuna para este 2025 será...")
                print("Este año traerá amor y oportunidades de crecimiento en lo laboral, pero también situaciones que podrían generarte ansiedad. Trata de no engancharte en los problemas y fluir en los momentos de incertidumbre.")
            elif horoscopo == "TIGRE":
                print("Siendo del horóscopo del TIGRE, su fortuna para este 2025 será...")
                print("La magia del caos te hará salir de tu zona de confort y será ese “empujoncito” que necesitabas para hacer tus sueños realidad. ¡Aprovéchalo!")
            elif horoscopo == "CONEJO":
                print("Siendo del horóscopo del CONEJO, su fortuna para este 2025 será...")
                print("La buena fortuna estará de tu lado. Sin embargo, deberás cuidarte de las envidias y de las falsas amistades porque podrías perder todo en un abrir y cerrar de ojos.")
            elif horoscopo == "DRAGÓN" or horoscopo == "DRAGON":
                print("Siendo del horóscopo del DRAGÓN, su fortuna para este 2025 será...")
                print("Este Año Nuevo Chino 2025 el universo quiere que dejes de procastinar y te pondrá a prueba para que te retes y le pierdas el miedo al “qué dirán”. Empieza a ponerte metas por mes y no dejes para mañana lo que puedes empezar a resolver hoy.")
            elif horoscopo == "SERPIENTE":
                print("Siendo del horóscopo de la SERPIENTE, su fortuna para este 2025 será...")
                print("Antes de decir tu fortuna... ¡Felicidades! Este 2025 es el Año de la Serpiente, por lo que es tu año")
                print("Antes de tomar cualquier decisión trascendental en tu vida, tómate el tiempo necesario para elegir sabiamente y reflexionar. Las malas decisiones te podrían costar muchos años de mala fortuna, ¡no lo tomes a la ligera!")
            elif horoscopo == "CABALLO":
                print("Siendo del horóscopo del CABALLO, su fortuna para este 2025 será...")
                print("Estás en el mejor momento para dejar ir los rencores del pasado y abrirte a las nuevas oportunidades del 2025. Limpia tu aura con regularidad para asegurarte que nada absorba tu buena energía.")
            elif horoscopo == "CABRA":
                print("Siendo del horóscopo de la CABRA, su fortuna para este 2025 será...")
                print("En el Año Nuevo Chino 2025, la suerte estará de tu lado si te comprometes a dejar de lado los pretextos y te pones en acción con tus objetivos.")
            elif horoscopo == "MONO":
                print("Siendo del horóscopo del MONO, su fortuna para este 2025 será...")
                print("La buena energía estará al tope, por lo no que te faltarán nuevas oportunidades de crecimiento. Lo que sí te vamos a recomendar, es realizar limpiezas energéticas con frecuencia para evitar que el “mal de ojo” interrumpa tus planes.")
            elif horoscopo == "GALLO":
                print("Siendo del horóscopo del GALLO, su fortuna para este 2025 será...")
                print("A nivel personal, este es un buen momento para reflexionar sobre tus relaciones y fortalecer los vínculos con aquellos que te apoyan y siempre están de tu lado. No descuides aquellas amistades que te aportan amor y felicidad.")
            elif horoscopo == "PERRO":
                print("Siendo del horóscopo del PERRO, su fortuna para este 2025 será...")
                print("Si permites que las inseguridades te dominen, corres el riesgo de quedarte estancado/a. Empieza a dominar tus miedos y, en automático, las puertas de la abundancia se te abrirán.")
            elif horoscopo == "JABALÍ" or horoscopo == "JABALI":
                print("Siendo del horóscopo del JABALÍ, su fortuna para este 2025 será...")
                print("La vida te dará la mayor lección este Año Nuevo Chino 2025, lo que te hará madurar y crecer emocionalmente. Aprovecha de este aprendizaje para fortalecerte espiritualmente.")
            else:
                print("Error, el valor introducido no corresponde con uno de los animales")
            
            #Mensaje para que el usuario pueda ver la respuesta antes de que se borre la pantalla y vuelva al menú
            print("")
            c=input("Pulse cualquier tecla para volver al menú ")
        
        # Para comprobar el número de la suerte...
        elif opc == 4:
            print("")
            print("---¿ESTÁ MI NÚMERO FAVORITO DENTRO DE LA LISTA DE NÚMEROS DE LA SUERTE?---")

            # Recolección de datos
            num=int(input("Introduzca su número favorito del 1 al 9: "))
            horoscopo=input("Introduzca su horóscopo chino (sólo el nombre del animal): ")
            horoscopo=horoscopo.upper()

            if horoscopo == "RATA":
                if num == 2 or num == 3 or num == 6 or num == 9:
                    print(f"¡ENHORABUENA! El número {num} está en la lista de números de la suerte")
                else:
                    print(f"El número {num} no está en la lista de números de la suerte de este año, pero ¡puede que lo esté el año que viene! El número sigue siendo genial")
            elif horoscopo == "BUEY":
                if num == 1 or num == 4 or num == 6:
                    print(f"¡ENHORABUENA! El número {num} está en la lista de números de la suerte")
                else:
                    print(f"El número {num} no está en la lista de números de la suerte de este año, pero ¡puede que lo esté el año que viene! El número sigue siendo genial")
            elif horoscopo == "TIGRE":
                if num == 1 or num == 3 or num == 4 or num == 8:
                    print(f"¡ENHORABUENA! El número {num} está en la lista de números de la suerte")
                else:
                    print(f"El número {num} no está en la lista de números de la suerte de este año, pero ¡puede que lo esté el año que viene! El número sigue siendo genial")
            elif horoscopo == "CONEJO":
                if num == 3 or num == 4 or num == 6 or num == 7:
                    print(f"¡ENHORABUENA! El número {num} está en la lista de números de la suerte")
                else:
                    print(f"El número {num} no está en la lista de números de la suerte de este año, pero ¡puede que lo esté el año que viene! El número sigue siendo genial")
            elif horoscopo == "DRAGÓN" or horoscopo == "DRAGON":
                if num == 1 or num == 6 or num == 7 or num == 9:
                    print(f"¡ENHORABUENA! El número {num} está en la lista de números de la suerte")
                else:
                    print(f"El número {num} no está en la lista de números de la suerte de este año, pero ¡puede que lo esté el año que viene! El número sigue siendo genial")
            elif horoscopo == "SERPIENTE":
                if num == 2 or num == 8 or num == 9:
                    print(f"¡ENHORABUENA! El número {num} está en la lista de números de la suerte")
                else:
                    print(f"El número {num} no está en la lista de números de la suerte de este año, pero ¡puede que lo esté el año que viene! El número sigue siendo genial")
            elif horoscopo == "CABALLO":
                if num == 2 or num == 3 or num == 6 or num == 7:
                    print(f"¡ENHORABUENA! El número {num} está en la lista de números de la suerte")
                else:
                    print(f"El número {num} no está en la lista de números de la suerte de este año, pero ¡puede que lo esté el año que viene! El número sigue siendo genial")
            elif horoscopo == "CABRA":
                if num == 2 or num == 7 or num == 8:
                    print(f"¡ENHORABUENA! El número {num} está en la lista de números de la suerte")
                else:
                    print(f"El número {num} no está en la lista de números de la suerte de este año, pero ¡puede que lo esté el año que viene! El número sigue siendo genial")
            elif horoscopo == "MONO":
                if num == 4 or num == 7 or num == 9:
                    print(f"¡ENHORABUENA! El número {num} está en la lista de números de la suerte")
                else:
                    print(f"El número {num} no está en la lista de números de la suerte de este año, pero ¡puede que lo esté el año que viene! El número sigue siendo genial")
            elif horoscopo == "GALLO":
                if num == 3 or num == 5 or num == 7 or num == 8:
                    print(f"¡ENHORABUENA! El número {num} está en la lista de números de la suerte")
                else:
                    print(f"El número {num} no está en la lista de números de la suerte de este año, pero ¡puede que lo esté el año que viene! El número sigue siendo genial")
            elif horoscopo == "PERRO":
                if num == 3 or num == 4 or num == 9:
                    print(f"¡ENHORABUENA! El número {num} está en la lista de números de la suerte")
                else:
                    print(f"El número {num} no está en la lista de números de la suerte de este año, pero ¡puede que lo esté el año que viene! El número sigue siendo genial")
            elif horoscopo == "JABALÍ" or horoscopo == "JABALI":
                if num == 2 or num == 5 or num == 8 or num == 9:
                    print(f"¡ENHORABUENA! El número {num} está en la lista de números de la suerte")
                else:
                    print(f"El número {num} no está en la lista de números de la suerte de este año, pero ¡puede que lo esté el año que viene! El número sigue siendo genial")
            else:
                print("Error, el valor introducido como horóscopo no corresponde con uno de los animales")
            
            #Mensaje para que el usuario pueda ver la respuesta antes de que se borre la pantalla y vuelva al menú
            print("")
            c=input("Pulse cualquier tecla para volver al menú ")
        
        #Saliendo del menú
        elif opc == 5:
            print("Saliendo del programa de curiosidades")
            exit()
