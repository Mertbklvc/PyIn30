import art
import os
import time
import sys
import kaffeesorten

def clear_screen():

    os.system('cls' if os.name == 'nt' else 'clear')



def closing_animation():
    # Schließanimation-Simulation
    print("Kaffeemaschine wird heruntergefahren...")
    for i in range(3, 0, -1):
        sys.stdout.write(f"Herunterfahren... {i}\r")
        sys.stdout.flush()
        time.sleep(1)

    print("Die Kaffeemaschine ist ausgeschaltet. Bis bald!")
    main()
    

def loading_animation(maschine_start):
        if maschine_start == 1:
            print("\nDie Kaffeemaschine schaltet sich ein, bitte warten Sie!")
            time.sleep(1)
            for i in range(3): 
                sys.stdout.write("\rWird geladen" + ".." * i)  
                sys.stdout.flush()  
                time.sleep(1)  
            print("\nSie können die Maschine jetzt benutzen!")
            time.sleep(1)
            print(art.kaffeemaschineon)
        else:
            print("Sie haben eine falsche Taste gedrückt.")
            wieder = int(input("\nBitte drücken Sie die 1, um die Kaffeemaschine zu starten: "))
            loading_animation(wieder)
            
            
summe = 0       
behalter = {
    "Wasser" : 2000,
    "Milch" : 1000,
    "Kaffee" : 500,
    
}

def report():
    print(f"Verbleibende Wassermenge: {behalter['Wasser']} ml")
    print(f"Verbleibende Milchmenge: {behalter['Milch']} ml")
    print(f"Verbleibende Kaffeemenge: {behalter['Kaffee']} g")
          
def zahlunginfo(wahl):
    if wahl == 1:
        print("\nBitte zahlen Sie 1,50€")
    elif wahl == 2:
        print("\nBitte zahlen Sie 2,90€")
    elif wahl == 3:
        print("\nBitte zahlen Sie 2,70€")
    elif wahl == 4:
        print("\nBitte zahlen Sie 1,90€")
    else: 
        print("\nBitte geben Sie eine gültige Zahl ein!")
        wahl2 = int(input("\nWelchen Kaffee möchten Sie? Bitte geben Sie die Nummer ein, die auf der Kaffeemaschine steht: "))
        zahlunginfo(wahl2)
        
def zahlung(summe,kaffeewahl):
    euro2 = int(input("\nWie viele 2-Euro-Münzen haben Sie? "))
    euro1 = int(input("\nWie viele 1-Euro-Münzen haben Sie? "))
    euro50 = int(input("\nWie viele 50-Cent-Münzen haben Sie? "))
    euro20 = int(input("\nWie viele 20-Cent-Münzen haben Sie? "))
    euro10 = int(input("\nWie viele 10-Cent-Münzen haben Sie? "))
    summe += euro2*200 + euro1*100 + euro50*50 + euro20*20 + euro10*10
    rest = 0
    
    if summe >= (kaffeesorten.kaffee["espresso"]["kosten"]*100) and kaffeewahl == 1:
        print("\nDie Zahlung war erfolgreich. Ihr Kaffee wird zubereitet...")
        behalter["Wasser"] -= kaffeesorten.kaffee["espresso"]["Zutaten"]["Wasser"]
        behalter["Kaffee"] -= kaffeesorten.kaffee["espresso"]["Zutaten"]["Kaffee"]
        time.sleep(2)
        print(art.kaffeeart)
        rest = summe - 150
        print(f"\nIhr Rückgeld: {rest/100}")
        time.sleep(2)
        closing_animation()
        
    elif summe >= (kaffeesorten.kaffee["filterkaffee"]["kosten"]*100) and kaffeewahl == 4:
        print("\nDie Zahlung war erfolgreich. Ihr Kaffee wird zubereitet...")
        behalter["Wasser"] -= kaffeesorten.kaffee["filterkaffee"]["Zutaten"]["Wasser"]
        behalter["Kaffee"] -= kaffeesorten.kaffee["filterkaffee"]["Zutaten"]["Kaffee"]
        behalter["Milch"] -= kaffeesorten.kaffee["filterkaffee"]["Zutaten"]["Milch"]
        time.sleep(2)
        print(art.kaffeeart)
        rest = summe - 190
        print(f"\nIhr Rückgeld: {rest/100}")
        time.sleep(2)
        closing_animation()
    elif summe >= (kaffeesorten.kaffee["cappuccino"]["kosten"]*100)  and kaffeewahl == 3:
        print("\nDie Zahlung war erfolgreich. Ihr Kaffee wird zubereitet...")
        behalter["Wasser"] -= kaffeesorten.kaffee["cappuccino"]["Zutaten"]["Wasser"]
        behalter["Kaffee"] -= kaffeesorten.kaffee["cappuccino"]["Zutaten"]["Kaffee"]
        behalter["Milch"] -= kaffeesorten.kaffee["cappuccino"]["Zutaten"]["Milch"]
        time.sleep(2)
        print(art.kaffeeart)
        rest = summe - 270
        print(f"Ihr Rückgeld: {rest/100}") 
        time.sleep(2)
        closing_animation()
           
    elif summe >= (kaffeesorten.kaffee["latte"]["kosten"]*100) and kaffeewahl == 2:
        print("\nDie Zahlung war erfolgreich. Ihr Kaffee wird zubereitet...")
        behalter["Wasser"] -= kaffeesorten.kaffee["latte"]["Zutaten"]["Wasser"]
        behalter["Kaffee"] -= kaffeesorten.kaffee["latte"]["Zutaten"]["Kaffee"]
        behalter["Milch"] -= kaffeesorten.kaffee["latte"]["Zutaten"]["Milch"]
        time.sleep(2)
        print(art.kaffeeart)
        rest = summe - 290
        print(f"\nIhr Rückgeld: {rest/100}")  
        time.sleep(2)
        closing_animation()
        
    else:
        print("\nDie Zahlung war nicht erfolgreich. Bitte versuchen Sie wieder!")
        time.sleep(2)
        clear_screen()
        print(art.kaffeemaschineon)
        neusumme = summe / 100
        wiederwahl2 = int(input(f"\nGerade haben Sie {neusumme}€. Welchen Kaffee möchten Sie? Bitte geben Sie die Nummer ein, die auf der Kaffeemaschine steht: "))

        zahlung(summe,wiederwahl2)
        
    
def main():

    print(art.kaffeemaschineoff)
    maschine_start = int(input("\nBitte drücken Sie die 1, um die Kaffeemaschine zu starten: "))
    if maschine_start == 0:
        report()
        time.sleep(2)
        main()
    loading_animation(maschine_start)
    
    
    wahl = int(input(f"\nGerade haben Sie {summe}€. Welchen Kaffee möchten Sie? Bitte geben Sie die Nummer ein, die auf der Kaffeemaschine steht: "))
    time.sleep(1)
    zahlunginfo(wahl)
    print("\nBitte werfen Sie die Münzen ein!")
    time.sleep(1)
    zahlung(summe,wahl)
    

main()