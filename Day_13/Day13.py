

try:
    age = int(input("Wie alt bist du? "))

except ValueError:
    print("\nSie haben keinen ganzzahligen Wert eingegeben. Bitte geben Sie eine Zahl ein!")
    age = int(input("\nWie alt bist du? "))

if age >= 18:
    print("Du kannst eintreten!")
    
    
    
# try und except in Python sind Befehle zur Fehlerbehandlung: try versucht, einen Codeblock auszuführen,
# und except fängt auftretende Fehler ab, um sie zu behandeln.