#Creem funció Janken.

def janken ():
   
    #IMPORTEM LES FUNCIONS I MÈTODES NECESSARIS.
    from robot import playing #Importem la funció corresponent a la tria del contrincant.

    from time import sleep

    r=robot.robot() #crea instància de robot.

    p=r.playing() #crido mètode playing de robot. 
    
    #r2=robot.robot() <-- Així crearia instància 2 de robot, així puc fer que 2 robots juguin.
     
    def joc():
        
        movUsuariValid = False

        while movUsuariValid == False:
            
            movUsuari = input(f"Tria el teu pròxim moviment escrivint alguna de les paraules següents a la consola: \n 1.Pedra 💎 \n 2.Paper 🧻  \n 3.Tisores ✂ ").lower().strip()
            
            if movUsuari == "pedra" or movUsuari == "paper" or movUsuari == "tisores":

                movUsuariValid = True

                print("Pedra, paper, tisores!")

                sleep (3)

                print(f"El teu moviment és {movUsuari}")        

                sleep (3)

                print(f"El moviment del robot és {p}")

                sleep (3)

                #Casos en els que es guanya: 

                victories = [
                ("pedra", "tisores"),
                ("paper", "pedra"),
                ("tisores", "paper")
                ]

                if movUsuari == p:
                    
                    print("Empat!")


                elif (movUsuari, p) in victories:
                    
                    print("Has guanyat!")
                    

                
                else:
                    
                    print("Has perdut!")



                




        
        
        
        



        

    #TRIA DEL MODE DE JOC.
    modeValid = False

    while modeValid != False:
             
        modeJoc= input(f"Tria el mode de joc: \n 3.El primer que arribi a 3 victòries. \n 5.El millor de 5 jugades. \n S.Sortir").lower().strip()
        
        if modeJoc == "3" or modeJoc == "5" or modeJoc == "s":
        
            modeValid = True

            #Creem contadors per als punts de l'usuari i el robot.

            puntsUsuari = 0
            puntsRobot = 0

            match modeJoc:
                case "3": #El primer que arribi a 3 victòries.
                    
                    
                    
                    for i in range(3): #Repetim el joc 3 cops (escrivim 2 perque compta des de 0)
            
                        joc()

                case "5": #5.El millor de 5 jugades.
                    
                    

                    for i in range(5): #Repetim el joc 5 cops (escrivim 4 perque compta des de 0)
            
                        joc()

                case "s":
                    print("Has escollit sortir del joc. A continuació es tancarà. Fins a la pròxima!")
        

   









def nana(): #Definim la funció nana, a dins programem el joc d'averiguar el número.

    import random #Importem la funció random de Python (per això no cal definir from).
    
    numeroGenerat = random.randint(1,100) #Generem una variable on guardem un nombre aleatori comprés entre 1 i 100.

    numeroIntent = 0 #Creem una variable amb valor inicial 0 per fer un comptador d'intents.

    while True: #Creem un bucle infinit.

        numeroAverigua = int(input("He pensat un nombre entre 1 i 100. Prova d'endevinar-lo."))
        
        #Mostrem un missatge en pantalla
        #Demanem input a l'usuari, que guardem a la variable averigua
        #I castejem l'input a un numero per poder comparar averigua amb numeroGenerat 

        if numeroAverigua.is_integer == False: #Si l'input no és un nombre...

            numeroAverigua = int(input(f"He pensat un nombre entre 1 i 100. Prova d'endevinar-lo. \n INTRODUEIX UN NOMBRE."))
            #Tornem a demanar input a l'usuari.

        else: #Si l'input es pot castejar a número, (per tant, és un nº)...

            numeroIntent += 1; #Afegim 1 al comptador numeroIntent.

            if numeroAverigua > 200 or numeroAverigua <1: #Si l'input és +gran que 200 o +petit que 1...

                print ("L'input és massa gran o petit. Torna-ho a intentar. És un número entre 1 i 100.")
            
            else:
                 
                if numeroAverigua > numeroGenerat:
                    print ("Massa alt!")
            
                elif numeroAverigua < numeroGenerat:
                    
                    print ("Massa baix!")
                
                else :
                    
                    print (f"Felicitats! Has encertat en el teu intent número {numeroIntent}!")
                    break
