import os
import logo 
def terminal_clear():
    os.system('cls' if os.name == 'nt' else 'clear')



print(logo.logo)
print("\n****************** Willkommen beim Taschenrechnerprogramm ******************\n")



def addition(zahl1,zahl2):
    return zahl1 + zahl2

def subtraktion(zahl1,zahl2):
    return zahl1 - zahl2

def multiplikation(zahl1,zahl2):
    return zahl1 * zahl2

def division(zahl1,zahl2):
    return zahl1 / zahl2



operationen = {
    
    "+": addition,
    "-": subtraktion,
    "*": multiplikation,
    "/": division,
    
}


def calculator():
    sollte_akkumulieren = True
    ersteZahl = float(input("\nWas ist die erste Zahl: "))
    while sollte_akkumulieren:
        
        print("""
        Wählen Sie eine Operation:
        ==========================
        +    (Addition)
        -    (Subtraktion)
        /    (Division)
        *    (Multiplikation)
        ==========================
        """)
        operation_symbol = input("\nWelche Operation möchten Sie durchführen: ")
        zweiteZahl = float(input("\nWas ist die zweite Zahl: "))
        antwort = operationen[operation_symbol](ersteZahl, zweiteZahl)
        print(f"{ersteZahl} {operation_symbol} {zweiteZahl} = {antwort}")


        auswahl = input("\nWenn Sie die vorherige Zahl verwenden möchten, drücken Sie 'w',um eine neue Berechnung zu starten, drücken Sie 'n': ")

        if auswahl == "w":
            ersteZahl = antwort
        else:
            sollte_akkumulieren = False
            terminal_clear()
            calculator()
            
            
            
calculator()