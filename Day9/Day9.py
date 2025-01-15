woerterbuch = {
    "name": "Mert",
    "alter": 24,
    "stadt" : "Bamberg", 
    
}

print(woerterbuch["name"])
print(woerterbuch["alter"])
print(woerterbuch["stadt"])


# Ein Dictionary (Wörterbuch) in Python ist eine Datenstruktur, die Schlüssel-Wert-Paare speichert. Jeder Schlüssel (key) ist einzigartig und 
# mit einem bestimmten Wert (value) verknüpft.

woerterbuch["Universität"] = "Otto-Friedrich Universität Bamberg"

# Wenn wir einen neuen Key-Value zu unserem Dictionary hinzufügen wollen:

print(woerterbuch)

empty_dict = {}
empty_dict["das Haus"] = "Ev"
print(empty_dict)

# Wenn wir ein neues Empty- Dictionary erstellen wollen:

woerterbuch = {}
print(woerterbuch)

# Wenn wir unser Dictionary löschen wollen:


autos = {
    "Deutschland" : "BMW",
    "Japan" : "Toyota",
    "Italien" : "Ferrari",  
}

for auto in autos:
    print(f"Land {auto} hat {autos[auto]}")

# Wenn wir in einem Dictionary eine Schleife machen möchten:



reise_log = {
    "Frankreich" : ["Paris","Marseille", "Strasbourg"] , 
    "Deutschland" : ["München", "Bamberg", "Frankfurt", "Stuttgart"], 
    "Türkei" : ["Istanbul","Izmir", "Antalya"],
    

}

print(reise_log["Deutschland"][1])

noten = [
    ["Ali", [85, 90]], 
    ["Ayşe", [78, 88]]
]

print(noten[0][1][0])  # Ausgabe: 85


# Nested Liste und Nested Dictionary sind Strukturen, die Daten in mehreren Ebenen organisieren. Beide ermöglichen die Arbeit mit verschachtelten (nested) Daten.

reise_log = {
    "Frankreich" : {
        "besuch_counter" : 2,
        "sterne_bewertung" : 4,
        "bestes_essen" : "Croissant"
        
    },
    "Italien" : {
        "besuch_counter" : 1,
        "sterne_bewertung" : 5,
        "bestes_essen" : "Pizza"
        
    },
   
    

}


print(reise_log["Italien"]["bestes_essen"])

