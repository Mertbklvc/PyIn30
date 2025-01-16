import random
phasen = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''']

print("--------------------Willkommen zum Galgenmännchen-Spiel!--------------------")
leben = 6
game_over = False
wörter = ["haus", "apfel", "strasse", "leben", "freund", "schmetterling", "wissenschaft", "geschwindigkeit", "entschuldigung", "zug", "buch", "baum", "licht", "liebe", "familie", "zeitung", "wald", "königin", "universität", "entwicklung", "gedächtnis", "krankenschwester", "abendessen", "schneeflocke", "schlüsselbund", "handy", "verantwortung", "mensch", "freundlichkeit", "erfahrung", "herausforderung"]
word = random.choice(wörter)
leere_vermutung = ""



for i in word:
    leere_vermutung += "_" + " "

print(leere_vermutung)
korrekter_buchs = []
while not game_over:
    
    vermutung = input("\nVermutung: ")
    gefüllte_vermutung = ""
    for i in word:
        if i == vermutung:
            gefüllte_vermutung += i
            korrekter_buchs.append(vermutung)
           
        elif i in korrekter_buchs:
            gefüllte_vermutung += i
        else:
            gefüllte_vermutung += "_"
            
          
    print(gefüllte_vermutung)
    
    if vermutung not in word:
        leben -= 1
        if leben == 0:
            print("Game OVER!")
            game_over = True
            

   
    
    
    if "_" not in gefüllte_vermutung:
        game_over = True
        print("You Win!")
        
    print(phasen[leben])