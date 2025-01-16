def my_function():
    print("\nHello, das ist meine Function!")

my_function()

# Eine Funktion in Python ist ein wiederverwendbarer Block von Code, der eine bestimmte Aufgabe ausführt. Mit einer Funktion kann man wiederholte Aktionen effizient organisieren.
# Funktionen werden mit dem Schlüsselwort def definiert.

# Wie definiert man eine Funktion?
# Mit dem Schlüsselwort def startet man die Definition.
# Man gibt der Funktion einen Namen.
# In den Klammern kann man Parameter angeben (optional).
# Der Codeblock der Funktion wird eingerückt geschrieben.


def addiere(zahl1, zahl2):
    return zahl1 + zahl2

sum = addiere(1,2)
print(sum)

# Wir haben eine Funktion mit zwei Parametern erstellt. 
# return gibt den Wert zurück, den die Funktion als Ergebnis liefert.

x = 0
while x < 5:
    print(x)
    x += 1

# Die while-Schleife wird verwendet, um einen Codeblock so lange auszuführen, wie eine bestimmte Bedingung wahr ist. 
# Sobald die Bedingung falsch wird, beendet die Schleife ihre Ausführung.

# Die while-Schleife wiederholt einen Codeblock, solange eine Bedingung wahr ist, 
# während die for-Schleife über eine bekannte Anzahl von Iterationen oder eine Sequenz läuft.

# .!.!.! In einer while-Schleife muss man sicherstellen, dass die Bedingung irgendwann falsch wird, um Endlosschleifen zu vermeiden.