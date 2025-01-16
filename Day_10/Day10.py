def format_name(vorname,nachname):
    full_name = ""
    vorname = vorname.title()
    nachname = nachname.title()
    full_name = vorname + " " + nachname
    
    return full_name


bearbeitete_version = format_name("mert","beklevic")
print(bearbeitete_version)

# In Python geben Funktionen mit return ein Ergebnis zurück, nachdem sie etwas berechnet haben. Du kannst dieses Ergebnis speichern und später verwenden.

def multiplication(zahl1,zahl2):
    return zahl1 * zahl2


def quadrat(zahl):
    return zahl **2


print(quadrat(multiplication(5,4)))

# Wie in diesem Beispiel zu sehen ist, können wir von einer return-Funktion eine Ausgabe erhalten und diese in eine andere Funktion einsetzen.


def multiplication2(zahl1,zahl2):
    return zahl1 * zahl2
    print("Hello")
    
print(multiplication2(3,4))

# Wir können die Zeile mit print(Hello) nicht sehen.
# Nach return wird der Code in der Funktion nicht mehr ausgeführt, weil return die Funktion sofort beendet. Alles, was danach steht, wird ignoriert.


def text_lower(text):
    if text == text.lower():
        return "Ihr Text ist bereits klein geschrieben"
    return text.lower()



print(text_lower("QMEQWEMQWEŞ"))
print(text_lower("qwelşöwöeqlöeqw"))

# Eine Funktion kann mehrere return-Anweisungen haben, aber nur diejenige, deren Bedingung erfüllt ist, wird ausgeführt. Danach wird die Funktion beendet.



def add_zwei(zahl):
    """ Dies ist eine Funktion, die 2 zu einer Zahl addiert.
    
    """
    return zahl +2


print(add_zwei(8))

# In Python werden Docstrings verwendet, um Funktionen, Klassen oder Module zu dokumentieren. Sie erklären, was der Code macht, 
# welche Parameter er erwartet und was er zurückgibt.

def multipliziere(a, b):
    return a * b

mein_func = multipliziere
print(mein_func(3, 4))  # Ausgabe: 12

# In Python können Funktionen wie Werte an Variablen zugewiesen werden. 