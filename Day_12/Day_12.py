feinde = 1

def feinde_erhöhen():
    feinde = 2
    print(f"Feinde innerhalb der Funktion: {feinde}")
    
    
    
feinde_erhöhen()
print(f"Feinde außer der Funktion: {feinde}")

# Globale Variablen: Sie werden außerhalb von Funktionen definiert und sind im gesamten Programm verfügbar.
# Lokale Variablen: Sie werden innerhalb von Funktionen definiert und sind nur dort gültig.


spiel_niveu = 3
feinde = ["Skelett","Zombie","Außerirdischer"]

if spiel_niveu < 5:
    neuer_Feind = feinde[0]
    
print(neuer_Feind)

# In Python bildet ein if-Block keinen eigenen Gültigkeitsbereich, und Variablen darin sind auch außerhalb zugänglich, 
# während in Java ein if-Block einen eigenen Scope hat und Variablen darin außerhalb nicht verfügbar sind.



leben_zahl = 3


def erhöht_leben_zahl():
    global leben_zahl
    leben_zahl +=1
    print(f"leben_zahl ist {leben_zahl}")
    
    
erhöht_leben_zahl()

# Mit dem Schlüsselwort global kann innerhalb einer Funktion auf Variablen außerhalb der Funktion zugegriffen werden.

PI = 3.14

# Wenn wir eine Konstante erstellen wollen, müssen wir alle Buchstaben groß schreiben.


def math_functions():
    print(PI)
    

math_functions()


# Ein Constant in Python ist eine Variable, deren Wert während des Programms nicht geändert werden sollte. Sie werden üblicherweise in Großbuchstaben benannt,
# z. B. PI = 3.14. Python erzwingt jedoch keine echten Konstanten; es ist eine Konvention.