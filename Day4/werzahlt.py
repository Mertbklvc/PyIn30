import random

friends = ["Mert", "Sinem", "Mehmet", "İrem", "Arda", "Bektaş"]

# erste Option 

randomzahl = random.randint(0,len(friends)-1)
print(randomzahl)
print(f"\ndie Person, die die Rechnung bezahlt: {friends[randomzahl]}")

# Zweite Option

zahler = random.choice(friends)
print(f"\ndie Person, die die Rechnung bezahlt: {zahler}")
