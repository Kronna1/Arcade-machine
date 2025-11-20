

#DEFINICIÓ DE LES FUNCIONS

def Main ():

    #IMPORTEM LES FUNCIONS NECESSÀRIES

    from time import sleep #Importen el mètode sleep de la llibreria time. 

    from jocs import janken #Importen la funció Janken del fitxer jocs. 

    from jocs import nana #Importen la funció nana del fitxer jocs. 

    #DEFINICIÓ DEL BUCLE

    while True: #Fem un bucle infinit.

        print(f"--- BENVINGUT/DA AL MINI ARCADE --- \n Tria una opció: \n 1.Jugar a Pedra, Paper, Tisora \n 2.Jugar a endevinar el número \n S.Sortir")
        #Mostrem el menú d'opcions a l'usuari.

        tria=input() #Guardem l'input de l'usuari a la variable tria.

        match tria: #Fem un match case per establir què s'ha de fer en cada cas.

            case "1": #En el cas que tria (l'input)  sigui 1...
                
                janken() #Cridem la funció janken i juguem a pedra / paper / tisores.

            case "2": #En el cas que tria (l'input)  sigui 2...
        
                nana() #Cridem la funció nana i juguem a endevinar un número.

            case "S": #En el cas que tria (l'input)  sigui S...
                
                print("Has escollit l'opció ""Sortir"". A continuació es finalitzarà el programa. Fins a la pròxima!")

                break #Trenquem el bucle per a que s'executi el que hi ha a continuació.

            case _: #En el cas que tria (l'input) no coincideixi amb cap dels anteriors...
                
                print("L'input introduït NO és vàlid. Torna-ho a provar.")         
                #Avisem a l'usuari que l'input és incorrecte i tornem a demanar-li input.

    quit() #FINALITZEM EL PROGRAMA.

Main()