def janken ():
   
   from robot import playing #Importem la funció corresponent a la tria del contrincant.
   
   from main import Main

   def joc():
       
       contadorUsuari = 0
       contadorRobot = 0

       
       
#Obtenir input usuari i robot. Fer casos amb if i sumar-li al jugador corresponent 1p.

   def victoriaDe3():
       
       contadorUsuari = 0
       contadorRobot = 0

       for i in range(2):
           
           joc()

   def millorDe5():
       
       contadorUsuari = 0
       contadorRobot = 0
       
       while contadorUsuari <3 or contadorRobot <3:

            #Obtenir input usuari i robot. Fer casos amb if i sumar-li al jugador corresponent 1p.
    

   modeJoc = input(f"Benvingut al joc de pedra, paper, tisora. Tria el mode de joc: \n 3.El primer que arribi a 3 victòries. \n 5.Al millor de 5 rondes. \n S.Sortir")

   match modeJoc:
       
       case "3":
           
           print(f"Has escollit l'opció \"El primer que arribi a 3 victòries.\" ")

       case "5":
           
           print(f"Has escollit l'opció \"Al millor de 5 rondes.\" ")

       case "S":
           
           print("Has escollit l'opció de sortir. Ara retornaràs al menú principal.")
           return
           Main()

       case _:
           
           print(f"L'opció introduïda no és vàlida. \n ")


        
   

#moviment = input(f"Benvingut al joc de pedra, paper, tisora. \n Tria el teu moviment: \n 1.Pedra \n 2.Paper \n 3.Tisora \n S.Sortir")

   









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
