print("Wilkommen bei meinem zahlen rate spiel!")

import random

Schwiereigkeit = input("Willst du es einfach, mittel oder schwer?")

if Schwiereigkeit == "Einfach" or Schwiereigkeit == "einfach":
    print("Du hast dich fuer einfach entschieden!")
    Zahl_Computer = random.randint(1, 10)

elif Schwiereigkeit == "Mittel" or Schwiereigkeit == "mittel":
    print("Du hast dich fuer Mitte entscheiden!")    
    Zahl_Computer = random.randint(1, 50)

elif Schwiereigkeit == "Schwer" or Schwiereigkeit == "schwer":
    print("Du hast dich fuer schwer entscheiden!")
    Zahl_Computer = random.randint(1, 100)

else:
    print("Error: Gib bitte Einfach, Mittel oder Schwer ein!")


Zahl_Spieler = int(input("Bitte waehl deine Zahl"))

while True:
    if Zahl_Spieler == Zahl_Computer:
        print(f"Die Zahl{Zahl_Computer} ist richtig!")
        break
    elif Zahl_Spieler < Zahl_Computer:
        print(f"Die Zahl {Zahl_Spieler} ist zu klein!")
        
    elif Zahl_Spieler > Zahl_Computer:
        print (f"die Zahl{Zahl_Spieler} ist zu gross!")
        
    elif Zahl_Spieler < 100:
        print ("Zahl zu gross")
    else:
        print("bitte gib eine gültige Zahl ein")
        
