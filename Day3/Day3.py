print("\nWillkommen in der Achterbahn!\n")
height = int(input("Wie groß sind Sie? (cm)\n"))

if height > 120:
    print("Sie können mit der Achterbahn fahren!")
else:
    print("Leider können Sie nicht mit der Achterbahn fahren!")
    
    
# Wenn 120 eingeschlossen werden soll, muss es als >= verwendet werden.

alter = int(input("\nWie alt sind Sie?\n"))

if alter == 18:
    print("Sie sind 18 Jahre Alt")
    
# = Zuweisungsoperator, weist einen Wert einer Variablen zu. z.B: x = 10
# == Vergleichsoperator, prüft, ob zwei Werte gleich sind, und gibt True oder False zurück. z.B: alter == 18

x = 10%3
print(x)
# In Python und Mathematik bedeutet % den Modulo-Operator. Er gibt den Rest einer Division zurück.


print("\nWillkommen in der Achterbahn!\n")
height = int(input("Wie groß sind Sie? (cm)\n"))
bill = 0

if height > 120:
    print("Sie können mit der Achterbahn fahren!")
    age = int(input("Wie alt sind Sie?\n"))
    if age <= 12:
        bill = 5
        print("Die Eintrittskarte kostet 5€!\n")
    elif age <=18:
        bill = 7
        print("Die Eintrittskarte kostet 7€!\n")
    elif age >= 45 and age <= 55:
        print("Die Eintrittskarte kostet 0€!\n")
    else:
        bill = 12
        print("Die Eintrittskarte kostet 12€!\n") 
    
    photo = input("Möchten Sie auch ein Foto machen lassen? Drücken Sie 'y' für Ja oder 'n' für Nein!\n")  
    if photo == "y":
        bill += 3
        
    print(f"\nBitte zahlen Sie {bill}€!\n")
        
else:
    print("Leider können Sie nicht mit der Achterbahn fahren!")
    
    
# Mit verschachtelten If-Else-Anweisungen können wir zwei verschiedene Bedingungen überprüfen!             
# elif wird in Python verwendet, um zusätzliche Bedingungen in einer If-Else-Struktur zu prüfen.


a = 13
if a > 12 and a < 18:
    print("12<a<18")

b = 8
if b > 12 or b%2 == 0:
    print("True!")
    
# and: Beide Bedingungen müssen wahr sein (UND).
# or: Mindestens eine Bedingung muss wahr sein (ODER).
# not: Kehrt den Wahrheitswert um (NICHT).