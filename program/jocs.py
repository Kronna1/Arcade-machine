from random import randint # Importem la funció per obtenir un integer (enter) aleatori.
from time import sleep
from robot import robot # Importem la funció corresponent a la tria del contrincant.


# Funció que juga una partida de pedra / paper / tisores i retorna el guanyador.
def janken_play(r): 
    # Per comoditat, assigno llista de moviments a una nova variable.
    movs = r.game

    # Demanem moviment a l'usuari
    while True:
        mov_usuari = input(f"\nTria el teu pròxim moviment escrivint alguna de les paraules següents a la consola:\n  Pedra\n  Paper\n  Tisora\n").strip().lower()
        
        # Si el moviment triat es troba a la llista de moviments comença el joc.
        if mov_usuari in movs:
            print(f"\nPedra, paper, tisores!")
            sleep (2)

            # El robot fa el seu moviment.
            mov_robot = r.playing()

            print(f"El teu moviment és {mov_usuari}\nEl moviment de {r.name} és {mov_robot}")        
            sleep (2)

            # Si el jugador empata amb el robot...
            if mov_usuari == mov_robot:
                print(f"Empat!")
                return "empat"

            # Fixant-me, la llista de moviments està ordenada de forma que el moviment posterior és el guanyador del anterior
            # així que si movem l'índex de la llista una posició podem obtenir el seu contramoviment.
            # Si moviment del jugador es igual a contramoviment del robot guanyes.
            elif mov_usuari == movs[(movs.index(mov_robot) + 1) % len(movs)]:
                print(f"Has guanyat!")
                return "jugador"

            # Sino, has perdut.
            else:
                print(f"Has perdut!") 
                return "robot"
        
        # En cas de que el moviment NO es trobi a la llista (moviment NO vàlid), es torna a demanar.
        else:
            print("L'input introduït NO és vàlid. Torna-ho a provar.")


# Juguem pedra / paper / tisores
def janken ():

    # Creem una instància de robot.
    r = robot()

    # Definim la puntuació i el comptador d'empats.
    punts_usuari = 0
    punts_robot = 0
    empats = 0

    # Demanem el mode de joc.
    while True:
        mode = input(f"\nTria el mode de joc:\n  1.El primer que arribi a 3 victòries.\n  2.El millor de 5 jugades.\n  s.Sortir\n").strip().lower()

        match mode:
            
            # El primer que arribi a 3 victòries.
            case "1": 

                # Juguem fins que algun jugador te 3 punts
                while punts_usuari < 3 and punts_robot < 3:
        
                    # Juguem una partida i sumem els punts al jugador corresponent.
                    resultat = janken_play(r)

                    if resultat == "empat":
                        empats += 1
                    elif resultat == "jugador":
                        punts_usuari += 1
                    else:
                        punts_robot += 1

                    # Imprimim el estat de la partida
                    sleep (2)
                    print(f"\nEstat del joc:\n  Empats: {empats}\n  Punts del jugador: {punts_usuari}\n  Punts de {r.name}: {punts_robot}")

            # El millor de 5 jugades.
            case "2":

                # juguem 5 rondes
                for i in range(5):
                    
                    # Juguem una partida i sumem els punts al jugador corresponent.
                    resultat = janken_play(r)

                    if resultat == "empat":
                        empats += 1
                    elif resultat == "jugador":
                        punts_usuari += 1
                    else:
                        punts_robot += 1

                    # Imprimim el estat de la partida
                    sleep (2)
                    print(f"\nEstat del joc:\n  Ronda {i + 1}\n  Empats: {empats}\n  Punts del jugador: {punts_usuari}\n  Punts de {r.name}: {punts_robot}")

            # Sortim del selector de mode al menú principal.
            case "s":
                print("Has escollit sortir del joc. A continuació es surtirà al menú principal. Fins a la pròxima!")
                break
            
            # El mode no existeix, es torna a intentar.
            case _:
                print("L'input introduït NO és vàlid. Torna-ho a provar.")
                continue
        
        # Es dona el guanyador a l'acabar un joc.
        sleep (2)
        print(f"\nFi de la partida:")

        if punts_usuari == punts_robot:
            print(f"Heu empatat!")

        if punts_usuari > punts_robot:
            print("Feliciats, has guanyat!")

        else:
            print("Has perdut!")

        sleep (2)
        break


# Juguem a averiguar un número.
def nana(): 
    
    # Generem un nombre aleatori entre 1 i 100.
    numero_generat = randint(1,100) 

    # Creem un comptador d'intents.
    intents = 0 

    # Comença el joc.
    while True:

        # Demanem un número a l'usuari.
        numero_averigua = input(f"\nHe pensat un nombre entre 1 i 100. Prova d'endevinar-lo.\n")

        # Comprovem que l'input de l'usuari és un número.
        if numero_averigua.isnumeric():
        
            # Afegim 1 al comptador d'intents i convertim l'input de l'usuari en un número.
            intents += 1
            numero_averigua = int(numero_averigua)

            # Comprobem que el número estigui entre l'1 i 100.
            if numero_averigua > 100 or numero_averigua < 1: 

                print (f"L'input és massa gran o petit. Torna-ho a intentar. És un número entre 1 i 100.")
            
            else:
                
                # Imprimim el resultat del joc al jugador
                if numero_averigua > numero_generat:
                    print ("Massa alt!")
            
                elif numero_averigua < numero_generat:
                    print ("Massa baix!")
                
                else:
                    print (f"\nFelicitats! Has encertat en el teu intent número {intents}!")
                    sleep (2)
                    break
            
            
        # L'input del jugador NO és un número, es torna a demanar.
        else:
            print("L'input introduït NO és vàlid. Torna-ho a provar.")
            
            
