# Arcade Machine

## Tasca final del projecte "Programació orientada a objectes"... 

##### ...amb el que s'han guanyat coneixements bàsics de programació emprant el llenguatge Python i s'ha realitzat una introducció al treball mitjançant repositoris en Git i GitHub. 

##### Aquesta consisteix en crear un programa que s'executa en bucle mostrant  joc arcade que mitjançant un menú de selecció permet triar entre jugar de Janken i averigua el número.


**INSTRUCCIONS**

*El programa es construeix a partir de diversos fitxers (mòduls):*

- main.py (construeix el menú general i crida les funcions de joc.py)
<br>

- jocs.py (fitxer en el que s'importen les llibreries i mètodes necessaris per executar els jocs)
<br>

- robot.py (arxiu donat pel professorat en el que es crea un robot "contrincant virtual" per jugar a Janken)

Per executar el programa és necessari descarregar els 3 fitxers, però només executar en terminal main.py (ja que la resta només defineixen funcions i mètodes).
<br>
En primer lloc es mostrarà un menú amb diverses opcions:
1. Janken (pedra/paper/tisora)
<br>
2. Averigua el número
<br>
S. Sortir
<br>

Amb les opcions 2 i S l'output serà directe:
<br>
2.Executarà un joc d'endevinar un nº aleatori generat entre 1 i 100.
<br>
L'usuari introdueix nombres, l'ordinador retorna pistes "massa alt!", "massa baix!" fins que l'usuari descobreix el nº, llavors l'ordinador felicita a l'usuari i li indica el nº d'intents realitzats.
<br>
S. Donarà l'avís de que el programa es tancarà i doanrà un missatge de comiat.
<br>

En el cas d'escollir 1 es mostrarà una tria de mode de joc, on:
<br>
1.El primer que arribi a 3 victòries
<br>
2.El millor de 5 rondes
<br>
S.Sortir

