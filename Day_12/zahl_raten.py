import random
import logo
print(logo.logo)

print("\n----------- Willkommen beim Zahlenratespiel! -----------")
schwierig_grad = input(("\nBitte wählen Sie den Schwierigkeitsgrad des Spiels! Schreiben Sie 'leicht' für leicht und 'schwer' für schwer: "))

def game(spiel_sgrad):
    spiel = 1
    zahl = random.randint(0,101)
    if spiel_sgrad == 'leicht':
        versuch_anzahl = 10
        
    else: 
        versuch_anzahl = 5
        
    while spiel:
        versuch = int(input("\nBitte geben Sie Ihre Zahlenschätzung ein: "))
        
        if versuch_anzahl == 0:
            print("\nSie haben keine Versuche mehr! Das Spiel ist vorbei.")
            print(f"Die richtige Zahl war: {zahl}")
            spiel = 0
                       
       
        if versuch > zahl:
            print("Zu hoch!")
           
        elif versuch < zahl:
            print("Zu niedrig!")
        else:
            print("Sie haben die Zahl gefunden! Glückwunsch!")
            spiel = 0
            
        versuch_anzahl -= 1
        print(f"Verbleibende Versuche: {versuch_anzahl}")
            


game(schwierig_grad)