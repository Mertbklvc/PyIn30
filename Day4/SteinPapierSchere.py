import random
import time


Stein = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


Papier = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""


# Scissors
Schere = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

#stein 0
#papier 1
#schere 2
game_images = [Stein,Papier,Schere]
game_text = ["Stein", "Papier", "Schere"]
auswahl = int(input("\nDrücken Sie 0 für Stein, 1 für Papier und 2 für Schere: \n"))
print(game_images[auswahl])
print(game_text[auswahl])
print("\n----------------------------------------------------------\n")

time.sleep(2)
computer = random.randint(0,2)

if auswahl == computer:
    print(game_images[computer])
    print(game_text[computer])
    print("\nUnentschieden!")
elif (auswahl == 0 and computer == 2) or (auswahl == 1 and computer == 0) or (auswahl == 2 and computer == 1):
    print(game_images[computer])
    print(game_text[computer])
    print("\nSie haben gewonnen!")
else:
    print(game_images[computer])
    print(game_text[computer])
    print("\nSie haben verloren!")
    
