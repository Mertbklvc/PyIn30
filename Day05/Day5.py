fruits = ["Apfel","Kirsche","Pfirsch"]

for fruit in fruits:
    print(fruit)
    print(fruit + " " +"Pie")

print(fruits)

# In Python sind for-Schleifen eine Kontrollstruktur, die verwendet wird, um eine Sequenz (wie eine Liste, ein Tuple, eine Zeichenkette oder einen Bereich) 
# -zu durchlaufen. Sie ermöglichen es, eine Aktion wiederholt für jedes Element in der Sequenz auszuführen.

# Beachten Sie, dass die Operation außerhalb der for-Schleife nur einmal durchgeführt wird!

studenten_noten = [70,12,34,56,75,43,23,13,68,55,62,43,42,40,20,10,4,74,87]

total_studenten_noten = sum(studenten_noten)
print(total_studenten_noten)


sum_studenten_noten = 0
for i in studenten_noten:
    sum_studenten_noten += i
    
print(sum_studenten_noten)

# Eigentlich kann die in Python vorhandene Funktion sum() auch mit einer for-Schleife selbst erstellt werden.


max_studenten_noten = max(studenten_noten)
print(max_studenten_noten)

max_note = 0
for i in studenten_noten:
    if i > max_note:
        max_note = i
        
        
print(max_note)

# Die höchste Note können wir auch mit einer selbst geschriebenen Schleife finden.


for number in range(0,10):
    print(number)
    
# range() in Python ist eine Funktion, die eine Sequenz von Zahlen erzeugt, z. B. für Schleifen: range(start, stop, step).

sum_von1_bis100 = 0

for i in range(1,101):
    sum_von1_bis100 += i
    
print(sum_von1_bis100)