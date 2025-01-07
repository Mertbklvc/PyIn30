import random
import mein_modul


randomzahl = random.randint(1,9)
print(randomzahl)

# In Python ist random ein Modul, mit dem man Zahlen oder Werte erzeugen kann, die zufällig erscheinen. Es wird häufig für Aufgaben wie Simulationen, Spiele 
# -oder das zufällige Auswählen von Daten verwendet.

mertsLieblingszahl = mein_modul.meineLieblingszahl 
print(mertsLieblingszahl)

# Ein eigenes Modul in Python erstellst du, indem du Funktionen oder Variablen in einer .py-Datei speicherst und diese anschließend mit import dateiname in 
# -deinem Programm nutzt.

randomzahlvon0bis1 = random.random()
randomzahl2 = random.random() * 10
print(randomzahlvon0bis1)
print(randomzahl2)
# random.random(): Liefert eine Zahl zwischen 0 und 1, die zufällig ist.
# Wir können die Funktion random() auch mit verschiedenen Zahlen multiplizieren.

randomzahlmit10 = random.uniform(1, 10)

# random.uniform() liefert eine Zahl zwischen 0 und 10. Inklusive 10.


städte_in_Deutschland = ["Bamberg", "München", "Frankfurt"]
print(f"\n{städte_in_Deutschland[0]} ist die beste Stadt in Deutschland")
städte_in_Deutschland[1] = "Münih"
print(städte_in_Deutschland[1])
# In Python ist eine Liste eine Datenstruktur, die mehrere Elemente in einer geordneten Reihenfolge speichert, 
# -verschiedene Datentypen enthalten kann (z. B. Zahlen, Texte oder andere Listen) und deren Inhalt durch Hinzufügen, Löschen oder Aktualisieren veränderbar ist.

# Eine Datenstruktur ist eine Methode, um Daten zu organisieren, zu speichern und effizient darauf zuzugreifen, beispielsweise 
# -Listen, Arrays oder Wörterbücher in Python.

# Listen in Python sind vielseitig und speichern unterschiedliche Datentypen, während Arrays effizienter und für mathematische Berechnungen optimiert sind, 
# -aber nur gleiche Datentypen enthalten.

städte_in_Deutschland.append("Berlin")
print(f"\n{städte_in_Deutschland}")

# append() ist eine Methode in Python, um ein Element am Ende einer Liste hinzuzufügen.

städte_in_Deutschland.extend(["Bremen","Hamburg"])
print(f"\n{städte_in_Deutschland}")
print(len(städte_in_Deutschland))

# extend ist eine Methode in Python, um mehrere Elemente (z. B. aus einer Liste) an eine bestehende Liste anzuhängen.


lebensmittel = [
    ["Apfel", "Birne", "Banane", "Erdbeere"],  # Obst
    ["Karotte", "Gurke", "Kartoffel", "Zwiebel"]  # Gemüse
]

# Verschachtelte Liste mit Obst und Gemüse


print("Obst:", lebensmittel[0])
print("Gemüse:", lebensmittel[1])

# Obst und Gemüse separat ausgeben


print("Ein Beispiel für Obst:", lebensmittel[0][2])  # Banane
print("Ein Beispiel für Gemüse:", lebensmittel[1][0])  # Karotte

# Einzelnes Element ausgeben