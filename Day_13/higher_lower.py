import art
import random 
import data
import os
import time 
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Kullanım



print(art.logo)
time.sleep(2)

def spiel():
    spiel_status = 1
    punkte = 0
    
    def wahlen():
        person = random.choice(data.inf)
        print(f"Name: {person['name']} \tBeschreibung: {person['description']} \tLand: {person['country']}")
        data.inf.remove(person)
        return person["follower_count"]
    
    def vergleich(a,b):
        if a>b:
            return True
        else:
            return False
        
        
    while spiel_status:
        clear_screen()
        print(f"\t\tDein Punkte: {punkte} \n")
        print("\t\t-------A--------\n")
        a = wahlen()
        print(art.vs)
        print("\t\t-------B--------\n")
        b = wahlen()
        grosser = vergleich(a,b)
        
        spieler_wahl = input("\nWer hat mehr Follower? A oder B?: ").lower()
        if spieler_wahl == "a" and grosser == 1:
            punkte += 1
            
        elif spieler_wahl == "a" and grosser == 0:
            spiel_status = 0
            print(f"\nSpiel Ende! Dein Punkte: {punkte} ")
        elif spieler_wahl == "b" and grosser == 1:
            spiel_status = 0
            print(f"\nSpiel Ende! Dein Punkte: {punkte} ")
        elif spieler_wahl == "b" and grosser == 0:
            punkte +=1
            
            
    
     
spiel()