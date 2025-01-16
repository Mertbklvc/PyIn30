print("Hello"[0])
# Mit eckigen Klammern am Ende eines Strings können wir angeben, welches Element des Strings wir auf dem Bildschirm ausgeben wollen.

print("Hello"[-1])
# Der Zugriff auf eine Liste erfolgt vom Ende her auch über einen negativen Index.

print("123"+"456")
# Alles, was wir in doppelten Anführungszeichen schreiben, wird als String-Ausdruck erkannt.

print(123+456)
# Integer = Whole Number

print(123_456_789)
# Wir können das Aussehen großer ganzer Zahlen mit dem Zeichen _ vereinfachen.

print(3,14159)
# Float-Zahlen sind Dezimalzahlen mit Nachkommastellen, die Brüche oder Werte darstellen, die keine Ganzzahlen sind.

print(True)
print(False)
# Boolean-Werte sind Wahrheitswerte, die entweder „True“ (wahr) oder „False“ (falsch) darstellen.

a = 10
print(type(a))
# Wir können die Funktion type() verwenden, um herauszufinden, welchen Datentyp eine Variable hat.

print(int("123")+ int("456"))
# Wir können den Datentyp eines String-Ausdrucks mit der Funktion int() ändern. Auf diese Weise wandeln wir eine String-Variable in eine Integer-Variable um.
# Natürlich können wir nicht jeden String-Ausdruck in einen Integer-Wert umwandeln. Zum Beispiel können wir den Ausdruck „abc“ nicht in eine ganze Zahl umwandeln.

print("My age: " + str(24))
# Auch haben wir float(), str() und bool().



print(12 + 24)
print(7 - 3)
print(3 * 2)
print(4 ** 4)
# Mathematische Operationen


print(6 / 2)
print(6 // 2) 
# Der Operator / führt eine Gleitkommadivision (mit Nachkommastellen) durch, während // eine ganzzahlige Division (ohne Nachkommastellen, nur den Ganzzahlanteil) liefert.

print(round(30.8))
print(round(30.2))
print(round(3.14159, 2))  # Ergebnis: 3.14
# Die round()-Funktion in Python wird verwendet, um eine Zahl auf eine bestimmte Dezimalstelle zu runden.

score = 0
score += 1
print(score)
# In Python steht += für einen kombinierten Zuweisungsoperator, der den Wert einer Variablen um einen bestimmten Wert erhöht und das Ergebnis der Variablen wieder zuweist.

x = 5
x += 3  # entspricht: x = x + 3
print(x)  # Ergebnis: 8


character_name = "Mert"
character_score = 0
character_is_winning = False
print(f"{character_name}-Score ist {character_score} und Charaktergewinnstatus ist {character_is_winning}")
# Ein f-string (formatierter String) in Python ermöglicht es, Variablen und Ausdrücke direkt in einen String einzufügen. Er beginnt mit einem f oder F vor den Anführungszeichen.

