from jocs import janken, nana # Importen la funció janken i nana del fitxer jocs.  

def main():

    while True: 

        # Demanem escollir opció a l'usuari.
        tria = input(f"\n--- BENVINGUT/DA AL MINI ARCADE ---\n\nTria una opció:\n  1.Jugar a Pedra, Paper, Tisora\n  2.Jugar a endevinar el número\n  s.Sortir\n").strip().lower() #Guardem l'input de l'usuari a la variable tria.

        # Si l'opció es correcta es juga sino es torna a demanar
        match tria:

            case "1": 
                # Juguem a pedra / paper / tisores.
                janken() 

            case "2":
                # Juguem a endevinar un número.
                nana() 

            case "s": 
                # Sortim del programa.
                print(f"Has escollit l'opció \"Sortir\". A continuació es finalitzarà el programa. Fins a la pròxima!")
                break

            case _:
                # L'opcio triada es incorrecta
                print("L'input introduït NO és vàlid. Torna-ho a provar.")         

main()
quit()